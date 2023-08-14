import requests
import json
import os

def get_user_data():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    return response.json()

def get_user_data_phone():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_json_path = os.path.join(current_dir, "data.json")
    
    with open(data_json_path, "r") as json_file:
        data = json.load(json_file)
    
    return data