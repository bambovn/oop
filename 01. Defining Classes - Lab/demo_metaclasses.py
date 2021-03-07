# class PersonClass(type):
#     pass
#
#
# class Person(metaclass=PersonClass):
#     pass
#
#
# p = Person()
# print(type(p))
# print(type(Person))

class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
            return super().__call__()
        return cls.__instances[cls]


class PersonFactory(metaclass=Singleton):
    pass


p = PersonFactory()
print(PersonFactory() == PersonFactory())
