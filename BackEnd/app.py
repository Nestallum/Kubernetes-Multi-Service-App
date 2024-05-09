from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database
db = mysql.connector.connect(
    host="host.docker.internal",
    user="root",
    password="nestallum_db_2511",
    database="db"
)

cursor = db.cursor()

@app.route('/')
def get_data():
    # Execute a query to fetch data from the database
    cursor.execute("SELECT * FROM db.students")
    # Fetch all the result rows
    rows = cursor.fetchall()
    
    # Create lists for each field
    student_numbers = []
    first_names = []
    last_names = []

    # Populate the lists with data from the database
    for row in rows:
        student_numbers.append(row[0])
        first_names.append(row[1])
        last_names.append(row[2])

    # Create a dictionary with the populated lists
    data = {
        'Student Number': student_numbers,
        'First Name': first_names,
        'Last Name': last_names
    }

    # Return the data in JSON format
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)