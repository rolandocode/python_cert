data_valid = False 

while data_valid == False:
    try: 
        grade1 = input("Type the grade of the first test: ")
    except:
        print("Invalid input")
        continue
    if grade1 < 0 or grade1 > 10: 
        print("Grade should be between 0 and 10")
        continue 
    else: 
        data_valid = True 
   


data_valid = False 
while data_valid == False: 
    try:
        grade2 = float ( input("Type the grade of the second test: ") ) 
    except:
         print("Invalid input")
         continue
    if grade2 < 0 or grade2> 10: 
        print("Grade should be between 0 and 10") 
        continue 
    else:
        data_valid = True

data_valid = False 
while data_valid == False: 
    try:
        total_classes = int (input("Type the total number of classes: ") )
    except:
        print("Grade should be between 0 and 10") 
        continue 
    if total_classes <= 0: 
        print("The number of classes can't be zero or less.")
        continue