import requests


def test_get_all_airports(url: str):
    res = requests.get(url).json()
    assert (res == [{
        'airports_id': 1,
        'name': 'Шереметьево',
        'description': 'Международный аэропорт в Москве.',
        'address': 'Аэропорт "Шереметьево", г. Химки, Московская обл., Россия',
        'country': 'Россия'
    },
        {
            'airports_id': 2,
            'name': 'Дубайский международный аэропорт',
            'description': 'Крупнейший аэропорт в мире по пассажиропотоку.',
            'address': 'Дубай, ОАЭ',
            'country': 'ОАЭ'
        },
        {
            'airports_id': 3,
            'name': 'Лондонский Хитроу',
            'description': 'Один из крупнейших и самых загруженных аэропортов мира.',
            'address': 'Хилтон-роуд, Хайтроу, Лондон, Великобритания',
            'country': 'Великобритания'
        },
        {
            'airports_id': 4,
            'name': 'Пекинский аэропорт имени Капитана Фана Цзыкя',
            'description': 'Один из крупнейших аэропортов в мире.',
            'address': 'Пекин, Китай',
            'country': 'Китай'
        },
        {
            'airports_id': 5,
            'name': 'Делийский аэропорт',
            'description': 'Один из крупнейших и самых загруженных аэропортов Индии.',
            'address': 'Нью-Дели, Индия',
            'country': 'Индия'
        }])


def test_get_airport_by_id(url: str):
    res = requests.get(url).json()
    assert (res == {
        'airports_id': 1,
        'name': 'Шереметьево',
        'description': 'Международный аэропорт в Москве.',
        'address': 'Аэропорт "Шереметьево", г. Химки, Московская обл., Россия',
        'country': 'Россия'
    })


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/airports/'
    test_get_airport_by_id(URL + '1')
    test_get_all_airports(URL)
