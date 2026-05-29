import sys
import uuid
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style

from sakipro.ui.console import console
from sakipro.core.config import settings
from sakipro.agents.iku_reviewer import IkuReviewAgent
from sakipro.agents.pk_reviewer import PkReviewAgent
from sakipro.agents.lkjip_reviewer import LkjipReviewAgent
from sakipro.agents.renstra_reviewer import RenstraReviewAgent
from sakipro.agents.rpjmd_reviewer import RpjmdReviewAgent
from sakipro.agents.cascading_reviewer import CascadingReviewAgent
from sakipro.agents.evidence_reviewer import EvidenceReviewAgent
from sakipro.agents.draft_agent import DraftAgent
from sakipro.agents.report_agent import ReportAgent
from sakipro.agents.ask_agent import AskAgent
from sakipro.storage.database import SessionLocal
from sakipro.storage.models import Workspace, Document, TokenUsage, Review
from sakipro.reports.writers import export_to_markdown, export_to_docx

# Basic autocomplete commands
slash_commands = [
    "/help", "/status", "/scan", "/ls", "/cek-indikator", "/cek-cascading", 
    "/review-rpjmd", "/review-pk", "/review-lkjip", "/review-renstra", "/cek-evidence", "/draft", "/report",
    "/token", "/model", "/config", "/profile", "/reset", "/clear", "/exit", "/wizard"
]

command_completer = FuzzyWordCompleter(slash_commands)

# Custom style
style = Style.from_dict({
    'bottom-toolbar': '#ffffff bg:#333333',
})

def bottom_toolbar():
    """Generates the bottom toolbar text."""
    # Using fixed mock values for UI demonstration
    return HTML(f' <b>{settings.default_model}</b> │ DISDIK_2026 │ 9 dok │ Token: 18.420 │ {settings.privacy_mode} │ ctrl+d keluar ')

def start_repl():
    """Starts the interactive REPL."""
    session = PromptSession(
        completer=command_completer,
        bottom_toolbar=bottom_toolbar,
        complete_while_typing=True,
        style=style
    )
    
    print("Ketik /scan untuk index dokumen, /cek-indikator, /review-rpjmd, /review-pk, /review-lkjip, /review-renstra, /cek-cascading, /cek-evidence untuk analisis.")
    print("Ketik /draft untuk usulan teks, /report untuk generate laporan final (DOCX).")
    print("Ketik /status untuk info db, /profile untuk atur konteks Pemda, /reset untuk hapus data, atau /exit untuk keluar.")

    while True:
        try:
            text = session.prompt("sakipro ❯ ")
            if not text.strip():
                continue
                
            if text.strip() == "/exit":
                break
                
            if text.strip() == "/clear":
                console.clear()
                continue
                
            # Dummy logic for processing inputs
            if text.startswith("/"):
                cmd = text.strip().split()[0]
                if cmd == "/scan":
                    args = text.strip().split()
                    folder = args[1] if len(args) > 1 else "."
                    console.print(f"[yellow]⠸ Memindai folder:[/] {folder}")
                    try:
                        from sakipro.documents.scanner import scan_directory
                        count = scan_directory(folder)
                        console.print(f"[green]✓ Selesai:[/] {count} file berhasil diproses.")
                    except Exception as e:
                        console.print(f"[red]Error saat memindai folder:[/] {e}")
                elif cmd == "/ls":
                    import os
                    from rich.table import Table
                    args = text.strip().split()
                    target_dir = args[1] if len(args) > 1 else "."
                    
                    try:
                        table = Table(title=f"Isi Direktori: {target_dir}", style="cyan")
                        table.add_column("Tipe", justify="left", style="yellow")
                        table.add_column("Nama File/Folder", justify="left", style="green")
                        table.add_column("Ukuran", justify="right", style="blue")
                        
                        items = sorted(os.listdir(target_dir))
                        for item in items:
                            if item.startswith('.'):
                                continue # Skip hidden files like .git or .venv
                                
                            item_path = os.path.join(target_dir, item)
                            is_dir = os.path.isdir(item_path)
                            type_str = "📁 Folder" if is_dir else "📄 File"
                            
                            size_str = "-"
                            if not is_dir:
                                size_bytes = os.path.getsize(item_path)
                                if size_bytes < 1024:
                                    size_str = f"{size_bytes} B"
                                elif size_bytes < 1024 * 1024:
                                    size_str = f"{size_bytes/1024:.1f} KB"
                                else:
                                    size_str = f"{size_bytes/(1024*1024):.1f} MB"
                                    
                            table.add_row(type_str, item, size_str)
                            
                        console.print(table)
                    except Exception as e:
                        console.print(f"[red]Gagal membaca direktori:[/] {e}")
                elif cmd in ["/cek-indikator", "/review-rpjmd", "/review-pk", "/review-lkjip", "/review-renstra", "/cek-cascading", "/cek-evidence", "/draft", "/report"]:
                    query = text[len(cmd):].strip()
                    
                    agent = None
                    if cmd == "/cek-indikator":
                        agent = IkuReviewAgent()
                    elif cmd == "/review-rpjmd":
                        agent = RpjmdReviewAgent()
                    elif cmd == "/review-pk":
                        agent = PkReviewAgent()
                    elif cmd == "/review-lkjip":
                        agent = LkjipReviewAgent()
                    elif cmd == "/review-renstra":
                        agent = RenstraReviewAgent()
                    elif cmd == "/cek-cascading":
                        agent = CascadingReviewAgent()
                    elif cmd == "/cek-evidence":
                        agent = EvidenceReviewAgent()
                    elif cmd == "/draft":
                        agent = DraftAgent()
                    elif cmd == "/report":
                        agent = ReportAgent()
                        
                    if agent:
                        from sakipro.ui.spinner import stream_with_spinner
                        response_stream = agent.run({"query": query})
                        wrapped_stream = stream_with_spinner(response_stream, console, message=f"{agent.agent_name} sedang bekerja")
                        
                        output_text = ""
                        for chunk in wrapped_stream:
                            console.print(chunk, end="")
                            output_text += chunk
                        console.print("\n")
                        
                        # Save token usage and review
                        db = SessionLocal()
                        try:
                            # 1 token roughly 4 characters
                            in_tokens = len(query) // 4
                            out_tokens = len(output_text) // 4
                            
                            tu = TokenUsage(
                                id=str(uuid.uuid4()),
                                model=settings.default_model,
                                input_tokens=in_tokens,
                                output_tokens=out_tokens,
                                command=cmd
                            )
                            # Just getting the first active workspace for demo
                            ws = db.query(Workspace).first()
                            ws_id = ws.id if ws else "default_workspace"
                            
                            rev = Review(
                                id=str(uuid.uuid4()),
                                workspace_id=ws_id,
                                command=cmd,
                                summary=output_text[:500]
                            )
                            db.add(tu)
                            db.add(rev)
                            db.commit()
                            
                            # Export report
                            export_path = export_to_markdown(output_text, cmd.strip('/'))
                            console.print(f"[dim]Laporan diekspor ke: {export_path}[/dim]")
                            
                            # Also export to DOCX
                            try:
                                docx_path = export_to_docx(output_text, cmd.strip('/'))
                                console.print(f"[dim]Laporan Word (DOCX) diekspor ke: {docx_path}[/dim]")
                            except Exception as doc_err:
                                console.print(f"[red]Gagal ekspor ke DOCX:[/] {doc_err}")
                                
                        except Exception as e:
                            db.rollback()
                            console.print(f"[red]Gagal menyimpan token usage:[/] {e}")
                        finally:
                            db.close()
                elif cmd == "/status":
                    db = SessionLocal()
                    try:
                        docs_count = db.query(Document).count()
                        token_usages = db.query(TokenUsage).all()
                        total_in = sum(t.input_tokens for t in token_usages)
                        total_out = sum(t.output_tokens for t in token_usages)
                        
                        from rich.panel import Panel
                        console.print(Panel(
                            f"📚 Dokumen Terindeks: {docs_count}\n"
                            f"⚙️ Model Aktif: {settings.default_model}\n"
                            f"🪙 Total Tokens In: {total_in}\n"
                            f"🪙 Total Tokens Out: {total_out}",
                            title="Status SAKIPRO", border_style="blue"
                        ))
                    finally:
                        db.close()
                elif cmd == "/help":
                    from rich.panel import Panel
                    help_text = """[bold cyan]Daftar Perintah SAKIPRO v1.0:[/bold cyan]
                    
[bold yellow]1. Manajemen Workspace & Dokumen[/bold yellow]
[green]/scan <folder>[/]         : Memindai dan meng-index folder dokumen kerja
  [dim]Contoh: /scan ./Dokumen_SAKIP_2026[/dim]
[green]/ls <folder>[/]           : Melihat isi file dan folder kerja saat ini
  [dim]Contoh: /ls atau /ls ./Dokumen[/dim]
[green]/status[/]               : Menampilkan status dokumen terindeks dan pemakaian token
  [dim]Contoh: /status[/dim]
[green]/profile[/]              : Mengatur Konteks Profil Pemda (Tahun, OPD, dll)
  [dim]Contoh: /profile[/dim]

[bold yellow]2. Evaluasi SAKIP[/bold yellow]
[green]/cek-indikator <query>[/]: Memeriksa orientasi hasil dan kelayakan IKU
  [dim]Contoh: /cek-indikator analisis IKU Dinas Pendidikan[/dim]
[green]/review-rpjmd <query>[/]  : Mengaudit Rencana Pembangunan Jangka Menengah Daerah (RPJMD)
  [dim]Contoh: /review-rpjmd cek keselarasan program lintas OPD[/dim]
[green]/review-pk <query>[/]    : Mengaudit keselarasan Perjanjian Kinerja
  [dim]Contoh: /review-pk cek kesesuaian target dengan Renstra[/dim]
[green]/review-lkjip <query>[/] : Mengaudit Laporan Kinerja Instansi Pemerintah (LKjIP)
  [dim]Contoh: /review-lkjip evaluasi bab capaian kinerja[/dim]
[green]/review-renstra <query>[/]: Mengaudit Rencana Strategis (Renstra)
  [dim]Contoh: /review-renstra periksa sasaran strategis[/dim]
[green]/cek-cascading <query>[/]: Mengecek keselarasan pohon kinerja antar level
  [dim]Contoh: /cek-cascading analisis cascading bidang kepegawaian[/dim]
[green]/cek-evidence <query>[/] : Meninjau ketersediaan bukti fisik laporan
  [dim]Contoh: /cek-evidence validasi bukti dukung program A[/dim]

[bold yellow]3. Output & Asisten[/bold yellow]
[green]/draft <query>[/]        : Memberikan usulan draf redaksional teks yang lebih baik
  [dim]Contoh: /draft usulkan perbaikan redaksional indikator X agar berorientasi hasil[/dim]
[green]/report <query>[/]       : Membuat rangkuman temuan menjadi draf LHE (DOCX)
  [dim]Contoh: /report buatkan draf LHE final dari temuan sebelumnya[/dim]

[bold yellow]4. Sistem & Utilitas[/bold yellow]
[green]/wizard[/]               : Menjalankan ulang konfigurasi (setup awal)
[green]/reset[/]                : Menghapus database dan profil agar mulai dari nol
[green]/clear[/]                : Membersihkan layar terminal
[green]/exit[/]                 : Keluar dari aplikasi SAKIPRO"""
                    console.print(Panel(help_text, title="SAKIPRO Help", border_style="cyan"))
                elif cmd == "/wizard":
                    console.print("[bold yellow]Menjalankan Wizard Setup...[/bold yellow]")
                    console.print("1. Pilih Provider AI (Simulasi) -> Selesai")
                    console.print("2. Pilih Workspace (Simulasi) -> Selesai")
                    console.print("[green]Konfigurasi berhasil disimpan.[/green]")
                elif cmd == "/reset":
                    import os
                    from dotenv import unset_key
                    from sakipro.storage.database import init_db, engine
                    
                    console.print("[bold red]Memulai proses reset total...[/bold red]")
                    
                    # 1. Reset Database
                    if os.path.exists(settings.db_path):
                        try:
                            # Tutup semua koneksi SQLite yang aktif (Connection Pool) agar tidak readonly
                            engine.dispose()
                            
                            os.remove(settings.db_path)
                            init_db()  # Buat ulang skema kosong
                            console.print("✓ Database berhasil dihapus dan dikosongkan.")
                        except Exception as e:
                            console.print(f"[red]Gagal menghapus database:[/] {e}")
                            
                    # 2. Reset Profile in .env
                    env_path = ".env"
                    if os.path.exists(env_path):
                        unset_key(env_path, "SAKIPRO_PEMDA_NAME")
                        unset_key(env_path, "SAKIPRO_OPD_NAME")
                        unset_key(env_path, "SAKIPRO_EVAL_YEAR")
                        unset_key(env_path, "SAKIPRO_RPJMD_PERIOD")
                        console.print("✓ Profil konteks global pada konfigurasi berhasil dihapus.")
                        
                    # 3. Reset in-memory settings
                    settings.pemda_name = "[Nama Pemda Belum Diatur]"
                    settings.opd_name = "[Nama OPD Belum Diatur]"
                    settings.eval_year = "[Tahun Belum Diatur]"
                    settings.rpjmd_period = "[Periode Belum Diatur]"
                    
                    console.print("[bold green]✓ SAKIPRO berhasil di-reset ke kondisi nol (fresh start)![/bold green]")
                elif cmd == "/profile":
                    from dotenv import set_key
                    import os
                    console.print("[bold yellow]=== SETUP PROFIL KONTEKS GLOBAL ===[/]")
                    console.print("[dim]Data ini akan menjadi acuan permanen (absolute fact) untuk semua sesi evaluasi AI.[/dim]")
                    pemda = session.prompt("Nama Pemda / Institusi : ", default=settings.pemda_name)
                    opd = session.prompt("Instansi Fokus (OPD)   : ", default=settings.opd_name)
                    tahun = session.prompt("Tahun Evaluasi         : ", default=settings.eval_year)
                    rpjmd = session.prompt("Periode RPJMD          : ", default=settings.rpjmd_period)
                    
                    # Update in memory
                    settings.pemda_name = pemda
                    settings.opd_name = opd
                    settings.eval_year = tahun
                    settings.rpjmd_period = rpjmd
                    
                    # Update in .env
                    env_path = ".env"
                    if not os.path.exists(env_path):
                        open(env_path, 'a').close()
                        
                    set_key(env_path, "SAKIPRO_PEMDA_NAME", pemda)
                    set_key(env_path, "SAKIPRO_OPD_NAME", opd)
                    set_key(env_path, "SAKIPRO_EVAL_YEAR", tahun)
                    set_key(env_path, "SAKIPRO_RPJMD_PERIOD", rpjmd)
                    
                    console.print("[green]✓ Profil berhasil disimpan ke dalam .env dan diterapkan ke dalam memori AI![/]")
                elif cmd == "/token":
                    console.print("[cyan]Informasi pemakaian token terintegrasi di dalam perintah /status.[/cyan]")
                elif cmd == "/model":
                    console.print(f"[cyan]Model aktif saat ini:[/] {settings.default_model}")
                elif cmd == "/config":
                    console.print(f"[cyan]Provider AI:[/] {settings.ai_provider}")
                    console.print(f"[cyan]Privacy Mode:[/] {settings.privacy_mode}")
                    console.print(f"[cyan]Output Dir:[/] {settings.output_dir}")
                else:
                    console.print(f"[yellow]Perintah tidak dikenal:[/] {cmd}")
            else:
                # Menangani input natural language sebagai General Chat / Tanya Jawab
                from sakipro.ui.spinner import stream_with_spinner
                agent = AskAgent()
                
                try:
                    response_stream = agent.run({"query": text.strip()})
                    wrapped_stream = stream_with_spinner(response_stream, console, message="AI sedang merumuskan jawaban")
                    
                    output_text = ""
                    for chunk in wrapped_stream:
                        console.print(chunk, end="")
                        output_text += chunk
                    console.print("\n")
                    
                    # Save token usage
                    db = SessionLocal()
                    try:
                        in_tokens = len(text) // 4
                        out_tokens = len(output_text) // 4
                        tu = TokenUsage(
                            id=str(uuid.uuid4()),
                            model=settings.default_model,
                            input_tokens=in_tokens,
                            output_tokens=out_tokens,
                            command="/chat"
                        )
                        ws = db.query(Workspace).first()
                        ws_id = ws.id if ws else "default_workspace"
                        
                        rev = Review(
                            id=str(uuid.uuid4()),
                            workspace_id=ws_id,
                            command="/chat",
                            summary=output_text[:500]
                        )
                        db.add(tu)
                        db.add(rev)
                        db.commit()
                    except Exception as e:
                        db.rollback()
                        console.print(f"[red]Gagal menyimpan aktivitas chat:[/] {e}")
                    finally:
                        db.close()
                except Exception as e:
                    console.print(f"[red]Error AI:[/] {e}")
                
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
            
    console.print("[cyan]Terima kasih telah menggunakan SAKIPRO![/]")
    sys.exit(0)
