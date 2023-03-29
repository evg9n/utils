from datetime import datetime, time
from time import sleep


def i_am_sleep(stand_up_hour: int = 0, stand_up_minute: int = 0) -> None:
    """
    Пауза до stand_up_hour:stand_up_minute
    :param stand_up_hour: Час
    :param stand_up_minute: Минуты
    :return: None
    """
    try:
        time(hour=stand_up_hour, minute=stand_up_minute)
    except ValueError:
        stand_up_hour = stand_up_minute = 0

    now = datetime.now().now()
    now_hour = now.hour
    now_minute = now.minute

    second_sleep = ((stand_up_hour - now_hour) * 60 + (stand_up_minute - now_minute)) * 60
    second_sleep = second_sleep if second_sleep >= 0 else second_sleep + 86400
    sleep(second_sleep if second_sleep >= 0 else second_sleep + 86400)


if __name__ == "__main__":
    i_am_sleep(11, 47)
