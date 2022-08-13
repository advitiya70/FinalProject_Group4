from flask import Flask, render_template as rt
from getData import getreport
import service as s
app = Flask(__name__)


@app.route("/")
def homepage():

    var1 = getreport()

    return rt("index.html", var=var1)


@app.route("/Home.html")
def HP():
    var1 = getreport()

    return rt("index.html", var=var1)


@app.route("/Contact.html")
def contact():

    return rt("Contact.html")


@app.route("/getallitems")
def getallitems():

    return s.getall()


@app.route("/gettemprange/min=<min>&&max=<max>")
def getRange(min="0", max="0"):

    return s.gettemprange(int(min), int(max))


@app.route("/getcity/city=<city>")
def getCity(city=""):

    return s.getbyid(city)


@app.route("/About.html")
def about():
    var = getreport()

    temperatures = [float(c[3]) for c in var]
    tempidx = [round(min(temperatures) * 0.75),
               round(max(temperatures) * 1.25)]
    temperatures = [tempidx[0]] + temperatures

    visibility = [float(c[6]) for c in var]
    vidx = [round(min(visibility) * 0.75),
            round(max(visibility) * 1.25)]
    visibility = [vidx[0]] + visibility
    cities = [""] + [c[1] for c in var]
    return rt("About.html", var=var, cities=cities, temperatures=temperatures, tempidx=tempidx, visibility=visibility, vidx=vidx)


if __name__ == "__main__":
    app.run()
