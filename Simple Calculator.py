import math

first_num = float (input("Enter first number: "))
second_num = float (input ("Enter second number: "))
what_operation = input ("What operation do you want to perform? (add/subtract/multiply/divide): ")
case_operation = what_operation.lower()

# add = first_num + second_num
# subtract = first_num - second_num
# multiply = first_num * second_num
# divide = first_num / second_num


def addition(first_num1, second_num2):
    add = first_num1 + second_num2
    square_root = round(math.sqrt(add))
    if square_root % 2 == 0:
        result = str(square_root) + " is an even number."
        return result
    else:
        return str(square_root) + " is an odd number."

def subtract(first_num1, second_num2):
    sub = first_num1 - second_num2
    square = sub ** 2
    return square

if case_operation == "add":
    print(addition(first_num, second_num))
elif case_operation == "subtract":
    print(subtract(first_num, second_num))
# elif case_operation == "multiply": print(multiply)
# elif case_operation == "divide":
#     if second_num != 0:
#         print("✅ Result:", first_num / second_num)
#     else:
#         print("⚠️ Cannot divide by zero!")
# else: print("❌ Invalid operation.")


