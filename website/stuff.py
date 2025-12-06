import requests

def read_temperature():
    url = "https://api.open-meteo.com/v1/forecast"
    # open access url Open Meteo provides themselves
    params = {
        "latitude": 52.9540,
        "longitude": 1.1550,
        "current_weather": True
    }
    # a dictionary that contains all the parameters we need to give in the HTTP route to open meteo
    r = requests.get(url, params=params)
    # a GET HTTP request to the Open Meteo URL with the parameters
    data = r.json()
    # parse the JSON content of the HTTP response  and convert it into a Python dictionary
    temp_c = str(data["current_weather"]["temperature"])
    #FIND the temperature value-pair that contains the celsius temperature IN the python dictionary "current_weather"

    try:
        with open("sensor.txt", "w") as f:
            f.write(temp_c)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    #displays correct use of the try-except block to except any errors
    #writes to file

    with open("sensor.txt", "r") as f:
        celsius = f.read()
        return celsius
    #reads from file
