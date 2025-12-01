from website import create_app
from meteostat import Point, Hourly

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)