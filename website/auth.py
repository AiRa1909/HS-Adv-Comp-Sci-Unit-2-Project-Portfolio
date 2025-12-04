from flask import Blueprint, render_template, flash
from website.stuff import read_temperature

auth = Blueprint('auth', __name__)

@auth.route("/")
def temperature():
    c = float(read_temperature())
    if 25 < c and 28 > c:
        flash("WARNING! Heatwave Temperatures Reached")
    elif c > 40:
        flash("WARNING! Highest Heatwave Temperatures Reached!")
    else:
        pass

    f = c * 9 / 5 + 32

    return render_template("base.html", c=c, f=f)

