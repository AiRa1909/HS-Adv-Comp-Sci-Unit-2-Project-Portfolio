from meteostat import Point, Hourly
from datetime import datetime


def read_temperature():
    place = Point(52.9389, -1.1981)

    now = datetime.now()
    data = Hourly(place, now, now).fetch()

    temp_list = list(data['temp'])
    temp_c = float(temp_list[0])

    with open("sensor.txt", "w") as f:
        f.write(f"t={int(temp_c * 1000)}\n")

    with open("sensor.txt", "r") as f:
        databack = f.readline().strip().split("=")[1]

    c = float(databack) / 1000
    f = c * 9 / 5 + 32

    return c,f