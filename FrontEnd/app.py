import requests
import pandas as pd
from flask import Flask

app = Flask(__name__)
SERVICE1_URL = "http://back-end-service:80"

def generate_html_from_dataframe(df):
    html = "<h1>Student Data</h1>"
    html += df.to_html(index=False)
    return html


@app.route('/')
def get_data_from_backend():
    response = requests.get(SERVICE1_URL)
    data = response.json()
    df = pd.DataFrame(data)
    return generate_html_from_dataframe(df)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
