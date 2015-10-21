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

        return {'temp': temp, 'conditions': conditions}


class TenDay:
    def __init__(self, q_string):
        self.q_string = q_string

    def run(self):
        url = 'http://api.wunderground.com/api/{}/forecast10day/q/{}.json'.format(my_secret_key, self.q_string)

        res = requests.get(url).json()

        ret = {}
        for n in range(20):
            period = 'period' + str(n + 1)
            ret[period] = res['forecast']['txt_forecast']['forecastday'][n]['title']
            ret[period + '_forecast'] = res['forecast']['txt_forecast']['forecastday'][n]['fcttext']
        return ret


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
        return {'sunriseh': sunriseh, 'sunrisem': sunrisem, 'sunseth': sunseth, 'sunsetm': sunsetm}
