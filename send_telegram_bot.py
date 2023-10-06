from os import environ
from json import loads

from requests import post
from dotenv import load_dotenv


def send_telegram(text: str) -> bool | None:
    """
    Отправка заявки через телеграмм бота
    :param text: Текст отправления
    :type text: str
    :return: True - отправилось | False - не отправилось | None
    :rtype bool | None
    """

    # Загрузка переменных из виртуального окружения
    load_dotenv()

    # Получение переменных из виртуального окружения
    USER_ID_TELEGRAM = environ.get('USER_ID_TELEGRAM')
    TOKEN_TELEGRAM_BOT = environ.get('TOKEN_TELEGRAM_BOT')

    url = f'https://api.telegram.org/bot{TOKEN_TELEGRAM_BOT}/sendMessage'

    headers = {
        'Content-Type': 'application/json'
    }

    params = {
        'chat_id': USER_ID_TELEGRAM,
        'text': text
    }

    response = post(url, headers=headers, params=params)
    result = loads(response.text)

    return result.get('ok')
