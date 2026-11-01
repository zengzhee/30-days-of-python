empty_list = []

list = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6']
print(len(list))
first_item = list[0]
middle_item = list[3]
last_item = list[-1]
print(first_item, middle_item, last_item)

mixed_data_types = ['zz', 19, 180, 'Single', 'Singapore']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(mixed_data_types)
print(it_companies)
print(len(it_companies))
first_item = it_companies[0]
middle_item = it_companies[len(it_companies)//2]
last_item = it_companies[-1]
print(first_item)
print(middle_item)
print(last_item)

it_companies[0] = 'Meta'
print(it_companies)
it_companies.append('Stripe')
print(it_companies)
it_companies.insert(len(it_companies)//2, 'Visa')
print(it_companies)
it_companies[0] = it_companies[0].upper()
print(it_companies)

string = ['hello']
join = it_companies + string
print(join)

does_exist = 'Google' in it_companies
print(does_exist)

it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)

remove_first_3 = it_companies[3:]
print(remove_first_3)
remove_last_3 = it_companies[:-3]
print(remove_last_3)
middle = len(it_companies)//2
remove_middle = it_companies[:middle] + it_companies[middle+1:]
print(remove_middle)

it_companies.pop(0)
print(it_companies)
middle = len(it_companies)//2
it_companies.pop(middle)
print(it_companies)
it_companies.pop()
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
#print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
new_list = front_end + back_end
print(new_list)

full_stack = new_list.copy()
print(full_stack)
index = full_stack.index('Redux')
full_stack.insert(index + 1, 'Python')
full_stack.insert(index + 2, 'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)
ages.sort()
print(ages)
min_age = ages[0]
print(min_age)
max_age = ages[-1]
print(max_age)
ages.append(min_age)
ages.append(max_age)
print(ages)
ages.sort()
print(ages)

if len(ages)%2 == 0:
    #if even
    median_age = (ages[len(ages)//2] + ages[len(ages)//2 -1])/2
else:
    #if odd
    median_age = ages[len(ages)//2]

print(median_age)

avg_age = sum(ages)/len(ages)
print(avg_age)

min_age = ages[0]
max_age = ages[-1]
age_range = max_age - min_age
print(age_range)

minavg_diff = abs(min_age - avg_age)
maxavg_diff = abs(max_age - avg_age)
print(minavg_diff)
print(maxavg_diff)

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

middle_country = countries[len(countries)//2]
print(middle_country)

mid = len(countries) // 2

if len(countries) % 2 == 0:
    # even: equal halves
    first_half = countries[:mid]
    second_half = countries[mid:]
else:
    # odd: first half gets the extra country
    first_half = countries[:mid + 1]
    second_half = countries[mid + 1:]

print(first_half)
print(second_half)