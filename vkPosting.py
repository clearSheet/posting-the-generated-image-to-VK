import secrets

import requests
import vk
import vk_api
import main
main.createImg()


acessToken = '5cf41e7a6f2d19a495e9665030ac1244d5a7ac43b80a085be8332d081ed8af22e422fca26561e2a009270'
group = 207924345
version = 5.122

text =[
    'Доброе утро, братчане⏰ Всем прекрасного дня!\nПрогноз погоды на сегодня 🌤',
    'С добрым утром и хорошего дня, братчане!\n Прогноз погоды на сегодня 🌤',
    'Доброе утро, братчане ✨ Отличного дня и позитивного настроения!\n Прогноз погоды на сегодня 🌤',
    'Доброе утро, друзья! Бодрого дня и хорошего настроения💫\nПрогноз погоды на сегодня 🌤',
    'Доброе утро, Братск!😃 Просыпайтесь! Вас ждет великий день!✌🏻\nПрогноз погоды на сегодня 🌤',
    'Доброе утро, друзья! Лёгкого дня и хорошего настроения!😃\nПрогноз погоды на сегодня 🌤',
    'Доброе утро, братчане! Выспались? Какие на сегодня планы?☺\nПрогноз погоды на сегодня 🌤'
]

VK = vk_api.VkApi(token=acessToken)

session = vk.Session(access_token=acessToken)
apiVk = vk.API(session)

upload_url = apiVk.photos.getWallUploadServer(group_id=group,
                                              v=version,
                                              scope='wall')['upload_url']

request = requests.post(upload_url, files={"file": open('xxx.png', 'rb')})

save_wall_photo = apiVk.photos.saveWallPhoto(group_id=group,
                                             v=version,
                                             photo=request.json()['photo'],
                                             server=request.json()['server'],
                                             hash=request.json()['hash'])

saved_photo = 'photo' + str(save_wall_photo[0]['owner_id']) + "_" + str(save_wall_photo[0]['id']) + "_" + acessToken


apiVk.wall.post(owner_id=-(group),
                v=version,
                attachments=str(saved_photo),
                message=secrets.choice(text)
                )

print('Weather information sent to the group!')




