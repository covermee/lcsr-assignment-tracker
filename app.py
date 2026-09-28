import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form["title"]
        course = request.form["course"]
        due_date = request.form["due_date"]

        connection = sqlite3.connect("assignments.db")

        connection.execute(
            "INSERT INTO assignments (title, course, due_date) VALUES (?, ?, ?)",
            (title, course, due_date)
        )

        connection.commit()
        connection.close()

    connection = sqlite3.connect("assignments.db")

    assignments = connection.execute(
        "SELECT * FROM assignments"
    ).fetchall()

    connection.close()

    return render_template("index.html", assignments=assignments)
