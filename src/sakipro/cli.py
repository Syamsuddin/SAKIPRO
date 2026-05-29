import typer
from typing import Optional
from sakipro.ui.console import console

app = typer.Typer(
    name="sakipro",
    help="AI CLI Assistant for OPD SAKIP Planning Documents",
    add_completion=False,
)

@app.command()
def wizard():
    """Start SAKIPRO in Wizard mode for beginners."""
    from sakipro.ui.console import print_banner
    print_banner()
    console.print("[cyan]Memulai mode Wizard... (To Be Implemented)[/]")

@app.command()
def status():
    """Show current workspace status."""
    from sakipro.core.config import settings
    from sakipro.ui.console import print_startup_panel
    print_startup_panel(
        project="DISDIK_2026",
        doc_count=9,
        model=settings.default_model,
        privacy=settings.privacy_mode,
        token_percent=41
    )

@app.command()
def scan(folder: str = typer.Argument(".", help="Folder to scan")):
    """Scan directory for SAKIP documents."""
    console.print(f"[yellow]⠸ Memindai folder:[/] {folder}")
    try:
        from sakipro.documents.scanner import scan_directory
        count = scan_directory(folder)
        console.print(f"[green]✓ Selesai:[/] {count} file berhasil diproses dan disimpan ke database.")
    except Exception as e:
        console.print(f"[red]Error saat memindai folder:[/] {e}")

if __name__ == "__main__":
    app()
