grades = ['A','B','F','C','F']
def remove_fail(grade):
    return grade != 'F'
#Filter
print(list(filter(remove_fail,grades)))
#For loop
filtered_grade = []
for grade in grades:
    if grade != 'F':
        filtered_grade.append(grade)
print(filtered_grade)
#Comprehensions Method
print([grade for grade in grades if grade != 'F'])