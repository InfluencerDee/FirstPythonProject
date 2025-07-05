#Create an empty dictionary called dog
dog = {}
print(type(dog))

#Add name, color, breed, legs, age to the dog dictionary
dog = {"name": "Hera", "color": "white", "breed": "Lhasa", "legs": 4, "age": 2}
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {"first_name": "Denise", "last_name": "Smith", "gender": "Female", "age": 18, "marital_status": False, "skills": ["literacy", "typing", "drawing"], "country": "USA", "City": "New York", "address": "NO 4 Ring Road"}
print(student)

#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
print(student["skills"])
print(type(student["skills"]))

#Modify the skills values by adding one or two skills
student["skills"].append("Python")
print(student)

#Get the dictionary keys as a list
student_keys = student.keys()
print(student_keys)

#Get the dictionary values as a list
students_values = student.values()
print(students_values)

#Change the dictionary to a list of tuples using items() method
print(student.items())

#Delete one of the items in the dictionary
student.pop("City")
print(student)

#Delete one of the dictionaries
del dog