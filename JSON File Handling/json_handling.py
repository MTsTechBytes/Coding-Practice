#How to save a Python list or dictionary in a file: JSON
import json

alphabet_letters = ["a", "b", "c"]

with open("alphabets_list.json", "w") as f:
    json.dump(alphabet_letters, f)

#Writing Dictionary
customer_29876 = {
    "first name": "David",
    "last name": "Elliott",
    "address": "4803 Wellesley St.",
}

with open("alphabets_list.json", "w") as f:
    json.dump(customer_29876, f)



#How to retrieve a Python list or dictionary from a JSON file
with open("customer_29876.json", "r") as f:
    customer_29876 = json.load(f)
