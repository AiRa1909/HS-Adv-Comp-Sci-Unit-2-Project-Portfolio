from flask import Blueprint, render_template, flash
from website.stuff import read_temperature

auth = Blueprint('auth', __name__)

@auth.route("/temperature", methods=["GET"])
def temperature():
    c = float(read_temperature())
    if c > 75:
        flash("TOO HOTT!!!")
    else:
        pass

    f = c * 9 / 5 + 32

    return render_template("base.html", c=c, f=f)

