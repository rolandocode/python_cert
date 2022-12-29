months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December")
birthday = input("Type birthdate DD-MM-YYYY ")

index = int(birthday[3:5])

bd_month = months[index-1]

print("Your month is ", bd_month);

people = ["Jonh", "Mary", "Peter"]

user = input("Type name ")
people.append(user)
print(people)