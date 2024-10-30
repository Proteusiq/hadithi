import functools
import time


def cacher(timeout: int):
    """helper function to return cached response within certain period"""

    cache = {}

    def outer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.monotonic()
            if "last_called" in cache:
                elapsed_time = current_time - cache["last_called"]
                if elapsed_time < timeout:
                    return cache["result"]
            result = func(*args, **kwargs)
            cache["last_called"] = current_time
            cache["result"] = result

            return result

        return wrapper

    return outer
