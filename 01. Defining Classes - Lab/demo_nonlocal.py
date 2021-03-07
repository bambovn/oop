def get_my_print():
    count = 0

    def my_print(x):
        nonlocal count
        count += 1
        print(f'My: ({count}): {x}')

    return my_print


my_print = get_my_print()
my_print('1')
my_print('Pesho')
my_print('Apples')