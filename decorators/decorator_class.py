class Decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before function call.")
        res = self.func(*args, **kwargs)
        print("After function call.")
        return res


@Decorator
def testfunc():
    print("Inside the function")


testfunc()
