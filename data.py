import requests

question_data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
question_data.raise_for_status()
question_data = question_data.json()["results"]


