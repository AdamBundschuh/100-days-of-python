# Medium Comics API
# https://opentdb.com/api.php?amount=10&category=29&difficulty=medium&type=boolean
# BASE URL: https://opentdb.com/api.php
# ARGS: amount=10, category=29, difficulty=medium, type=boolean

import requests

parameters = dict(amount=10, type='boolean')
response = requests.get(url='https://opentdb.com/api.php', params=parameters)
response.raise_for_status()
question_data = response.json()['results']

# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The first computer bug was formed by faulty wires.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     }
# ]
