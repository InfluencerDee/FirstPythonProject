list1 = [1, 2, 3, 4, 5]

list1[2] = 6

list1.append("Cletus")

print (list1)

list2 = ["denise" , "Joy", "Queen"]

print(list1 + list2)

list1.extend(list2)
print(list1)

#Declare an empty list

empty_list = []

#Declare a list with more than 5 items

five_times = [2, 1, 4, 7, 5, 9, 10]

#Find the length of your list

print(len(five_times))

# #Get the first item, the middle item and the last item of the list

print(five_times[0])
print(five_times[3])
print(five_times[-1])
#
# #Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ["Denise", 31, "50cm", False, "Uyo, Nigeria"]
#
# #Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#Print the list using print()

print (it_companies)

#Print the number of companies in the list

print (len(it_companies))

#Print the first, middle and last company

print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])

# #Print the list after modifying one of the companies

it_companies[2] = "Twitter"
print(it_companies)
#
# #Add an IT company to it_companies

it_companies.append("StarLink")
print(it_companies)

# #Insert an IT company in the middle of the companies list

it_companies.insert(4, "Xiaomi")
print(it_companies)

# #Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)

# #Join the it_companies with a string '#;  '
new_string = "#; "
it_companies.extend(new_string)
print(it_companies)

#
# #Check if a certain company exists in the it_companies list
print ("IBM" in it_companies)

# #Sort the list using sort() method
it_companies.sort()
print(it_companies)

# #Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# #Slice out the first 3 companies from the list
first_three = it_companies[0:3]
print(first_three)

# #Slice out the last 3 companies from the list
last_three = it_companies[-3:-1]
print(last_three)

# #Slice out the middle IT company or companies from the list
middle_item = it_companies[-7:-5]
print(middle_item)

# #Remove the first IT company from the list

it_companies.remove(it_companies[0])
it_companies.pop(0)
print(it_companies)

# #Remove the middle IT company or companies from the list
del it_companies[-7:-5]
print(it_companies)

# #Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# #Remove all IT companies from the list
del it_companies[0:6]
print(it_companies)

# #Destroy the IT companies list
it_companies.clear()
print(it_companies)

# #Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)

# #After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = joined_list.copy()
full_stack.insert(5,"Python")
full_stack.insert(6,"SQL")
print(full_stack)

#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
ages.sort()
minimum = min(ages)
maximum = max(ages)
print (minimum, maximum)

#Add the min age and the max age again to the list
ages.append(minimum)
ages.append(maximum)

#Find the median age (one middle item or two middle items divided by two)
ages.sort()
print(ages)
length = len(ages)
print(length)
middle = length/2
print (middle)
if middle % 2 == 0:
     median = middle + middle
     print (median)
else:
     print (middle)

#Find the average age (sum of all items divided by their number )
average = sum(ages)/len(ages)
print (average)

#Find the range of the ages (max minus min)
range_age = maximum - minimum
print (range_age)

#Compare the value of (min - average) and (max - average), use abs() method
min_diff = abs(minimum - average)
max_diff = abs(maximum - average)
print (min_diff, max_diff)

#Find the middle country(ies) in the countries list

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
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
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
  'Macedonia',
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
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
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
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
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
  'Zimbabwe',
]
countries.sort()
country_length = len(countries)
middle_country = country_length // 2

if middle_country % 2 == 0:
    final_middle_country = countries[middle_country - 1] + countries[middle_country]
    print(final_middle_country)
else:
    print (countries[middle_country])


#Unpack the first three countries and the rest as scandic countries.
new = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandic = new
print(ch, ru, us)
print (scandic)
