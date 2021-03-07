x = 'global'


def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print("inner:", x)

    def change_global():
        global x
        x = 'global: changed!'

    print('outher:', x)
    inner()
    print("outher:", x)
    change_global()


print(x)
outer()
print(x)
