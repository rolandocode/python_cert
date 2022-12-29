num1 = 8
num2 = 4
print (num1 > num2)
print (num1 < num2)
print (num1 == num2)

num1 = float (input("first number: "))
num2 = float (input("first number: "))

if (num1 > num2):
    print(num1, " is greater than ", num2)
elif (num1 == num2):
    print(num1, " is equals to ", num2)
else:
    print(num1, " is less than ", num2)

print ("out of if")