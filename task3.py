f = open('data/scientist.txt', encoding='utf-8')  # открываем файл
plainData = f.readlines()  # считываем данные
headers, data = plainData[0].strip().split('#'), list(
    map(lambda x: x.strip().split('#'), plainData[1:]))  # обрабатываем в список


def date_to_seconds(s):
    """
    Конвертация даты в секунды
    :param s: дата в формате ГГГГ-ММ-ДД
    :return: приблизительное кол-во секунд с 0000-00-00
    """

    year, month, day = map(int, s.split('-'))
    return 60 * 60 * 24 * 365 * year + 60 * 60 * 24 * 30 * month + 60 * 60 * 24 * day


for d in data:  # оставляем дату - она пригодится при выводе
    d.append(d[2])
    d[2] = date_to_seconds(d[2])
data.sort(key=lambda x: x[2])  # конвертируем дату и сортируем по ней


def binary_searchL(seconds, l=0, r=len(data) - 1):
    """
    Бин поиск самой левой подходящей записи
    :param seconds: секунды
    :param l: левый указалель
    :param r: правый указатель
    :return: нужный индекс
    """
    mid = (l + r) // 2  # алгоритм бинпоиска
    if data[mid][2] > seconds:
        return binary_searchL(seconds, l, mid - 1)
    if data[mid][2] < seconds:
        return binary_searchL(seconds, mid + 1, r)
    if data[mid][2] == seconds and data[mid - 1][2] < seconds:
        return mid
    else:
        return binary_searchL(seconds, l, mid - 1)


def binary_searchR(seconds, l=0, r=len(data) - 1):
    """
        Бин поиск самой правой подходящей записи
        :param seconds: секунды
        :param l: левый указалель
        :param r: правый указатель
        :return: нужный индекс
        """
    mid = (l + r) // 2  # алгоритм бинпоиска
    if data[mid][2] > seconds:
        return binary_searchR(seconds, l, mid - 1)
    if data[mid][2] < seconds:
        return binary_searchR(seconds, mid + 1, r)
    if data[mid][2] == seconds and data[mid + 1][2] > seconds:
        return mid
    else:
        return binary_searchR(seconds, mid + 1, r)


inputDate = input()
while inputDate != 'эксперимент':  # проверка на эксперимент
    inputDate = date_to_seconds(inputDate)  # конвертация в секунды
    try:
        l, r = binary_searchL(inputDate), binary_searchR(inputDate)  # бинпоиск указателей
    except RecursionError:  # таких записей не нашлось
        print('В этот день ученые отдыхали')
        inputDate = input()
        continue
    if data[l][2] != inputDate:  # таких записей не нашлось
        print('В этот день ученые отдыхали')
    else:
        for d in data[l:r + 1]:  # проходим по подходящим учёным и выводим их на экран
            name = d[0].split()
            print(f'Ученый {name[0]} {name[1][0]}.{name[2][0]}. создал препарат: {d[1]} - {d[-1]}')

    inputDate = input()
