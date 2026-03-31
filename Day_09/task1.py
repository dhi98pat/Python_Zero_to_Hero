student_score = {
    'Harry': 88,
    'Rom' : 78,
    'Herminoe' : 95,
    'Draco': 75,
    'Neville': 60
}
student_grads = {}
for student in student_score:
    score = student_score[student]
    if score >= 91:
        student_grads[student] = "Outstanding"
    elif score >= 81:
        student_grads[student] = "Exceed Expectation"
    elif score >= 71:
        student_grads[student] = "Acceptable"
    else:
        student_grads[student] = "Fail"
print(student_grads)