from flask import Flask, render_template, request
from functions import add_new_car
import db

cars = db.cars

app = Flask(__name__)
@app.route("/")
def lolo_pepe():
    data = cars
    return render_template("index.html", cars=data)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/cars/")
def info_cars():
    return render_template("cars.html", cars=cars)

@app.route("/new_car", methods=["GET", "POST"])
def new_car():
    if request.method == "GET":
        return render_template("new_car.html")
    elif request.method == "POST":
        company = request.form.get("company")
        model = request.form.get("model")
        info = request.form.get("info")
        logo = request.form.get("logo")
        image = request.form.get("image")
        add_new_car(cars, company, model, info, logo, image)
        return render_template("new_car.html")

@app.route("/list_car")
def list_car():
    return render_template("list_car.html", cars=cars)

app.run(debug=True)

