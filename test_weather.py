import os
import requests_mock
from weather_report_data import Current, TenDay, Astronomy, Alerts, Hurricane

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

    with open('weather_data/sun.json') as sun:
        m.get(url, text=sun.read())

    astronomy = Astronomy('28409')
    res = astronomy.run()

    assert res['sunriseh'] == "7"
    assert res['sunrisem'] == "20"
    assert res['sunseth'] == "18"
    assert res['sunsetm'] == "31"


@requests_mock.Mocker()
def test_alerts(m):
    url = 'http://api.wunderground.com/api/{}/alerts/q/28409.json'.format(my_secret_key)

    with open('weather_data/alerts.json') as alt:
        m.get(url, text=alt.read())

    alerts = Alerts('28409')
    res = alerts.run()

    assert res['alert'] == "\u000A...Heat advisory remains in effect until 7 am CDT Saturday...\u000A\u000A* temperature...heat indices of 100 to 105 are expected each \u000A afternoon...as Max temperatures climb into the mid to upper \u000A 90s...combined with dewpoints in the mid 60s to around 70. \u000A Heat indices will remain in the 75 to 80 degree range at \u000A night. \u000A\u000A* Impacts...the hot and humid weather will lead to an increased \u000A risk of heat related stress and illnesses. \u000A\u000APrecautionary/preparedness actions...\u000A\u000AA heat advisory means that a period of hot temperatures is\u000Aexpected. The combination of hot temperatures and high humidity\u000Awill combine to create a situation in which heat illnesses are\u000Apossible. Drink plenty of fluids...stay in an air-conditioned\u000Aroom...stay out of the sun...and check up on relatives...pets...\u000Aneighbors...and livestock.\u000A\u000ATake extra precautions if you work or spend time outside. Know\u000Athe signs and symptoms of heat exhaustion and heat stroke. Anyone\u000Aovercome by heat should be moved to a cool and shaded location.\u000AHeat stroke is an emergency...call 9 1 1.\u000A\u000A\u000A\u000AMjb\u000A\u000A\u000A"


@requests_mock.Mocker()
def test_hurricane(m):
    fullurl = 'http://api.wunderground.com/api/{}/currenthurricane/view.json'.format(my_secret_key)

    with open('weather_data/hurricane.json') as data:
        m.get(fullurl, text=data.read())

    hurricane = Hurricane()
    res = hurricane.run()

    assert res[0] == 'Hurricane Olaf'
