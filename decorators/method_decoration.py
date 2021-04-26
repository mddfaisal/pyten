from types import MethodType


class Decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Inside the decorator.")

    def __get__(self, instance, owner):
        # Return a method if it is called on an instance
        return self if instance is None else MethodType(self, instance)


class Test(object):
    @Decorator
    def __init__(self):
        pass


a = Test()