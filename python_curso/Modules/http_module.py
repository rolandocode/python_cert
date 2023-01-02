#py -m pip install requests

import requests
import json
#https://bobbyhadz.com/blog/python-could-not-find-version-that-satisfies-the-requirement-pprint#:~:text=The%20error%20%22Could%20not%20find,a%20built%2Din%20Python%20module.
import pprint

# response = requests.get("https://randomuser.me/api/")
# response.content
# print(response.content)

url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple"
response = requests.get(url)

#https://www.datasciencelearner.com/attributeerror-str-object-has-no-attribute-read-solved/#:~:text=The%20error%20attributeerror%3A%20'str',no%20attribute%20'read'%20error.
question = json.loads(response.text)

# Beuty view of json
# print(pprint.pprint(question))
print("Category -", question["results"][0]["category"])
print("Question: ", question["results"][0]["question"])
print("Correct answer: ", question["results"][0]["correct_answer"])

person = {"name": "Rolando", "age": 30, "email": "rolando@gmail.com"}

person_json = json.dumps(person)
print ("serialized json: ", person_json)