person = {
    "name" : "Ricky",
    "gender" : "male",
    "age" : 25
}

prop = input("Enter wich property want to know ").lower()

print(person.get(prop, "Property does not exist"))
