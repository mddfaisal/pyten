def singleton(cls):
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]
    return wrapper


@singleton
class SomeSingletonClass:
    x = 2

    def __init__(self):
        print("Created")



instance = SomeSingletonClass()
instance = SomeSingletonClass() # doesn't print anything
print(instance.x) # 2
instance.x = 3
print(SomeSingletonClass().x) # 3
