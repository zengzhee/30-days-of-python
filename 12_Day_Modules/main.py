
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100
print(mass)
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive


def random_user_id():
    user_id = ""
    for i in range(6):
        user_id += str(randint(0,9))
    return user_id

print(random_user_id()) 


from random import choices

def user_id_gen_by_user(no_char, no_id):
    chars = string.ascii_letters + string.digits
    for i in range(no_id):
        user_id = "".join(choices(chars, k=no_char))
        print(user_id)

input1 = int(input('Enter number of character: '))
input2 = int(input('Enter number of ID generated: '))
user_id_gen_by_user(input1, input2)

def rgb_color_gen():
    rgb = [0, 0, 0]
    for i in range(len(rgb)):
        rgb[i] = randint(0, 255)
    print(f"rgb({rgb[0]},{rgb[1]},{rgb[2]})")

rgb_color_gen()

def list_of_hexa_colors(count):
    hexa = '0123456789ABCDEF'
    list_of_hexa = []
    for _ in range(count):
        hexa_color = "#" + "".join(choices(hexa, k=6))
        list_of_hexa.append(hexa_color)
    return list_of_hexa

print(list_of_hexa_colors(4))

def list_of_rgb(count):
    list_of_rgb = []
    for i in range(count):
        rgb_color = 'rgb(' + str(randint(0,255)) + ', ' + str(randint(0,255)) + ', '+ str(randint(0,255)) + ')'
        list_of_rgb.append(rgb_color)
    return list_of_rgb

print(list_of_rgb(1))

def generate_colors(type, count):
    if type == 'hexa':
        print(list_of_hexa_colors(count))
    elif type == 'rgb':
        print(list_of_rgb(count))
    else:
        print('not recognised')

generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
generate_colors('hexa', 1) # ['#b334ef']
generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
generate_colors('rgb', 1)  # ['rgb(33,79, 176)']