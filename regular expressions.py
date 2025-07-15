import re
from collections import Counter


#What is the most frequent word in the following paragraph?
paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
regex_pattern = r'[A-Za-z0-9]+'
matches = re.findall(regex_pattern, paragraph, re.I)
print(matches)
matches_count = {}
for match in matches:
    if match not in matches_count:
        matches_count[match] = 1
    else:
        matches_count[match] += 1
sorted_matches = sorted(matches_count.items(), key=lambda x: x[1], reverse=True)

print(sorted_matches[0])

#Extract these numbers from this whole text and find the distance between the two furthest particles.
txt = ("The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.")
regex_pattern_numbers = r'-?\d+'
points = re.findall(regex_pattern_numbers, txt)
print(points)
sorted_points = list(map(int, points))
print(sorted_points)
distance = sorted_points[-1] - sorted_points[0]
print(distance)

#Write a pattern which identifies if a string is a valid python variable
is_valid_variable_regex = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
def is_valid_variable_name(name):
    return bool(re.match(is_valid_variable_regex, name))
print(is_valid_variable_name("1firstname"))

#Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
clean_text = re.sub(r'[^a-zA-Z\s]', "", sentence).strip()
print(clean_text)
words = clean_text.lower().split()
word_count = Counter(words)
most_common_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))[:3]
print("Top 3 most frequent words:", most_common_words)
