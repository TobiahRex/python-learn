import functools
import time

def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

def sayHi(name):
    print(f"Hi {name}")

def decorator(func):
    functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper_decorator


def timer(func):
    functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        """Print total run time of decorated function"""
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return result
    return wrapper_timer


