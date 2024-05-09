from flask import Flask, jsonify

app = Flask(__name__)

data = {
    'First Name': ['LATTAB', 'AZZAOUI'],
    'Last Name': ['Nassim', 'Mohamed'],
    'Student Number': ['123456789', '987654321']
}

@app.route('/')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
