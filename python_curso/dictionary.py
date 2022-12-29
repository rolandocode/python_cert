person = { 
    "first_name": "Jonh", 
    "last_name" : "Green",
    "birth_year" : 1990,
    "country_of_birth": "Canada"
    }

person["children"] = ["Ana", "Jonh"]

person["children"].append("Elton")
print(person["first_name"])

print(person)

print(person.get("age", "invalid property"))
key = "country_of_birth"
print(person[key])