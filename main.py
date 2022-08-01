import mod


def print_hi(name: str):
    print('Как тебя зовут?')
    name = input()
    print(f'Привет, {name}!')


def print_hi_user01():
    print('Привет от User01!')


if __name__ == '__main__':
    print('HI')
    print_hi('PyCharm')
    print_hi_user01()
