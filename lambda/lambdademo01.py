students = [
    {'name': 'TOM', 'grade': 100},
    {'name': 'ROSE', 'grade': 190},
    {'name': 'Jack', 'grade': 220}
]

def rank():
    #rank n is xxx, the grade is xxx
    students.sort(key=lambda x: x['name'])
    print(students)
#accountsystemye32f8

rank()