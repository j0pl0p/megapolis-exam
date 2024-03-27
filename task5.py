import random


def make_hash(name):
    """
    Создаёт хэш по имени
    :param name: имя пользователя
    :return: хэш
    """
    table = list(range(1024))  # создаём таблицу перестановок
    random.shuffle(table)  # перемешиваем
    total_hashes = 0  # сумма хэшей
    for symbol in name:  # проходимся по сиволам и складываем их хэши
        index = ord(symbol) % 1024
        total_hashes += table[index]
    return total_hashes % 2048


f = open('data/scientist.txt', encoding='utf-8')  # открываем файл
plainData = f.readlines()  # считываем данные
headers, data = plainData[0].strip().split('#'), list(
    map(lambda x: x.strip().split('#'), plainData[1:]))  # обрабатываем в список

fNew = open('data/scientist_with_hash.csv', 'w', encoding='utf-8')  # создаём новый файл
fNew.write('hash,ScientistName,preparation,date,components' + '\n')  # записываем заголовки
for i in range(len(data)):  # проходимся по данным и создаём логины и пароли
    d = data[i]
    hash = make_hash(d[0])
    if i != len(data) - 1:  # если запись не последняя, добавляем \n
        fNew.write(f"{hash},{','.join(d)}\n")  # записываем данные
    else:
        fNew.write(f"{hash},{','.join(d)}")
fNew.close()  # закрываем файл
