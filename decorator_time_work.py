from time import time


def decorator_time_work(func):
    """
    Декоратор для опредления времени работы функции
    """
    def wrapper(*args, **kwargs):
        start = time()

        func(*args, **kwargs)

        stop = time()
        all_time = round(stop - start, 2)

        hour = int(all_time / 60 // 60)
        minutes = int(all_time // 60 - 60 * hour)
        seconds = int(round(all_time - (hour * 60 * 60 + minutes * 60), 0))

        hour = hour if hour > 9 else f"0{hour}"
        minutes = minutes if minutes > 9 else f"0{minutes}"
        seconds = seconds if seconds > 9 else f"0{seconds}"

        print(f"Выполнено за {hour}:{minutes}:{seconds}")

    return wrapper


# Пример использования декоратора
@decorator_time_work
def main():
    a = [e for e in range(10000000)]
    a = a[15]
    b = a * 111
    print(f"{a} * 111 = {b}")

# Вывод:
# 15 * 111 = 1665
# Выполнено за 00:00:01


if __name__ == '__main__':
    main()
