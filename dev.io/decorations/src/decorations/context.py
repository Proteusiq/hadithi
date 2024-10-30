import contextlib
import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.monotonic()
        results = func(*args, **kwargs)

        print(
            f"Function: {func.__name__!r} - Execution Time: {time.monotonic() - start_time : .2f}s"
            f"- Results: {results!r}"
        )

        return results

    return wrapper


@contextlib.contextmanager
def timers(name: str):
    start_time = time.monotonic()

    try:
        yield

    finally:
        print(
            f"Function: {name!r} - Execution Time: {time.monotonic() - start_time : .2f}s"
        )
