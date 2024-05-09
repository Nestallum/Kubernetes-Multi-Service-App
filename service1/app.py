from flask import Flask, jsonify

app = Flask(__name__)

# Simuler une base de données
data = {
        'First Name': ['LATTAB', 'AZZAOUI'],
        'Last Name': ['Nassim', 'Mohamed'],
        'Student Number': ['123456789', '987654321']
    }

@app.route('/get-data')
def get_data():
    # Ici, vous interrogeriez la base de données pour récupérer les données réelles
    # Pour l'instant, nous utilisons simplement une liste en dur
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
