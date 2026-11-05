empty_dict = {}

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

dog = {}

dog['name'] = 'hotdog'
dog['color'] = 'dark brown'
dog['breed'] = 'dachshund'
dog['legs'] = 4
dog['age'] = 2
print(dog)

student = {
    'first_name' : 'Zeng Zhe',
    'last_name' : 'Keh',
}
print(student)

student['gender'] = 'male'
student['age'] = '22'
student['marital status'] = 'single'
student['country'] = 'Singapore'
print(student)
print(len(student))

print(person['skills'])
person['skills'].append('HTML')
person['skills'].append('C++')
print(person['skills'])

print(student.keys())
print(student.values())

print(student.items())

del student['marital status']
print(student)

del student