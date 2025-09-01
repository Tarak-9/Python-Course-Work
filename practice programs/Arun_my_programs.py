def guess_the_number_program():
    print("🧠 Program: Guess the Number Game\n")

    print("📄 Code:")
    print('''\
import random

def guess_number():
    number = random.randint(1, 10)
    guess = None
    while guess != number:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct! You guessed it.")''')

    print("\n🧪 Test Cases:")
    print("Manual play: Try entering numbers until you guess correctly.")

    print("\n📝 Explanation:")
    print("1. A random number between 1 and 10 is generated.")
    print("2. The user guesses until they match the number.")
    print("3. Hints are given if the guess is too high or low.")


def simple_calculator_program():
    print("🧠 Program: Simple Calculator\n")

    print("📄 Code:")
    print('''\
def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"''')

    print("\n🧪 Test Cases:")
    print("calculator(5, 3, '+') → 8")
    print("calculator(10, 2, '/') → 5.0")
    print("calculator(8, 0, '/') → 'Error: Division by zero'")

    print("\n📝 Explanation:")
    print("Performs basic arithmetic based on the given operator.")


def operators_examples_program():
    print("🧠 Program: Operators Examples (6 types)\n")

    print("📄 Code:")
    print('''\
def operators_demo(a, b):
    return {
        "Addition": a + b,
        "Subtraction": a - b,
        "Multiplication": a * b,
        "Division": a / b if b != 0 else "undefined",
        "Modulus": a % b if b != 0 else "undefined",
        "Exponentiation": a ** b
    }''')

    print("\n🧪 Test Cases:")
    print("operators_demo(5, 2) → {'Addition': 7, 'Subtraction': 3, 'Multiplication': 10, 'Division': 2.5, 'Modulus': 1, 'Exponentiation': 25}")

    print("\n📝 Explanation:")
    print("Demonstrates six different arithmetic operators in Python.")


def admin_password_program():
    print("🧠 Program: Admin Password Check\n")

    print("📄 Code:")
    print('''\
def check_admin_password(password):
    ADMIN_PASS = "admin123"
    return password == ADMIN_PASS''')

    print("\n🧪 Test Cases:")
    print("check_admin_password('admin123') → True")
    print("check_admin_password('wrong') → False")

    print("\n📝 Explanation:")
    print("Checks if the entered password matches the predefined admin password.")


def frequency_counter_program():
    print("🧠 Program: Frequency Counter\n")

    print("📄 Code:")
    print('''\
from collections import Counter

def frequency_counter(items):
    return dict(Counter(items))''')

    print("\n🧪 Test Cases:")
    print("frequency_counter([1, 2, 2, 3, 3, 3]) → {1: 1, 2: 2, 3: 3}")
    print("frequency_counter('hello') → {'h': 1, 'e': 1, 'l': 2, 'o': 1}")

    print("\n📝 Explanation:")
    print("Uses Python's Counter to count the frequency of each element.")


def shopping_cart_program():
    print("🧠 Program: Shopping Cart Total\n")

    print("📄 Code:")
    print('''\
def shopping_cart(cart):
    total = sum(price * qty for item, price, qty in cart)
    return total''')

    print("\n🧪 Test Cases:")
    print("shopping_cart([('Apple', 2, 3), ('Banana', 1, 5)]) → 11")

    print("\n📝 Explanation:")
    print("Calculates the total cost by multiplying price and quantity for each item.")


def vowel_replacer_bot_program():
    print("🧠 Program: Vowel Replacer Bot\n")

    print("📄 Code:")
    print('''\
def replace_vowels(text, replacement='*'):
    vowels = "aeiouAEIOU"
    return ''.join(replacement if ch in vowels else ch for ch in text)''')

    print("\n🧪 Test Cases:")
    print("replace_vowels('Hello World') → 'H*ll* W*rld'")
    print("replace_vowels('Python', '#') → 'Pyth#n'")

    print("\n📝 Explanation:")
    print("Replaces all vowels in the given text with a replacement character.")


def student_marks_program():
    print("🧠 Program: Student Marks Average & Grade\n")

    print("📄 Code:")
    print('''\
def student_marks(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        grade = 'A'
    elif avg >= 75:
        grade = 'B'
    elif avg >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return avg, grade''')

    print("\n🧪 Test Cases:")
    print("student_marks([90, 85, 88]) → (87.67, 'B')")
    print("student_marks([40, 50, 45]) → (45.0, 'F')")

    print("\n📝 Explanation:")
    print("Calculates the average of marks and assigns a grade based on it.")

def number_pattern_program():
    print("🧠 Program: Number Pattern\n")

    print("📄 Code:")
    print('''\
def number_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()''')

    print("\n🧪 Test Cases:")
    print("number_pattern(5) →\n1\n1 2\n1 2 3\n1 2 3 4\n1 2 3 4 5")

    print("\n📝 Explanation:")
    print("1. Outer loop controls the rows.")
    print("2. Inner loop prints numbers from 1 to the current row number.")
    print("3. A newline is printed after each row.")


def star_letter_z_program():
    print("🧠 Program: Print Letter 'Z' Using Stars\n")

    print("📄 Code:")
    print('''\
def print_letter_z(size):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or i + j == size - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()''')

    print("\n🧪 Test Cases:")
    print("print_letter_z(5) →\n*****\n   *\n  *\n *\n*****")

    print("\n📝 Explanation:")
    print("1. Top and bottom rows are filled with '*'.")
    print("2. The diagonal from top-right to bottom-left is also filled.")
    print("3. All other positions are spaces to form the letter 'Z'.")
