import sqlite3
from flask import Flask, render_template, request, redirect, url_for

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

        return redirect(url_for("home"))

    connection = sqlite3.connect("assignments.db")

    assignments = connection.execute(
        "SELECT * FROM assignments"
    ).fetchall()

    connection.close()

    return render_template("index.html", assignments=assignments)


@app.route("/complete/<int:assignment_id>", methods=["POST"])
def complete_assignment(assignment_id):
    connection = sqlite3.connect("assignments.db")

    connection.execute(
        "UPDATE assignments SET completed = 1 WHERE id = ?",
        (assignment_id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("home"))


@app.route("/delete/<int:assignment_id>", methods=["POST"])
def delete_assignment(assignment_id):
    connection = sqlite3.connect("assignments.db")

    connection.execute(
        "DELETE FROM assignments WHERE id = ?",
        (assignment_id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("home"))