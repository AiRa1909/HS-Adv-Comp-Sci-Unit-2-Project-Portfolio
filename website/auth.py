from flask import Blueprint, render_template, flash
from .stuff import read_temperature

auth = Blueprint('auth', __name__)

@auth.route("/temperature")
def temperature():
   c, f = read_temperature()
   if c > 75:
       flash("TOO HOTT!!!")
   return render_template("base.html", c=c, f=f)
