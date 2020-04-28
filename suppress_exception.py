import contextlib


class CustomError(BaseException):
    """Raise exception"""
    pass


class CustomError2(BaseException):
    """Raise exception"""
    pass


def do_something(data):
    return data


# usar pass é uma má pratica
try:
    do_something(1)
except CustomError:
    pass

# Usar contextlib inves de pass
with contextlib.suppress(CustomError, CustomError2):
    do_something(1)
