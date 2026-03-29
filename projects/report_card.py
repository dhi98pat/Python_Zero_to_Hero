# ================= STUDENT REPORT CARD ====================
# Input section

name = "Dhiraj Pate"
student_class = "10th Grade"

## Subjects

math = 88
science = 91
computer = 94
english = 95
history = 96

## Processing
total_marks = math + science + computer + english + history
percentage = total_marks / 5
# Grade Logic
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "D"
## Output /Report
print("=============Report Card================")
print("Name:",name)
print("Student Class:",student_class)
print("Total Marks:",total_marks)
print("Percentage:",percentage, "%")
print("Grade:",grade)