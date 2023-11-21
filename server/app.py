from flask import Flask, jsonify, request
import psycopg2


app = Flask(__name__)

conn = psycopg2.connect('postgres://master:GCH2tuj1egk@db:5432/testdb')

CREATE_TASKS_TABLE = (
    "CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY, name TEXT);"
)

def create_tasks_table():
    try:
        cursor = conn.cursor()
        cursor.execute(CREATE_TASKS_TABLE)
        conn.commit()
        cursor.close()
    except psycopg2.Error as e:
        print("Error creating tasks table:", e)

create_tasks_table()

@app.route('/api', methods=['GET'])
def index():
  return {
    "channel": "The Show",
    "tutorial": "React, Flask and Docker"
  }


@app.route('/tasks', methods=['GET'])
def get_tasks():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks;')
    tasks = cursor.fetchall()
    cursor.close()
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task_name = data.get('name')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (name) VALUES (%s);', (task_name,))
    conn.commit()
    cursor.close()
    return jsonify({'message': 'Task created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
