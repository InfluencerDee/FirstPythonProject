from collections import Counter
import re
import json
from fileinput import filename
from stop_words import stop_words
import csv


#Read obama_speech.txt.txt file and count number of lines and words
with open('obama_speech.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    total_lines = len(lines)

    regex_words = r"\b[a-zA-Z'-]+\b"
    words = re.findall(regex_words, content)
    total_words = len(words)
    print("Total number of lines:", total_lines)
    print("Total number of words:", total_words)

#Read michelle_obama_speech.txt file and count number of lines and words
with open('michelle_obama_speech.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    total_lines = len(lines)
    regex_words = r"\b[a-zA-Z'-]+\b"
    words = re.findall(regex_words, content)
    total_words = len(words)
    print("Total number of lines:", total_lines)
    print("Total number of words:", total_words)

#Read donald_speech.txt file and count number of lines and words
with open('donald_speech.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    total_lines = len(lines)
    regex_words = r"\b[a-zA-Z'-]+\b"
    words = re.findall(regex_words, content)
    total_words = len(words)
    print("Total number of lines:", total_lines)
    print("Total number of words:", total_words)

#Read melina_trump_speech.txt file and count number of lines and words
with open('melina_trump_speech.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    total_lines = len(lines)
    regex_words = r"\b[a-zA-Z'-]+\b"
    words = re.findall(regex_words, content)
    total_words = len(words)
    print("Total number of lines:", total_lines)
    print("Total number of words:", total_words)

#Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

def ten_most_spoken_lang(file_path, top_n):
    with open(file_path, 'r') as f:
        countries = json.load(f)

        lang_count = {}
        for country in countries:
            for lang in country["languages"]:
                if lang not in lang_count:
                    lang_count[lang] = 1
                else:
                    lang_count[lang] += 1
        sorted_top_ten = sorted(lang_count.items(), key=lambda x: (-x[1], x[0]))[:top_n]
        return sorted_top_ten
print(ten_most_spoken_lang('/Users/denise/Desktop/First-Python-Project/countries_data.json', 10))

#Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def ten_most_populated(file_path, top_n):
    with open(file_path, 'r') as f:
        countries = json.load(f)
        population_lst = []
        for country in countries:
            name = country["name"]
            population = country["population"]
            population_lst.append((name, population))

        sorted_pop_dict = sorted(population_lst, key=lambda x: x[1], reverse=True)
        return sorted_pop_dict[:top_n]
print(ten_most_populated('/Users/denise/Desktop/First-Python-Project/countries_data.json', 10))

#Extract all incoming email addresses as a list from the email_exchange_big.txt file.
with open('email_exchanges_big.txt', 'r') as f:
    content = f.read()
regex_for_email = r"(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*" \
          r'|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]' \
          r'|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@' \
          r'(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+' \
          r'[a-zA-Z]{2,}|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}' \
          r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|' \
          r'[a-zA-Z\-0-9]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-' \
          r'\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)])'
regex_email = re.findall(regex_for_email, content)
print(regex_email)

#Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order.
def find_most_common_words(file_path, top_n):
    with open(file_path, 'r') as f:
        content = f.read()
        regex_words = r"\b[a-zA-Z'-]+\b"
        words = re.findall(regex_words, content)
        words_count = Counter(words)
        most_common_words = sorted(words_count.items(), key=lambda x: (-x[1], x[0]))
        return most_common_words[:top_n]
print(find_most_common_words('/Users/denise/Desktop/First-Python-Project/obama_speech.txt', 10))
print(find_most_common_words("/Users/denise/Desktop/First-Python-Project/michelle_obama_speech.txt", 10))
print(find_most_common_words("/Users/denise/Desktop/First-Python-Project/donald_speech.txt", 10))
print(find_most_common_words("/Users/denise/Desktop/First-Python-Project/melina_trump_speech.txt", 10))

#Find the 10 most repeated words in the romeo_and_juliet.txt
with open('romeo_and_juliet.txt', 'r') as f:
    content = f.read()
regex_words = r"\b[a-zA-Z'-]+\b"
words = re.findall(regex_words, content)
words_count = Counter(words)
most_common_words = sorted(words_count.items(), key=lambda x: (-x[1], x[0]))
print(most_common_words[:10])

#Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts.

#Function to clean text (remove punctuation, lowercase)
def clean_txt (text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

#Function to remove stopwords
def remove_support_words (text, stopwords):
    words = text.split()
    return [word for word in words if word not in stopwords]

#Function to calculate similarity between two sets of words
def check_text_similarity(text_1, text_2):
    set1 = set(text_1)
    set2 = set(text_2)
    union_len = len(set1.union(set2))
    if union_len == 0:
        return 0.0
    return len(set1.intersection(set2)) / union_len

with open('michelle_obama_speech.txt', "r") as f:
    michelle_text = f.read()

with open ("melina_trump_speech.txt", "r") as f:
    melina_text = f.read()

michelle_cleaned_txt = clean_txt(michelle_text)
melina_cleaned_txt = clean_txt(melina_text)

michelle_words = remove_support_words(michelle_cleaned_txt, stop_words)
melina_words = remove_support_words(melina_cleaned_txt, stop_words)

similarity_score = check_text_similarity(michelle_words, melina_words)
print(similarity_score)

#Count the number of lines containing python or Python
count = 0
with open("hacker_news.csv", newline='') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        line = "".join(row)
        if re.search(r'\b[Pp]ython\b', line):
            count += 1
print(count)