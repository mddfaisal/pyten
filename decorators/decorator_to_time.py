import time


def timer(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        f = func(*args, **kwargs)
        t2 = time.time()
        print('Runtime took {0} seconds'.format(t2 - t1))
        return f


@time
def example_function():
    # do stuff
    pass


example_function()