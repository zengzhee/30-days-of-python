# Day 2: 30 Days of python programming

first_name = 'Zeng Zhe'
last_name = 'Keh'
full_name = 'Keh Zeng Zhe'
country = 'Singapore'
city = 'Jurong West'
age = 19
year = 2026
is_married = False
is_true = True
is_light_on = False
first_name, last_name, full_name = 'Zeng Zhe', 'Keh', 'Keh Zeng Zhe'

print('Full Name: ', full_name)
print('Age: ', age)
print('Country: ', country)

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))

print('Length of first name: ', len(first_name))
print('Length of last name: ', len(last_name))
print(len(first_name) - len(last_name))

num_one, num_two = 5, 4

diff = num_one-num_two
print('Diff: ', diff)
product = num_one*num_two
print('Product: ', product)
division = num_one/num_two
print('Div: ', division)
remainder = num_two%num_one
print('Remainder: ', remainder)
exp = num_one**num_two
print('Exp: ', exp)
floor_division = num_one//num_two
print('Floor division: ', floor_division)

radius = input('Radius of circle in meters: ')
area_of_circle = 3.14*float(radius)**2
circum_of_circle = 2*3.14*float(radius)
print('Radius: ', radius, 'm, ', 'Area: ', area_of_circle, 'm2, ', 'Circumfrance: ', circum_of_circle, 'm')

first_name = input('Enter first name: ')
last_name = input('Enter last name: ')
country = input('Enter country: ')
age = input('Enter age: ')

print('Full Name: ', first_name, last_name)
print('Age: ', age)
print('Country: ', country)