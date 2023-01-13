import random

from PIL import Image, ImageDraw, ImageFont
import app



def createImg():
    count = random.randrange(1, 4)
    img = Image.open(f'backgroud/{count}.jpg')

    print(count, ' - count')

    pixels = img.getdata()
    brightness_multiplier = 0.5
    new_image_list = []

    for pixel in pixels:
        new_pixel = (int(pixel[0] * brightness_multiplier),
                     int(pixel[1] * brightness_multiplier),
                     int(pixel[2] * brightness_multiplier))

        # check the new pixel values are within rgb range
        for pixel in new_pixel:
            if pixel > 255:
                pixel = 255
            elif pixel < 0:
                pixel = 0
        new_image_list.append(new_pixel)

    img.putdata(new_image_list)


    # font15 = ImageFont.truetype('/Library/Fonts/Arial Unicode.ttf', size=15, layout_engine=ImageFont.LAYOUT_BASIC)
    # font25 = ImageFont.truetype('/Library/Fonts/Arial Unicode.ttf', size=25, layout_engine=ImageFont.LAYOUT_BASIC)
    # font40 = ImageFont.truetype('/Library/Fonts/Arial Unicode.ttf', size=40, layout_engine=ImageFont.LAYOUT_BASIC)
    # font60 = ImageFont.truetype('/Library/Fonts/Arial Unicode.ttf', size=60, layout_engine=ImageFont.LAYOUT_BASIC)

    font15 = ImageFont.truetype('caviar-dreams.ttf', size=15, layout_engine=ImageFont.LAYOUT_BASIC)
    font25 = ImageFont.truetype('caviar-dreams.ttf', size=25, layout_engine=ImageFont.LAYOUT_BASIC)
    font40 = ImageFont.truetype('caviar-dreams.ttf', size=40, layout_engine=ImageFont.LAYOUT_BASIC)
    font60 = ImageFont.truetype('caviar-dreams.ttf', size=60, layout_engine=ImageFont.LAYOUT_BASIC)

    draw_text = ImageDraw.Draw(img)


    def addIconWeather(weather, x ,y):
        watermark = Image.open(f'icons128/{weather}.png').convert("RGBA")
        img.paste(watermark, (x, y), watermark)

    def addText(text, x, y, fnt):
        draw_text.text(
            (x, y),
            f'{text}',
            font=fnt,
            fill=(255, 255, 255)
        )


    # Добавление названия города
    addText(f'Погода {app.city}', 310, 40, font60)

    # Добавление нынешней даты
    addText(f'{app.date} {app.mounth}', 410, 120, font40)

    # Добавление источника информации
    addText('Данные предоставлены https://yandex.ru/pogoda', 360, 1045, font15)

    # Добавление ифнормации о группе
    addText('vk.com/city_bratsk', 350, 960, font40)

    # Добавляем иконки отображения состояния погода
    addIconWeather(app.weather_morning, 800, 200)
    addIconWeather(app.weather_day, 800, 400)
    addIconWeather(app.weather_evening, 800, 600)
    addIconWeather(app.weather_night, 800, 800)

    # Добавляем текст отображающий время дня
    addText(app.time_of_days[0], 100, 230, font60)
    addText(app.time_of_days[1], 100, 430, font60)
    addText(app.time_of_days[2], 100, 630, font60)
    addText(app.time_of_days[3], 100, 830, font60)

    # Добавляем текст отображающий состояние погоды
    addText(app.weather_morning, 100, 305, font25)
    addText(app.weather_day, 100, 505, font25)
    addText(app.weather_evening, 100, 705, font25)
    addText(app.weather_night, 100, 905, font25)

    # Температура утром
    if len(app.temp_morning) == 2:
        addText(app.temp_morning[0], 500, 230, font60)
    else:
        addText(app.temp_morning[0], 500, 230, font60)
        addText(f'    {app.temp_morning[1]}', 555, 230, font60)

    # Температура днем
    if len(app.temp_day) == 2:
        addText(app.temp_day[0], 500, 430, font60)
    else:
        addText(app.temp_day[0], 500, 430, font60)
        addText(f'    {app.temp_day[1]}', 555, 430, font60)

    # Температура вечером
    if len(app.temp_evening) == 2:
        addText(app.temp_evening[0], 500, 630, font60)
    else:
        addText(app.temp_evening[0], 500, 630, font60)
        addText(f'    {app.temp_evening[1]}', 555, 630, font60)

    # Температура ночью
    if len(app.temp_night) == 2:
        addText(app.temp_evening[0], 500, 830, font60)
    else:
        addText(app.temp_evening[0], 500, 830, font60)
        addText(f'    {app.temp_evening[1]}', 555, 830, font60)

    img.save('xxx.png')

