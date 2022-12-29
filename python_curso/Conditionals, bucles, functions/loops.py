blog_post = ["Post1", "Post2", "Post3", "", "Post x"]

for post in blog_post:
    if (post == ""):
        continue
    print(post)

myString ="Rolando"

for char in myString:
    print(char)

for x in range(0,100):
    print(x)

person = {
    "Name": "Rolando", 
    "Age" : 25, 
    "Gender": "Male"}

for key in person:
    print(key, ": ", person[key])