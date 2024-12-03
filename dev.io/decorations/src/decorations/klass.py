import functools
import time


class cacher:
    """helper function to return cached response within certain period"""

    def __init__(self, timeout):
        self.timeout = timeout
        self.cache = {}

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.monotonic()
            if "last_called" in self.cache:
                elapsed_time = current_time - self.cache["last_called"]
                if elapsed_time < self.timeout:
                    return self.cache["result"]
            result = func(*args, **kwargs)
            self.cache["last_called"] = current_time
            self.cache["result"] = result

            return result

        return wrapper
