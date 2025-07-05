#Create an empty tuple
empty_tuple = ()
print(empty_tuple)

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters_tuple = ("Denise", "Joy")
brothers_tuple = ("Cletus", "James" )

#Join brothers and sisters tuples and assign it to siblings
siblings = sisters_tuple + brothers_tuple
print(siblings)

#How many siblings do you have?
print (len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings.append("Father")
siblings.append("Mother")
siblings = tuple(siblings)
family_members = siblings
print(family_members)

#Unpack siblings and parents from family_members
first_sibling, second_sibling, third_sibling, fourth_sibling,  *rest = family_members
print(first_sibling)
print(second_sibling)
print(rest)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "banana", "orange")
vegetables = ("spinach", "tomato", "pepper")
animal = ("dog", "cat", "elephant")
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_lt.sort()
print(food_stuff_lt)
middle_lst = food_stuff_lt[int(len(food_stuff_lt)/2)]
print(middle_lst)

#Slice out the first three items and the last three items from food_staff_lt list
first_three_lst = food_stuff_lt[:3]
last_three_lst = food_stuff_lt[-3:]
print(first_three_lst)
print(last_three_lst)

#Delete the food_staff_tp tuple completely
del food_stuff_tp

#Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)

#Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)


