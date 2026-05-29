import sys
from sakipro.cli import app
from sakipro.ui.console import print_banner, print_startup_panel
from sakipro.ui.repl import start_repl
from sakipro.core.config import settings

from sakipro.storage.database import init_db

def main():
    """
    Main entry point.
    If run with arguments (e.g. `sakipro wizard`), delegates to Typer.
    If run without arguments (`sakipro`), launches interactive REPL.
    """
    # Ensure database is initialized
    init_db()
    
    if len(sys.argv) > 1:
        # User provided a subcommand
        app()
    else:
        # Default Interactive Mode
        print_banner()
        print_startup_panel(
            project="DISDIK_2026",
            doc_count=9,
            model=settings.default_model,
            privacy=settings.privacy_mode,
            token_percent=41
        )
        start_repl()

if __name__ == "__main__":
    main()
