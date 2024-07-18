"""
Генерация данных для тестирования
Цель: Применить на практике методы работы с данными

1. Скачать файл data.csv из материалов занятия
2. Загрузить данные из файла
3. Сгенерировать
4. Получить набор из 100 уникальных строк, заполненных данными полностью как файл в приложении результаты.txt
5. Сохранить полученный файл

Ваша задача в домашнем задании - взять конечный набор фио и других столбцов из таблицы и составить из них набор
попарно неэквивалентных строк, в каждой из которых есть все параметры пользователя - фио, город, кредитная карта, вклад, ипотека.
То есть перемешиваете все имеющиеся значения и сохраняете в строки.
Разделитель в csv - запятая, чтобы прочитать можно было удобно.

Критерии оценки: Генерация данных должны быть с помощью generation expression

"""

import pandas as pd
import random

def generate_data():
    # Определение пути к файлам
    base_dir = r'C:\Users\olesia\olya\[OTUS] Python QA Engineer (2019)\4. Data Driven Testing\Материалы'
    data_file = base_dir + r'\data.csv'
    result_file = base_dir + r'\результаты.txt'

    # Загрузка данных из файла data.csv с указанием кодировки UTF-8
    data = pd.read_csv(data_file, encoding='utf-8')

    # Получение всех уникальных значений по каждому столбцу
    names = data['ФИО'].unique()
    cities = data['Город'].unique()
    credit_cards = data['Кредитная карта'].unique()
    deposits = data['Вклад'].unique()
    mortgages = data['Ипотека'].unique()

    # Генерация 100 уникальных строк
    generated_data = set()
    while len(generated_data) < 100:
        name = random.choice(names)
        city = random.choice(cities)
        credit_card = random.choice(credit_cards)
        deposit = random.choice(deposits)
        mortgage = random.choice(mortgages)

        generated_data.add((name, city, credit_card, deposit, mortgage))

    # Преобразование в DataFrame
    generated_df = pd.DataFrame(list(generated_data), columns=['ФИО', 'Город', 'Кредитная карта', 'Вклад', 'Ипотека'])

    # Сохранение в файл результаты.txt
    generated_df.to_csv(result_file, sep=',', index=False)
    return result_file

def test_generate_data():
    result_file = generate_data()
    # Проверка, что файл существует и не пустой
    with open(result_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content, "Файл с результатами был создан, но пуст"