# #Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to drive")
else:
    print("You need " + str(18 - age) + " more years to learn to drive")

# #Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
your_age = int(input("Enter your age: "))
my_age = 25

if my_age > your_age:
    if abs(my_age - your_age) == 1:
        print ("You are " + str(abs(my_age - your_age)) + " year younger than me")
    else:
        print ("You are " + str(abs(my_age - your_age)) + " years younger than me")
elif my_age < your_age:
    if abs(my_age - your_age) == 1:
        print ("You are " + str(abs(my_age - your_age)) + " year older than me")
    else:
        print ("You are " + str(abs(my_age - your_age)) + " years older than me")
else:
    print("We are same age")
#
#
# #Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))

if first_num > second_num:
    print ("First number is greater than second number")
elif first_num < second_num:
    print ("First number is smaller than second number")
else:
    print ("First number is equal to second number")
#
# #Write a code which gives grade to students according to theirs scores:
score = float(input("Enter your score: "))

if score >= 80 and score <= 100:
    print ("Your score is " + str(score) + " and you got A")
elif score >= 70 and score < 80:
    print ("Your score is " + str(score) + " and you got B")
elif score >= 60 and score < 70:
    print ("Your score is " + str(score) + " and you got C")
elif score >= 50 and score < 60:
    print ("Your score is " + str(score) + " and you got D")
elif score >= 0 and score < 50:
    print ("Your score is " + str(score) + " and you got E")
else:
    print ("Your score is " + str(score) + " and not in the system")


from xmlrpc.client import boolean

#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter your month: ")
month = month.lower()

if month == "september" or month == "october" or month == "november":
    print ("the season is Autumn")
elif month == "december" or month == "january" or month == "february":
    print ("the season is Winter")
elif month == "march" or month == "april" or month == "may":
    print ("the season is Spring")
elif month == "june" or month == "july" or month == "august":
    print ("the season is Summer")
else:
    print ("enter the correct month in full e.g September")


#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_name = input("Enter fruit name: ")

if fruit_name in fruits:
    print ("That fruit already exist in the list")
else:
    fruits.append(fruit_name)
    print(fruits)

#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
person= {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }


if "skills" in person:
#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
    person["skills"].sort()
    middle = int(len(person["skills"])/2)
    middle= person["skills"][middle]
#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
    python_exists = "Python" in person["skills"]
    print(middle)
    print(python_exists)

#If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

what_skill = input("Enter your skills (separated by commas): ")
skills = what_skill.split(',')
cleaned = [skill.strip().capitalize() for skill in skills]
# cleaned = [skill[0].strip(), skill[1].strip(), skill[2].strip()]

print(skills)
person["skills"] = cleaned
print(person['skills'])

if "JavaScript" in person["skills"] and  "React" in person["skills"]:
    print("He is a frontend developer")
elif "Node" in person["skills"] and  "Python" in person["skills"] and "MongoDB" in person["skills"]:
    print("He is a backend developer")
elif "React" in person["skills"] and  "Node" in person["skills"] and "MongoDB" in person["skills"]:
    print("He is a fullstack developer")
else:
    print("unknown title")

#If the person is married and if he lives in Finland, print the information in the following format:

first_nam = input("What is your first name? ").capitalize()
last_nam = input("What is your last name? ").capitalize()
what_country = input("What is your country? ").capitalize()
Marital_status = input("Are you married ").lower()
check_married = Marital_status in ["yes", "y", "true", "1"]

person['first_name'] = first_nam
person['last_name'] = last_nam
person['is_married'] = check_married

if person["is_married"] == True and person["country"] == "Finland":
    print(person["first_name"] + " lives in " + person["country"] + "." + " He is married")
