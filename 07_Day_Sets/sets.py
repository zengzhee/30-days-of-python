st = set()
empty_set = {}

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
some_companies = ('Samsung', 'Nvidia', 'Equinix')
it_companies.update(some_companies)
print(it_companies)
it_companies.remove('Facebook')
print(it_companies)
it_companies.discard('Meta')
print(it_companies)
#discard does not raise an error if item is not found in set, while remove will raise error if item is not found

C = A.union(B)
print(C)
C = A.intersection(B)
print(C)
print(A.issubset(B))
print(A.isdisjoint(B))

print(A.symmetric_difference(B))

print(A)
del A

age_set = set(age)
print(age)
print(age_set)

#   Main difference between str, lst, tuple, set

#   str can store only text and characters
#   list can store any data types
#   tuple cannot be edited after creation
#   set does not allow duplicates and is unordered

sentence = 'I am a teacher and I love to inspire and teach people.'
words = sentence.split()
words_unique = set(words)
print(sentence)
print(words)
print(words_unique)
print(len(words_unique))