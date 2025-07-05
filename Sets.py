#Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update(["YouTube", "MTN"])
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.discard("YouTube")
print(it_companies)

#Join A and B
C = A.union(B)
print(C)

#Find A intersection B
D = A.intersection(B)
print(D)

#Is A subset of B
E = A.issubset(B)
print(E)

#Are A and B disjoint sets
F = A.isdisjoint(B)
print(F)

#Join A with B and B with A
A.update(B)
print(A)
B.update(A)
print(B)

#What is the symmetric difference between A and B
sym_diff = A.symmetric_difference(B)
print(sym_diff)

#Delete the sets completely
del A
del B
del it_companies

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(age_set)
print(len(age_set) >= len(age))

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
unique_words = "I am a teacher and I love to inspire and teach people."
print(set(unique_words.split()))
print(len(unique_words.split()))