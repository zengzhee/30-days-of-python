# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10]

# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console
print((lambda a, b: a + b)(2,3))

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22





#exercise

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zero_numbers = [i for i in numbers if i <= 0]
print(negative_zero_numbers)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

single_list = [number for row in list_of_lists for number in row]
print(single_list)

numbers = []
for number in range(11):
    numbers.append(number)
    for count in range (6):
        numbers.append(number ** count)

print(numbers)

numbers = [tuple([number] + [number ** count for count in range(6)]) for number in range(11)]
print(numbers)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

country_list = [[country.upper(), country[:3].upper(), city.upper()] for [(country, city)] in countries]
print(country_list)

country_dict = [{'country': country.upper(), 'city': city.upper()} for [(country, city)] in countries]
print(country_dict)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

full_name_list = [[first_name + ' ' + last_name] for [(first_name, last_name)] in names]
full_name = [name for row in full_name_list for name in row]
print(full_name)