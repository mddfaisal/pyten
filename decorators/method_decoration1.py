from types import MethodType


class CountCallsDecorator(object):
    def __init__(self, func):
        self.func = func
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        return self if instance is None else MethodType(self, instance)


class Test(object):
    def __init__(self):
        pass

    @CountCallsDecorator
    def do_something(self):
        return 'something was done'


a = Test()
a.do_something()
a.do_something.ncalls
print(a.do_something.ncalls)

b = Test()
b.do_something()
b.do_something.ncalls
print(b.do_something.ncalls)