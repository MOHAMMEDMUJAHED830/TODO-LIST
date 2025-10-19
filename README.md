# TODO-LIST
A simple, minimal To-Do list web application built with Python's Flask framework and SQLite for database management.
# Simple Flask To-Do App

This is a minimal web application for managing a simple to-do list, built using the **Flask** micro-framework in Python and **SQLite** for persistence.

## Features

* **Add** new tasks to the to-do list.
* **View** all current tasks.
* **Delete** tasks once they are completed.
* Uses a simple **SQLite** database to store tasks.

## Technologies Used

* **Python 3**
* **Flask** (Web Framework)
* **SQLite** (Database)
* **HTML/CSS** (Frontend templating with Jinja)

## Getting Started

Follow these steps to get a copy of the project up and running on your local machine.

### Prerequisites

You need **Python 3** installed on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [YOUR_REPOSITORY_URL]
    cd simple-flask-todo-app
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate   # On Windows
    ```

3.  **Install Flask:**
    Since this is a very simple project, you only need Flask.
    ```bash
    pip install Flask
    ```
    *(For a larger project, you would typically use a `requirements.txt` file.)*

4.  **Run the application:**
    ```bash
    python app.py
    ```

5.  **Access the application:**
    The application should now be running at `http://127.0.0.1:5000/`. The database file (`database.db`) will be automatically created the first time the application is run, thanks to the `init_db()` function in `app.py`.

## Project Structure

The core components of the application are:

* `app.py`: The main Flask application file defining routes, database interactions, and application setup.
* `database.db`: The SQLite database file (automatically created).
* `templates/`: (Implied directory where HTML files like `index.html`, `add.html`, and `tasks.html` should reside).
    * `index.html`: Home page.
    * `add.html`: Form to add a new task.
    * `tasks.html`: Page to display and delete tasks.

## License

This project is open-source and available under the **MIT License**. (You can change this or add a `LICENSE` file if you prefer a different license).
