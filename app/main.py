from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash_store = {}

    def wrapper(*args) -> Any:

        if args not in cash_store:
            res = func(*args)
            cash_store[args] = res
            print("Calculating new result")
            return res
        else:
            print("Getting from cache")
            return cash_store[args]
    return wrapper
