#Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
updated_numbers = [i for i in numbers if i > 0]
print(updated_numbers)

#Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
new_list = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print(new_list)

#Using list comprehension create the following list of tuples:
list_of_tuples = [(x, x**0, x**1, x**2, x**3, x**4, x**5) for x in range(11) ]
print(list_of_tuples)

#Flatten the following list to a new list:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# # for country in countries:
# #     for i, j in country:
# #         result = [i.upper(), i[:3].upper(), j.upper()]
# #         print(result)
# countries_list = [[i.upper(), i[:3].upper(), j.upper()] for country in countries for i, j in country ]
# print(countries_list)

#Change the following list to a list of dictionaries:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# keys = ["country", "city"]
# list_country = []
# for country in countries:
#     for city in country:
#         dict_countries = dict(zip(keys, city))
#         list_country.append(dict_countries)
# print(list_country)

# countries_dict = [dict(zip(keys, city)) for country in countries for city in country ]
# print(countries_dict)

#Change the following list of lists to a list of concatenated strings:
# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# list_names = []
# for name in names:
#     for i in name:
#         string_countries = " ".join(i)
#         list_names.append(string_countries)
# print(list_names)

# names_str = [ " ".join(i) for name in names for i in name]
# print(names_str)

#Write a lambda function which can solve a
def slope():
    return lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

final_slope = slope()
print(final_slope(100, 200, 300, 400))

