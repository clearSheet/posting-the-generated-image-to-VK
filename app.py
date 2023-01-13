import requests as requests
from bs4 import BeautifulSoup
from datetime import datetime
url = 'https://yandex.ru/pogoda/bratsk/details?via=ms#15'

request = requests.get(url)
bs = BeautifulSoup(request.text, 'html.parser')
nowDate = datetime.now().day  # Создаем переменную в которой находится ныняшняя дата для проверки


# Создаем массив описания погоды
# 0 - утро | 1 - день | 2 - вечер | 3 - ночь

date = bs.find('strong', class_='forecast-details__day-number').text
mounth = bs.find('span', class_='forecast-details__day-month').text

city = bs.find('h1', class_='title title_level_1 header-title__title').text
city = str(city[20:])


# Проверка на сегодяшний блок
if str(date) == str(date):

    # Создаем массив описания погоды
    # 0 - утро | 1 - день | 2 - вечер | 3 - ночь
    condition = []
    for status in bs.find_all('td', class_='weather-table__body-cell weather-table__body-cell_type_condition'):
        condition.append(status.text)

    # Находи все строки и помещаем их тела в массив
    rows = []
    for row in bs.find_all('tr', class_='weather-table__row'):
        rows.append(row)

    # Находим все времена дня и помещаем их в массив
    time_of_days = []
    for time_of_day in bs.find_all('div', class_='weather-table__daypart'):
        time_of_days.append(time_of_day.text.capitalize())

    # Находим диапазан температур утром
    # В массиве будет от одно(1) до двух(2) элментов
    # Последний элемент массива отображает "как ощущается"
    temp_morning = []
    for temp in rows[0].find_all('span', class_='temp__value temp__value_with-unit'):
        temp_morning.append(f"{temp.text}°")

    # Находим диапазан температур днем
    temp_day = []
    for temp in rows[1].find_all('span', class_='temp__value temp__value_with-unit'):
        temp_day.append(temp.text)

    # Находим диапазан температур вечером
    temp_evening = []
    for temp in rows[2].find_all('span', class_='temp__value temp__value_with-unit'):
        temp_evening.append(temp.text)

    # Находим диапазан температур вечером
    temp_night = []
    for temp in rows[3].find_all('span', class_='temp__value temp__value_with-unit'):
        temp_night.append(temp.text)

    # Находим состояние погоды утром
    weather_morning = []
    for weath in rows[0].find_all('td', class_='weather-table__body-cell weather-table__body-cell_type_condition'):
        weather_morning.append(weath.text)
        weather_morning = weather_morning[0]

    # Находим состояние погоды днем
    weather_day = []
    for weath in rows[1].find_all('td', class_='weather-table__body-cell weather-table__body-cell_type_condition'):
        weather_day.append(weath.text)
        weather_day = weather_day[0]

    # Находим состояние погоды вечером
    weather_evening = []
    for weath in rows[2].find_all('td', class_='weather-table__body-cell weather-table__body-cell_type_condition'):
        weather_evening.append(weath.text)
        weather_evening = weather_evening[0]

    # Находим состояние погоды вечером
    weather_night = []
    for weath in rows[3].find_all('td', class_='weather-table__body-cell weather-table__body-cell_type_condition'):
        weather_night.append(weath.text)
        weather_night = weather_night[0]

        
#
x = 9
# x = int(input('Введите значение от 0 до 3: '))
if x == 0:
    print(time_of_days[0], temp_morning, weather_morning)
elif x == 1:
    print(time_of_days[1], temp_day, weather_day)
elif x == 2:
    print(time_of_days[2], temp_evening, weather_evening)
elif x == 3:
    print(time_of_days[3], temp_night, weather_night)
