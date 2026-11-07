age = input('Enter your age: ')
if int(age) >= 18:
    print('You are old enough to learnt to dirve')
else:
    print(f'You need {18-int(age)} more years to learn to dive')

p1_age = input('Enter person1 age: ')
p2_age = input('Enter person2 age: ')
if int(p1_age) > int(p2_age):
    if int(p1_age) - int(p2_age) == 1:
        print('person1 is older than person2 by 1 year')
    else:
        print(f'person1 is older than person2 by {int(p1_age) - int(p2_age)} year')
elif int(p2_age) > int(p1_age):
    if int(p2_age) - int(p1_age) == 1:
        print('person2 is older than person1 by 1 year')
    else:
        print(f'person2 is older than person1 by {int(p2_age) - int(p1_age)} year')
else:
    print('person1 and person2 are the same age')

a = input('Enter number one: ')
b = input('Enter number two: ')
if int(a) > int(b):
    print(f'{a} is greater than {b}')
elif int(b) > int(a):
    print(f'{b} is greater than {a}')
else:
    print(f'{a} is equals to {b}')

score = input('Enter score: ')
score_int = int(score)
if score_int >= 90:
    grade = 'A'
elif score_int >= 80:
    grade = 'B'
elif score_int >= 70:
    grade = 'C'
elif score_int >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f'Grade: {grade}')

month = input('Enter month: ')
Autumn = ('September', 'October', 'November')
Winter = ('December', 'January', 'February')
Spring = ('March', 'April', 'May')
Summer = ('June', 'July', 'August')
season = 'idk'
if month in Autumn:
    season = 'Autumn'
elif month in Winter:
    season = 'Winter'
elif month in Spring:
    season = 'Spring'
elif month in Summer:
    season = 'Summer'
else:
    print('Month not found')

print(f'Season of {month} is {season}')

fruits = ['banana', 'orange', 'mango', 'lemon']
input_fruit = input('Enter fruit: ')
if input_fruit in fruits:
    print(f'{input_fruit} is already in the list')
else:
    fruits.append(input_fruit)
    print(fruits)
    print(f'{input_fruit} added to the list')

person={
    'first_name': 'Zeng Zhe',
    'last_name': 'Keh',
    'age': 22,
    'country': 'Singapore',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    print(skills[len(skills) // 2])

if 'skills' in person:
    print('Python' in person['skills'])

skills = set(person.get('skills', []))
if {'React', 'Node', 'MongoDB'} <= skills:
    print('He is a fullstack developer')
elif {'Node', 'Python', 'MongoDB'} <= skills:
    print('He is a backend developer')
elif skills == {'JavaScript', 'React'}:
    print('He is a front end developer')
else:
    print('unknown title')

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
else:
    print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He is single')