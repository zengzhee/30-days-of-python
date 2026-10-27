# Day 3: 30 Days of python programming

base = input('Enter base: ')
height = input('Enter height: ')
area = 0.5*float(base)*float(height)
print(f'The area of the triangle is {area}')

a = input('Enter side a: ')
b = input('Enter side b: ')
c = input('Enter side c: ')
perimeter = int(a)+int(b)+int(c)
print('The perimeter of the triangle is', perimeter)

rec_length = input('Enter rectangle length: ')
rec_width = input('Enter rectangle width:: ')
rec_area = int(rec_length)*int(rec_width)
print('The area of the rectangle is', rec_area)
rec_perimeter = 2*(int(rec_length)+int(rec_width))
print('The perimeter of the rectangle is', rec_perimeter)

radius = input('Enter circle radius: ')
area_of_circle = 3.14*float(radius)**2
circum_of_circle = 2*3.14*float(radius)
print('The area of the circle is', area_of_circle)
print('The circumfrance of the circle is', circum_of_circle)

print(len('python')==len('dragon'))

if len('python') == len('dragon'):
    print('python is the same length as dragon')
else:
    print('python is not the same length as dragon')

print('on in python and dragon', 'on' in 'python' and 'dragon')

sentance = 'I hope this course is not full of jargon'
if 'jargon' in sentance:
    print('jargon found in sentance')
else:
    print('jargon not found in sentance')

text_length = len('python')
text_length_float = float(text_length)
text_length_str = str(text_length)

num = 5
if num%2 == 0:
    print('num is even')
else:
    print('num is odd')

print(7//3 == int(2.7))
print(type('10') == type(10))
print(int(float('9.8')) == 10)

hours = input('Enter hours: ')
rate = input('Enter rate per hour: ')
earnings = float(hours)*float(rate)
print('Your earnings is', earnings)

years_lived = input('Enter number of years yoy have lived: ')
gap_year = int(years_lived)/4
days_lived = int(years_lived)*365 + gap_year
hours_lived = days_lived*24
min_lived = hours_lived*60
sec_lived = min_lived*60

print('gap years:', gap_year)
print('days lived:', days_lived)
print('hours lived:', hours_lived)
print('minutes lived:', min_lived)
print('seconds lived:', sec_lived)

for n in range(1,6):
    print(n, n**0, n**1, n**2, n**3)