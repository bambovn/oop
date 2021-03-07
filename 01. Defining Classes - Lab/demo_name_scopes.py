print(abs(-1))  # global name space

x = 5

print(x)


def print_x():
    print(f'Print {x}')


print(x)
print_x()


def f1():
    def nested_f1():
        nonlocal y
        global x
        # y +=1
        y = 88
        x += 1
        ll.append(3)
        # ll = [3]
        z = 7
        print(f'From nested f1')
        print(x)
        print(y)
        print(z)
        print(abs(-x - y - z))

    global name
    name = 'Pesho'
    return 'Pesho'

    y = 6
    ll = []
    print(f'Before {y}')
    print(ll)
    nested_f1()
    print(ll)
    print(f'After {y}')


f1()
