from email.mime.text import MIMEText
from smtplib import SMTP
from typing import List, Union

from config import PASSWORD, LOGIN, HOST, PORT, RECIPIENT


def send_mail(sender: str, password: str,
              recipient: Union[str, List[str]],
              host: str, port: int,
              subject: str = 'Subject', message: str = 'Message') -> bool:
    """
    Отправка сообщения по электронной почте

    :param sender: Отправитель адрес электронной почты
    :type sender: str
    :param password: Пароль от электронной почты отправителя
    :type password: str
    :param recipient: олучатель, если несколько получателей то List[str]
    :type recipient:str
    :param subject: Тема
    :type subject:str
    :param message: Сообщение
    :type message:str
    :param host: Хост
    :type host: str
    :param port: Порт
    :type port: int
    :return: True - отправилось, False - не отправилось
    :rtype bool
    """

    server = SMTP(host, port)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = subject

        server.sendmail(sender, recipient, msg.as_string())
        return True

    except Exception:
        return False


def main():
    subject = "TEST"
    message = "TEST"
    send_mail(
        sender=LOGIN,
        password=PASSWORD,
        recipient=RECIPIENT,
        port=PORT,
        host=HOST,
        subject=subject,
        message=message
    )


if __name__ == "__main__":
    main()
