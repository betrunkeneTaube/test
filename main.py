def print_hi(name):
    print(f'Hi, {name}')


def count20():
    for i in range(21):
        var = lambda a: a ** 3
        i = var(i)
        print(i)


if __name__ == '__main__':
    print_hi('PyCharm')
    count20()
