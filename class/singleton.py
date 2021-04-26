class Singleton:
    def __new__(cls):
        try:
            it = cls.__it__
        except AttributeError:
            it = cls.__it__ = object.__new__(cls)
        return it

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__.upper())

    def __eq__(self, other):
        return other is self

    def Instance(self):
        print("Printin instance.")


s = Singleton()
s.Instance()

s2 = Singleton()
s2.Instance()