# ...existing code...
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

def init_db():

    with sqlite3.connect('database.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS TODO (
                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     task TEXT NOT NULL)''')
        conn.commit()

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        task = request.form['task']
        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO TODO (task) VALUES (?)', (task,))
            conn.commit()
        return redirect(url_for('tasks'))
    return render_template('add.html')


@app.route('/tasks')
def tasks():
    with sqlite3.connect('database.db') as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        # select ID as id to use a consistent lowercase name in templates
        cursor.execute('SELECT ID AS id, task FROM TODO')
        data = cursor.fetchall()
    return render_template('tasks.html', data=data)



@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM TODO WHERE ID = ?', (task_id,))
        conn.commit()
    return redirect(url_for('tasks'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
# ...existing code...