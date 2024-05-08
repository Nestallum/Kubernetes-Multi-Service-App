from flask import Flask, jsonify

app = Flask(__name__)

# Simuler une base de données
students = [
    {"nom": "Doe", "prenom": "John", "num_etudiant": "12345"},
    {"nom": "Smith", "prenom": "Alice", "num_etudiant": "67890"}
]

@app.route('/get-data')
def get_data():
    # Ici, vous interrogeriez la base de données pour récupérer les données réelles
    # Pour l'instant, nous utilisons simplement une liste en dur
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
