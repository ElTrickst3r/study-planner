import sqlite3
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
DATABASE = Path(__file__).parent / "tasks.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                subject TEXT NOT NULL,
                deadline TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
        """)


@app.route("/")
def index():
    with get_connection() as connection:
        tasks = connection.execute(
            "SELECT * FROM tasks ORDER BY completed, deadline, id"
        ).fetchall()

    return render_template("index.html", tasks=tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    subject = request.form.get("subject", "").strip()
    deadline = request.form.get("deadline", "").strip()

    if title and subject and deadline:
        with get_connection() as connection:
            connection.execute(
                "INSERT INTO tasks (title, subject, deadline) VALUES (?, ?, ?)",
                (title, subject, deadline),
            )

    return redirect(url_for("index"))


@app.route("/tasks/<int:task_id>/toggle", methods=["POST"])
def toggle_task(task_id):
    with get_connection() as connection:
        connection.execute(
            """
            UPDATE tasks
            SET completed = CASE WHEN completed = 0 THEN 1 ELSE 0 END
            WHERE id = ?
            """,
            (task_id,),
        )

    return redirect(url_for("index"))


@app.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    with get_connection() as connection:
        connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    return redirect(url_for("index"))


initialize_database()

if __name__ == "__main__":
    app.run(debug=True)