# Question 20: Create a simple student marks program that:
#     a. accepts marks for 5 subjects,
#     b. calculates the total and percentage,
#     c. assigns a grade,and displays whether the student passed or failed.

# Solution

# Passing requires at least 40 marks in each subject. Grades use the percentage.
marks = []
for subject in range(1, 6):
    mark = float(input(f"Enter marks for subject {subject} (out of 100): "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

passed = all(mark >= 40 for mark in marks)

print("Total marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
if passed:
    print("Result: Passed")
else:
    print("Result: Failed")
