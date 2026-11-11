# syntax
# Declaring a function
def function_name():
    return
# Calling a function
function_name()

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    print(nums)
    return total
print(sum_all_nums(2, 3, 5)) # 10

def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum

print(add_two_numbers(4,5))

def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area

print(area_of_circle(5))

def add_all_numbers(*arg):
    sum = 0
    for i in arg:
        if type(i) != int:
            print(f'{i} is not a integer')
        else:
            sum += i
    return sum

print(add_all_numbers(1,'e',3,4,5))

def conver_celsius_to_fahrenheit(temp_celsius):
    temp_fahrenheit = temp_celsius * (9/5) + 32
    return temp_fahrenheit

print(conver_celsius_to_fahrenheit(30))

def check_season(month):
    if month in ('December', 'January', 'Feburary'):
        return 'Winter'
    elif month in ('March' , 'April' , 'May'):
        return 'Spring'
    elif month in ('June' , 'July' , 'August'):
        return 'Summer'
    elif month in ('September' , 'October' , 'November'):
        return 'Autumn'
    else:
        return 'Month not recognised'

print(check_season('November'))

def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return None
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(1, 2, 3, 6))

def print_list(fruits):
    for i in fruits:
        print(i)

fruits = ['kiwi', 'banana', 'apple', 'papaya']
print_list(fruits)

def reverse_list(a):
    reverse = a[::-1]
    return reverse

print(reverse_list(fruits))

def capitalize_list_items(list):
    return [i.upper() for i in list]

print(capitalize_list_items(fruits))

def add_item(list, item):
    list.append(item)
    return list

print(add_item(fruits, 'orange'))

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

def remove_item(list, item):
    list.remove(item)
    return list

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

def sum_of_numbers(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

def sum_of_odds(num):
    odd_sum = 0
    for i in range(num+1):
        if i%2==0:
            continue
        else:
            odd_sum += i
    return odd_sum

def sum_of_evens(num):
    even_sum = 0
    for i in range(num+1):
        if i%2==0:
            even_sum += i
        else:
            continue
    return even_sum

print(sum_of_evens(5))
print(sum_of_odds(10))
print(sum_of_evens(100)) 

def evens_and_odds(num):
    even_count = 0
    odd_count = 0
    for i in range(num+1):
        if i%2==0:
            even_count += 1
        else:
            odd_count += 1
    print(f'The number of odds are {odd_count}')
    print(f'The number of evens are {even_count}')

evens_and_odds(100)

def greet(name = 'Guest'):
    print(f'Hello {name}!')

greet()
greet('Zeng Zhe')

def show_args(**kwargs):
    pairs = [f"{key}: {value}" for key, value in kwargs.items()]
    print("Received: " + ", ".join(pairs))

show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny

# 1. Prime check
def is_prime(n):
    if not isinstance(n, int) or n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# 2. All items unique
def all_unique(items):
    return len(items) == len(set(items))

# 3. All items the same data type
def all_same_type(items):
    return len({type(item) for item in items}) <= 1

print([n for n in range(30) if is_prime(n)])  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(all_unique([1, 2, 3]))                   # True
print(all_unique([1, 2, 2]))                   # False
print(all_same_type([1, 2, 3]))                # True
print(all_same_type([1, '2', 3.0]))            # False