def decoratorfactory(msg):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            print('The decorator wants to tell you: {}'.format(msg))
            return func(*args, **kwargs)
        return wrapped_func
    return decorator


@decoratorfactory('Hello World')
def test():
    pass


test()