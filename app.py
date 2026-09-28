from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form["title"]
        course = request.form["course"]
        due_date = request.form["due_date"]

        print(title)
        print(course)
        print(due_date)

    return render_template("index.html")

