class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_oldewr(self):
        self.age += 1

    def __str__(self):
        return f'{self.name}; {self.age}'


pesho = Person('Pesho', 15)
stamo = Person('Stamo', 11)

print(pesho)
print(stamo)

pesho.get_oldewr()

print(pesho)
print(stamo)
