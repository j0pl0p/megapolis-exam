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


data.sort(key=lambda x: date_to_seconds(x[2]))  # сортируем данные по дате в секундах

fNew = open('data/scientist_origin.txt', 'w', encoding='utf-8')  # создаём новый файл

scientists = []
for name, prep, date, comps in data:  # проходимся по данным и ищем ученых, которые разрабатывают Аллопуринол, записываем в отдельный список
    if prep == 'Аллопуринол':
        scientists.append((name, date))

print('Разработчиками Аллопуринола были такие люди:', file=fNew)  # выводим результат
for name, date in scientists:
    print(f'{name} - {date}', file=fNew)
print(f'Оригинальный рецепт принадлежит: {scientists[0][0]}', file=fNew)
fNew.close()  # закрываем файл
