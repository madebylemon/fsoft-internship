import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime

def fetch_exchange_rate():
    load_dotenv()
    url = "https://api.exchangeratesapi.io/v1/latest"
    params = {
        "access_key": os.getenv("EXCHANGE_API_KEY"),
        "base": "EUR"
    }
    response = requests.get(url, params=params)
    print("Status code:", response.status_code)
    print("Response text:", response.text) 
    if response.status_code == 200:
        try:
            data = response.json()
            today = datetime.today().strftime('%Y-%m-%d')
            filename = f"/opt/airflow/data_{today}.json"
            with open(filename, "w") as f:
                json.dump(data, f)
            print(f"Data saved to {filename}")
        except Exception as e:
            print("Error parsing JSON:", str(e))
    else:
        print(f"Error: {response.status_code}")
