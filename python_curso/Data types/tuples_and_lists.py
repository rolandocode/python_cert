students = ["Jonh", "Mary", "Steve"]

studentCount = len(students);
first_student = students[0];
last_student = students[-1];

months = ("January", "February", "March", "April")

first_mont = months[0];

#add new element
students.append("Rolando");
#push new element
students.insert(0, "Ivonne");
#delete element, last element
students.pop()
students.pop(1)
students.remove("Mary")

students2 = ["Paul", "Jonh"]
university = students + students2
