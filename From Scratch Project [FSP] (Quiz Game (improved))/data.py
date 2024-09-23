import html
import requests

# declaring a dict name parameter for API fetching purpose
parameters = {"amount": 20, "category": 18, "difficulty": "hard", "type": "multiple"}

# creating a request for the required url
response = requests.get(url="https://opentdb.com/api.php", params=parameters)

# raise any error if happens
response.raise_for_status()

# catching the results key from the json file and store it in question_data
question_data = response.json()["results"]


# un-escaping the html abbreviations through html module and using list comprehension store them in variable name question_bank
question_bank = [
    {
        "question": html.unescape(question["question"]),
        "correct_answer": html.unescape(question["correct_answer"]),
        "incorrect_answers": [html.unescape(options) for options in question["incorrect_answers"]]
    }
    for question in question_data
]
