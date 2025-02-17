from flask import Flask, render_template, request
import db
app = Flask(__name__)
@app.route("/")
def lolo_pepe():
    data = db.cars
    return render_template("index.html", cars=data)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/cars/")
def info_cars():
    import db
    return render_template("cars.html", cars=db.cars)

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

        return f"{company}"

app.run(debug=True)

