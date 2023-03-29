from requests import get
from bs4 import BeautifulSoup
from json import dumps
from re import sub


class DownloadCBRF:
    """
    Скачиваются все курсы валют на текущий момент с официального сайта ЦБ РФ https://www.cbr.ru/currency_base/daily/
    """

    def __init__(self):
        self.__list_cb_rf = self.__get_cb_rf()
        self.__json_cb_rf = dumps(self.__get_cb_rf(), indent=4, ensure_ascii=False)

    def __str__(self):
        return """
        Скачиваются все курсы валют на текущий момент с официального сайта ЦБ РФ https://www.cbr.ru/currency_base/daily/
        """

    def __repr__(self):
        return """
        Скачиваются все курсы валют на текущий момент с официального сайта ЦБ РФ https://www.cbr.ru/currency_base/daily/
        
        методы:
        get_list_cb_rf - возвращает результат list
        get_json_cb_rf - возвращает результат в формате json
        get_numbers_codes - возвращает numbers_codes
        get_names - возвращает names
        get_alphas_codes - возвращает alphas_codes
        get_eds - возвращает eds
        get_values - возвращает values
        """

    @classmethod
    def __get_cb_rf(cls) -> list:
        """
        Скачиваются все курсы валют на текущий момент с официального сайта ЦБ РФ https://www.cbr.ru/currency_base/daily/
        :rtype list
        """
        cookies = {
            'yandexuid': '3641923381676615575',
            'yuidss': '3641923381676615575',
            'ymex': '1991975575.yrts.1676615575#1991975575.yrtsi.1676615575',
            'is_gdpr': '0',
            'yashr': '4330156041676615578',
            '_ym_uid': '16766446101008094116',
            '_ym_d': '1676644610',
            'yabs-sid': '96892031676895822',
            'gdpr': '0',
            'yandex_login': 'e.evgen999',
            'i': '5Rh6o3lQg0SNbYlxZ3ogFNPD7dl2bW8vO7R5IvsQVZsZ0/wXe090C9ZyU2XyiShcyFwM9YhUX2nWKvOpa/M/5NQSQ58=',
            'is_gdpr_b': 'CNCdfRCgrAEoAg==',
            'yandex_gid': '236',
            'yp': '1994393759.udn.cDplLmV2Z2VuOTk5#1679579123.szm.0_8999999761581421:1320x665:1466x615#1681571997.ygu.'
                  '1#1994347336.pcs.1#1679592136.mcv.0#1679592136.mcl.wewl54#1710523336.p_sw.1678987336',
            'ys': 'udn.cDplLmV2Z2VuOTk5#c_chck.2520867083',
            'skid': '6618438071679576223',
            'Session_id': '3:1679812282.5.0.1678083948984:inL4WQ:36.1.2:1|1513154723.949811.2.2:949811.3:1679033759'
                          '|3:10267479.727955.UkcFBbZgSaaoZTh3VmoFAqMda94',
            'sessionid2': '3:1679812282.5.0.1678083948984:inL4WQ:36.1.2:1|1513154723.949811.2.2:949811.3:1679033759'
                          '|3:10267479.727955.fakesign0000000000000000000',
            'cycada': '5tBxr9BhNmT1q74quvqZpKiuzTSuOt4WtXGtbBNG7dM=',
        }
        headers = {
            'authority': 'mc.yandex.ru',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'origin': 'https://www.cbr.ru',
            'referer': 'https://www.cbr.ru/',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/109.0.0.0 Safari/537.36',
        }
        url = "https://www.cbr.ru/currency_base/daily/"
        result = list()
        response = get(url=url, headers=headers, cookies=cookies)
        if response.status_code != 200:
            return result

        html = response.text
        bs = BeautifulSoup(html, 'lxml')
        list_val = bs.find(name='table', class_='data')

        for val in list_val.find_all(name='tr')[1:]:
            number_code, alpha_code, ed, name, value = val.find_all(name='td')
            number_code = number_code.text
            alpha_code = alpha_code.text
            ed = int(ed.text)
            name = name.text
            value = float(sub(r',', r'.', value.text))

            result.append(dict(
                number_code=number_code,
                alpha_code=alpha_code,
                ed=ed,
                name=name,
                value=value
            ))

        return result

    def get_list_cb_rf(self) -> list:
        return self.__list_cb_rf

    def get_json_cb_rf(self) -> str:
        return self.__json_cb_rf

    def get_numbers_codes(self) -> list:
        return [number.get('number_code') for number in self.__list_cb_rf]

    def get_alphas_codes(self) -> list:
        return [number.get('alpha_code') for number in self.__list_cb_rf]

    def get_eds(self) -> list:
        return [number.get('ed') for number in self.__list_cb_rf]

    def get_names(self) -> list:
        return [number.get('name') for number in self.__list_cb_rf]

    def get_values(self) -> list:
        """
        :return:
        """
        return [number.get('value') for number in self.__list_cb_rf]


def main():
    cb = CBRF()
    print(cb.__doc__)


if __name__ == "__main__":
    main()
