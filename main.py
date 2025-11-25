from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

def read_temperature():
    path = #i will write path here later i dont know what folder the temperature values will be in right now

    with open(path, "r") as f:
        lines = f.readlines()

    temp_str = lines[1].split("t=")[1]

    c = float(temp_str) / 1000
    f = (c * 9 / 5) + 32

    return c, f