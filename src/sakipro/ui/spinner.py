import time
import threading
from typing import Generator
from rich.console import Console

def stream_with_spinner(response_stream: Generator[str, None, None], console: Console, message: str = "AI sedang berpikir") -> Generator[str, None, None]:
    """
    Wraps the LLM response stream with an animated status spinner and a timer.
    The spinner runs until the first chunk is yielded, then it disappears.
    """
    start_time = time.time()
    stop_event = threading.Event()

    def update_status_text(status_obj):
        while not stop_event.is_set():
            elapsed = int(time.time() - start_time)
            mins, secs = divmod(elapsed, 60)
            # Prevent calling update if stop_event is set to avoid glitch after context manager exits
            if not stop_event.is_set():
                status_obj.update(f"[bold cyan]⚡ {message}... [{mins:02d}:{secs:02d}][/bold cyan]")
            time.sleep(0.5)  # Update frequently to respond quickly to stop_event

    with console.status(f"[bold cyan]⚡ {message}... [00:00][/bold cyan]", spinner="dots") as status:
        timer_thread = threading.Thread(target=update_status_text, args=(status,), daemon=True)
        timer_thread.start()
        
        try:
            # Blocks here until the LLM yields the first token
            first_chunk = next(response_stream)
        except StopIteration:
            stop_event.set()
            return
        except Exception as e:
            stop_event.set()
            yield f"\n[bold red]Error:[/] {str(e)}\n"
            return
            
        # Stop the timer thread before exiting the context manager
        stop_event.set()
        # timer_thread.join(timeout=1.0) # Not strictly necessary for a daemon thread, and speeds up the render
        
    # Spinner is now gone, yield the stream
    yield first_chunk
    
    for chunk in response_stream:
        yield chunk
