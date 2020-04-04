import sys
from urllib.error import HTTPError

def catch_404(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except HTTPError as e:
            if e.code == 404:
                print(f"Couldn't find definition for word {args[1]}.")
                sys.exit()
            raise e
    return wrapper

def get_attr_or_empty(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AttributeError:
            return "Not found"
    return wrapper
