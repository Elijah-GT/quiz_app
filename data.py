import requests
import html

AMOUNT = 10
TYPE = "boolean"  #True/False

parameters = {
    "amount": 10,
    "type": TYPE,
}

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]

