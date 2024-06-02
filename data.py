import requests

OPEN_TRIVIA_DATABASE_URL = "https://opentdb.com/api.php?"
parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url=OPEN_TRIVIA_DATABASE_URL, params=parameters)
response.raise_for_status()
question_data = response.json()['results']


