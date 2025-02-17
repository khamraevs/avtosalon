from flask import Flask, render_template
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

app.run(debug=True)

