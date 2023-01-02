# file = open("test2abc1.txt", "x")
import time as t

# file = open(r'C:\Users\Rolando\Desktop\Code\Udemy\python_cert\python_curso\Modules\file.txt', "a")
# stringToWrite = "\n" + str (t.time())
# file.write(stringToWrite)

# file = open(r'C:\Users\Rolando\Desktop\Code\Udemy\python_cert\python_curso\Modules\file.txt')
# print(file.read())

file = open('file.txt', "a")
stringToWrite = "\n" + str (t.time())
file.write(stringToWrite)

file = open('file.txt')
print(file.read())