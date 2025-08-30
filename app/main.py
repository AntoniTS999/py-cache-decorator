from typing import Callable


def cache(func: Callable) -> Callable:
    result_store = {}

    def wrapper(*args, **kwargs) -> None:
        if args not in result_store:
            result_store[args] = func(*args, **kwargs)
            res = result_store[args]
            print("Calculating new result")
            return res
        print("Getting from cache")
        return result_store[args]
    return wrapper
