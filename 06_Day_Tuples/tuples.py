empty_tuple = ()

brothers = ('ron', 'yip kai')
sisters = ('adli', 'sin tuck')
siblings = brothers + sisters
print(siblings)
print(len(siblings))

family_members = list(siblings)
family_members.append('mom')
family_members.append('dad')
print(family_members)

brother1, brother2, sister1, sister2, mom, dad = family_members
print(brother1)
print(sister1)
print(mom)
print(dad)

fruits = ('apple', 'banana', 'kiwi', 'mango')
vegetables = ('lettuce', 'cucumber', 'parsley')
animal_products = ('prok', 'beef', 'chicken')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
print(len(food_stuff_lt))

middle = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    #if even
    food_stuff_lt = food_stuff_lt[:middle - 1] + food_stuff_lt[middle + 1:]
else:
    #if odd
    food_stuff_lt = food_stuff_lt[:middle] + food_stuff_lt[middle + 1:]

print(food_stuff_lt)
print(len(food_stuff_lt))

food_stuff_lt = food_stuff_lt[3:-3]
print(food_stuff_lt)
print(len(food_stuff_lt))

del food_stuff_tp
#print('mango' in food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)