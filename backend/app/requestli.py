import requests

url = "http://127.0.0.1:8000/add_transaction/"
data = {
    # Remove id as it's auto-generated
    "type": "expense",
    "amount": 50.0,
    "category": "Food",
    "description": "Lunch at restaurant"
}

response = requests.post(url, json=data)
print(response.json())