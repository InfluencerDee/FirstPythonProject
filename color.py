import string
import random


def random_user_id():
    user_id_length = 6
    all_user_id = string.ascii_letters + string.punctuation + string.digits
    new_user_id = ""
    for i in range(user_id_length):
        new_user_id += random.choice(all_user_id)
    return new_user_id
print(random_user_id())

def user_id_gen_by_user():
    all_user_id = string.ascii_letters + string.punctuation + string.digits
    user_id_char = int (input("Enter number of characters: "))
    user_id_num = int (input("Enter number of IDs: "))
    for _ in range(user_id_num):
        new_user_id = ""
        for _ in range(user_id_char):
            new_user_id += random.choice(all_user_id)
        print (new_user_id)
print(user_id_gen_by_user())

#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    for _ in range(0, 255):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
    return r, g, b
print(rgb_color_gen())
#
# #Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors (n):
    hexa_colors = []
    for _ in range(n):
        color = "#"
        for _ in range(6):
            color += random.choice('0123456789abcdef')
        hexa_colors.append(color)
    return hexa_colors
print(list_of_hexa_colors(6))

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(n):
    rgb_colors = []
    for i in range(n):

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = f"rgb({r}, {g}, {b})"
        rgb_colors.append(color)
    return rgb_colors
print(list_of_rgb_colors(3))





