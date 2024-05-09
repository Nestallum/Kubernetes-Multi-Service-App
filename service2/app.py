import requests
import pandas as pd
from flask import Flask

app = Flask(__name__)

def generate_html_from_dataframe(df):
    html = "<h1>Student Data</h1>"
    html += df.to_html(index=False)
    return html

@app.route('/')
def display_data():
    # Appeler le service 1 pour récupérer les données
    response = requests.get("http://service1/get-data")
    data = response.json()
    # Afficher les données
    df = pd.DataFrame(data)
    return generate_html_from_dataframe(df)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
