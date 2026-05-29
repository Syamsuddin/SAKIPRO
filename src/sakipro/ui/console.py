from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def print_banner():
    """Prints the SAKIPRO startup banner."""
    banner = """
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ███████╗ █████╗ ██╗  ██╗██╗██████╗ ██████╗  ██████╗            ║
║   ██╔════╝██╔══██╗██║ ██╔╝██║██╔══██╗██╔══██╗██╔═══██╗           ║
║   ███████╗███████║█████╔╝ ██║██████╔╝██████╔╝██║   ██║           ║
║   ╚════██║██╔══██║██╔═██╗ ██║██╔═══╝ ██╔══██╗██║   ██║           ║
║   ███████║██║  ██║██║  ██╗██║██║     ██║  ██║╚██████╔╝           ║
║   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝            ║
║                                                                  ║
║   AI CLI Assistant for OPD SAKIP Planning Documents  v1.0.0      ║
║   Review  •  Improve  •  Draft  •  Evidence  •  Report           ║
║   Hak Cipta(c)2026 -syams_ideris •  syamsuddin.ideris@gmail.com  ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
    """
    console.print(Text(banner, style="bold cyan"))

def print_startup_panel(project: str, doc_count: int, model: str, privacy: str, token_percent: int):
    """Prints the workspace status panel."""
    status_text = f"""
  Project      : {project}
  Folder       : ./Dokumen_SAKIP_DisDik   ({doc_count} dokumen indexed)
  Model        : {model}  [API Key Ready]
  Privacy      : {privacy}
  Token Bulan  : 412.900 / 1.000.000  [{"▓" * (token_percent//10)}{"░" * (10 - token_percent//10)}]  {token_percent}%
  Status       : ✓ Siap
    """
    panel = Panel(
        status_text,
        title="Workspace",
        border_style="cyan",
        subtitle="Ketik /  untuk perintah    •    Ketik ?  untuk bantuan    •    Ctrl+D untuk keluar"
    )
    console.print(panel)
