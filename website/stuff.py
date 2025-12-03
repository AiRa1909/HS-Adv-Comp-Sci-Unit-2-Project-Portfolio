import requests

def read_temperature():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 52.9540,
        "longitude": 1.1550,
        "current_weather": True
    }
    r = requests.get(url, params=params)
    data = r.json()
    temp_c = str(data["current_weather"]["temperature"])

    try:
        with open("sensor.txt", "w") as f:
            f.write(temp_c)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    with open("sensor.txt", "r") as f:
        celsius = f.read()
        return celsius
