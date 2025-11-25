from flask import Blueprint, render_template, flash

from main import read_temperature

auth = Blueprint('auth', __name__)

@app.route("/temperature")
def temperature():
    c, f = read_temperature()
    if c > 75:
        flash("TOO HOTT!!!")
    else:
        pass

    return render_template("page.html",c=c,f=f)