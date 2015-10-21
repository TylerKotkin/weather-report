import requests
import os

my_secret_key = os.environ['WUNDER_KEY']


class Current:
    def __init__(self, q_string):
        self.q_string = q_string

    def run(self):
        url = 'http://api.wunderground.com/api/{}/conditions/q/{}.json'.format(my_secret_key, self.q_string)

        res = requests.get(url).json()

        temp = res['current_observation']['temp_f']
        conditions = res['current_observation']['weather']

        return "\nCurrent Temp: {}. Current Conditions: {}\n".format(temp, conditions)


class TenDay:
    def __init__(self, q_string):
        self.q_string = q_string

    def run(self):
        url = 'http://api.wunderground.com/api/{}/forecast10day/q/{}.json'.format(my_secret_key, self.q_string)

        res = requests.get(url).json()

        for n in range(20):

            tenday_period = res['forecast']['txt_forecast']['forecastday'][n]['title']
            tenday_forecast = res['forecast']['txt_forecast']['forecastday'][n]['fcttext']
            print("\n{}: {}\n".format(tenday_period, tenday_forecast))


class Astronomy:
    def __init__(self, q_string):
        self.q_string = q_string

    def run(self):
        url = 'http://api.wunderground.com/api/{}/astronomy/q/{}.json'.format(my_secret_key, self.q_string)

        res = requests.get(url).json()

        sunriseh = res['moon_phase']['sunrise']['hour']
        sunrisem = res['moon_phase']['sunrise']['minute']
        sunseth = res['moon_phase']['sunset']['hour']
        sunsetm = res['moon_phase']['sunset']['minute']
        return "\nSunrise: {}:{}. Sunset {}:{}\n".format(sunriseh, sunrisem, sunseth, sunsetm)


class Alerts:
    def __init__(self, q_string):
        self.q_string = q_string

    def run(self):
        url = 'http://api.wunderground.com/api/{}/alerts/q/{}.json'.format(my_secret_key, self.q_string)

        res = requests.get(url).json()

        if not res['alerts']:
            alert = 'None'
            print("Weather Alerts: {}".format(alert))
        else:
            for alert in res['alerts']:
                alert = res['alerts'][0]['message']
                print("\nWeather Alerts: {}\n".format(alert))


class Hurricane:
    def run():
        url = 'http://api.wunderground.com/api/{}/currenthurricane/view.json'.format(my_secret_key)

        res = requests.get(url).json()

        if not res['currenthurricane']:
            hurricanes = 'None'
            print(hurricanes)
        else:
            for hurricane in res['currenthurricane']:
                hurricanes = hurricane['stormInfo']['stormName']
                print(hurricanes)
