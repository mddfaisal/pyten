from functools import wraps


class Decorator(object):
    def __init__(self, func):
        self._wrapped = wraps(func)(self)

    def __call__(self, *args, **kwargs):
        return self._wrapped(*args, **kwargs)


@Decorator
def test():
    """Docstring of test"""
    pass


test.__doc__
