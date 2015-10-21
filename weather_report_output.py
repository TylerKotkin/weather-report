from weather_report_data import Current, TenDay, Astronomy, Alerts, Hurricane


def zipcode():
    zipcode = input('Want a weather report?\n Enter a 5 digit zipcode: ')
    return weather_report(zipcode)


def weather_report(zipcode):
    while True:
        x = input('''\nEnter 1 for current weather conditions.
            Enter 2 for the ten-day forecast.
            Enter 3 for sunrise and sunset times.
            Enter 4 for weather alerts.
            Enter 5 for a list of named tropical storms.
            Enter exit to exit.-''')
        if x == '1':
            print(Current(zipcode).run())
        elif x == '2':
            print(TenDay(zipcode).run())
        elif x == '3':
            print(Astronomy(zipcode).run())
        elif x == '4':
            print(Alerts(zipcode).run())
        elif x == '5':
            print(Hurricane.run())
        else:
            exit()


if __name__ == '__main__':
    zipcode()
