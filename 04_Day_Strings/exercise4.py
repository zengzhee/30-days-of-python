string = 'Thirty', 'Days', 'Of', 'Python'
print(string[0], string[1], string[2], string[3])

x = 'Coding'
y = 'For'
z = 'All'
print(x, y, z)

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

remove_first_word = company[7:]
print(remove_first_word)

target = 'Coding'
print(company.index(target))
print(company.find(target))
print(company.replace(target, 'Python'))

split = company.split()
print(split)

brands = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(brands.split(','))

print(company[0])
print(company[-1])
print(company[10])

acronym = 1

print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))

sentance = 'You cannot end a sentence with because because because is a conjunction'
print(sentance.find('because'))
print(sentance.rindex('because'))
slice_sentance = sentance[0:sentance.find('because')] + sentance[sentance.rindex('because')+len('because'):]
print(slice_sentance)

substring = 'Coding'
print(company.index(substring))

x = '   Coding For All      '
print(x.strip())

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

libaries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' '.join(libaries)
print(result)

single = 'I am enjoying this challenge. \nI just wonder what is next.'
print(single)

print('Name\tAge\tCountry\t\tCity\nZZ\t22\tSingapore\tidk')

radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius 10 is {area} meters square')

num1 = 8
num2 = 6
print('{} + {} = {}'.format(num1, num2, num1+num2))
print('{} - {} = {}'.format(num1, num2, num1-num2))
print('{} * {} = {}'.format(num1, num2, num1*num2))
print('{} / {} = {}'.format(num1, num2, num1/num2))
print('{} % {} = {}'.format(num1, num2, num1%num2))
print('{} // {} = {}'.format(num1, num2, num1//num2))
print('{} ** {} = {}'.format(num1, num2, num1**num2))
