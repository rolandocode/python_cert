grade1 = float ( input("Type the grade of the first test: ") )
grade2 = float ( input("Type the grade of the second test: ") )

absences = int ( input("Type the number of absences: ") )
total_classes = int ( input("Type the total number of classes: ") ) 

avg_grade = (grade1 + grade2) / 2 
attendance = (total_classes - absences) / total_classes

if (avg_grade >= 6):
    if (attendance >= 0.8): 
        print("The student has been approved.")
else: 
    print("The student has failed.") 
