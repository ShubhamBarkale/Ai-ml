# Check if a student passes (minimum 35 marks in each subject).


m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Student Pass")
else:
    print("Student Fail")

