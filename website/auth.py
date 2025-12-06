from flask import Blueprint, render_template, flash
from website.stuff import read_temperature

auth = Blueprint('auth', __name__)

@auth.route("/")
def temperature():
    #defines the view function that is called when the user accesses the default route "/" when they click the link
    c = float(read_temperature())
    #gets the celsius value from stuff.py
    #converts it to a float so that it can be calculated into f
    if 25 < c and 40 > c:
        flash("WARNING! Heatwave Temperatures Reached", "error")
        #uses flask flash SMS that sends this message to the html template
    elif c > 40:
        flash("WARNING! Highest Heatwave Temperatures Reached!", "error")
    else:
        pass

    f = round(c * 9 / 5 + 32, 1)
    #follows standard formula to convert celsius to fahrenheit

    return render_template("base.html", c=c, f=f)
#rendering the base.html template to display the web page to the user, while passing c and f to the template as parameters

