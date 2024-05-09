from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Connexion à la base de données MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Grassim_80",
    database="db"
)

cursor = db.cursor()

@app.route('/')
def get_data():
    # Exécutez une requête pour récupérer les données depuis la base de données
    cursor.execute("SELECT * FROM db.students")
    # Récupérez toutes les lignes de résultats
    rows = cursor.fetchall()
    
    # Créez des listes pour chaque champ
    student_numbers = []
    first_names = []
    last_names = []

    # Remplissez les listes avec les données de la base de données
    for row in rows:
        student_numbers.append(row[0])
        first_names.append(row[1])
        last_names.append(row[2])

    # Créez un dictionnaire avec les listes remplies
    data = {
        'Student Number': student_numbers,
        'First Name': first_names,
        'Last Name': last_names
    }

    # Retournez les données au format JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
