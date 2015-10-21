import os
import requests_mock
from weather_report_data import Current, TenDay, Astronomy

my_secret_key = os.environ['WUNDER_KEY']


@requests_mock.Mocker()
def test_current(m):
    url = 'http://api.wunderground.com/api/{}/conditions/q/28409.json'.format(my_secret_key)

    with open('weather_data/current.json') as current:
        m.get(url, text=current.read())

    conditions = Current('28409')
    res = conditions.run()

    assert res['temp'] == 58.0
    assert res['conditions'] == "Clear"


@requests_mock.Mocker()
def test_ten(m):
    url = 'http://api.wunderground.com/api/{}/forecast10day/q/28409.json'.format(my_secret_key)

    with open('weather_data/tenday.json') as ten:
        m.get(url, text=ten.read())

    ten = TenDay('28409')
    res = ten.run()

    assert res['period1'] == "Tuesday"
    assert res['period1_forecast'] == "A few clouds. Lows overnight in the low 50s."
    assert res['period2'] == "Tuesday Night"
    assert res['period2_forecast'] == "Mostly clear. Low 53F. Winds light and variable."


@requests_mock.Mocker()
def test_astronomy(m):
    url = 'http://api.wunderground.com/api/{}/astronomy/q/28409.json'.format(my_secret_key)

    with open('weather_data/sun.json') as data:
        m.get(url, text=data.read())

    astronomy = Astronomy('28409')
    res = astronomy.run()

    assert res['sunriseh'] == "7"
    assert res['sunrisem'] == "20"
    assert res['sunseth'] == "18"
    assert res['sunsetm'] == "31"
