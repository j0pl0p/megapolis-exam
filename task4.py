import random


def make_login(name):
    """
    Создаёт логин
    :param name: имя пользователя
    :return: логин
    """
    return f'{name.split(" ")[0]}_{name.split(" ")[1][0]}{name.split(" ")[2][0]}'  # создаём логин с инициалами


def make_password():
    """
    Создаёт пароль
    :return: пароль
    """
    password = ''
    for i in range(10):
        password += random.choice(
            'abcdefghijklmnopqrstuvwxyz0123456789' + 'abcdefghijklmnopqrstuvwxyz'.upper())  # 10 раз берем рандомный символ из алфавита или цифр
    return password


f = open('data/scientist.txt', encoding='utf-8')  # открываем файл
plainData = f.readlines()  # считываем данные
headers, data = plainData[0].strip().split('#'), list(
    map(lambda x: x.strip().split('#'), plainData[1:]))  # обрабатываем в список

fNew = open('data/scientist_password.csv', 'w', encoding='utf-8')  # создаём новый файл
fNew.write('ScientistName,preparation,date,components,login,password' + '\n')  # записываем заголовки
for i in range(len(data)):  # проходимся по данным и создаём логины и пароли
    d = data[i]
    login = make_login(d[0])
    password = make_password()
    if i != len(data) - 1:  # если запись не последняя, добавляем \n
        fNew.write(f"{','.join(d)},{login},{password}\n")  # записываем данные
    else:
        fNew.write(f"{','.join(d)},{login},{password}")
fNew.close()  # закрываем файл
