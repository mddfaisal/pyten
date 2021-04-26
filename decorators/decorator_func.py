def super_secret_func(f):
    return f


def disabled(f):
    """
    This function returns nothing, and hence removes the decorated function from the local scope.
    """
    pass


def print_args(func):
    def inner_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
    return inner_func


@super_secret_func
def my_func():
    print("This is my secret function.")


@disabled
def my_func():
    print("This function can no longer be called...")


@print_args
def multiply(a, b):
    return a*b


print(multiply(3,5))
my_func()