count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1

language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

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
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)



for number in range(0,11):
    print(number)
for number in range(10,-1,-1):
    print(number)

count = 1
while count < 8:
    print('#' * count)
    count += 1

row = 0
while row < 8:
    print('# ' * 8)
    row += 1

a = 0
while a < 11:
    print(f'{a} x {a} = {a*a}')
    a += 1

list1 = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in list1:
    print(i)

for i in range(0,100,2):
    print(i)

for i in range(1,101,2):
    print(i)

sum = 0
for i in range(0,101):
    print(i)
    sum += i
print(sum)

odd_sum = 0
even_sum = 0
for i in range(0,101):
    if i%2==0:
        even_sum += i
    else:
        odd_sum += i
print(odd_sum)
print(even_sum)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

land = []
for country in countries:
    if 'land' in country:
        print(country)
        land.append(country)
print(land)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_reverse = []
count = -1
for fruit in fruits:
    fruits_reverse.append(fruits[count])
    count -= 1
print(fruits_reverse)

from countries_data import countries_data

all_languages = []
for country in countries_data:
    for key in country:
        if key == 'languages':
            for langauge in country[key]:
                all_languages.append(langauge)

unique_languages = set(all_languages)
print(unique_languages)
total_langauges = len(unique_languages)
print(total_langauges)



# Part 2: ten most spoken languages
language_counts = {}
for country in countries_data:
    for language in country['languages']:
        language_counts[language] = language_counts.get(language, 0) + 1

print(language_counts.items())

def get_count(item):
    # item is a (language, count) tuple, e.g. ('English', 91)
    return item[1]

sorted_languages = sorted(language_counts.items(), key=get_count, reverse=True)

print('Ten most spoken languages:')
for language, count in sorted_languages[:10]:
    print(language, count)


# Part 3: ten most populated countries
def get_population(country):
    return country['population']

top_10 = sorted(countries_data, key=get_population, reverse=True)[:10]

print('\nTen most populated countries:')
for country in top_10:
    print(country['name'], country['population'])