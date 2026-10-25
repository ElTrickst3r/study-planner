# Study Planner

Study Planner is a small web app for keeping track of study tasks and deadlines. It was built as a prototype for Mandatory Assignment 3 in DAVE3625.

## Features

- Add a task with a title, subject, and deadline.
- Mark tasks as done or reopen them.
- Delete tasks after a confirmation prompt.
- Keep tasks between app restarts using a local SQLite database.

## Technology

- Python and Flask
- SQLite
- HTML and CSS
- `uv` for dependency management

## Run locally

Install [uv](https://docs.astral.sh/uv/) if needed. Then, from the project directory, run:

```bash
uv sync
uv run python app.py
```

Open the local address shown in the terminal (usually `http://127.0.0.1:5000/`).

The app creates `tasks.db` automatically on the first run. The database is local and is not included in the GitHub repository.

## Use of AI

I used ChatGPT to brainstorm a manageable app idea, plan the implementation, generate initial code, and suggest improvements. I reviewed the suggestions and tested each feature in the browser before continuing. After testing the first version, I added task completion and deletion and adjusted the header styling and text contrast based on how the interface looked in the browser.

## Testing

I manually checked that:

- The app starts and displays the page.
- A task can be added with a title, subject, and deadline.
- Tasks remain after refreshing the page and restarting the app.
- A task can be marked as done and reopened.
- The Delete confirmation can be cancelled or confirmed to remove the task.
- The form blocks submission when a required field is empty.
- The layout remains usable in a narrow browser window.