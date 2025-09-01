def factorial_program():
    print("🧠 Program: Find the Factorial of a Number\n")

    print("📄 Code:")
    print('''\
def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result''')

    print("\n🧪 Test Cases:")
    print("Input:  factorial(0)  → Output: 1")
    print("Input:  factorial(5)  → Output: 120")
    print("Input:  factorial(7)  → Output: 5040")
    print("Input:  factorial(10) → Output: 3628800")

    print("\n📝 Explanation:")
    print("1. This function checks if the input is a non-negative integer.")
    print("2. If the input is valid, it initializes result as 1.")
    print("3. It then multiplies result by all numbers from 2 to n.")
    print("4. The final result is returned as the factorial of n.")

def check_prime_program():
    print("🧠 Program: Check if a Number is Prime\n")

    print("📄 Code:")
    print('''\
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True''')

    print("\n🧪 Test Cases:")
    print("Input: is_prime(7)  → Output: True")
    print("Input: is_prime(10) → Output: False")

    print("\n📝 Explanation:")
    print("A prime number has only two divisors: 1 and itself.")
    print("We check from 2 to √n for any divisors.")


def palindrome_number_program():
    print("🧠 Program: Check Palindrome Number\n")

    print("📄 Code:")
    print('''\
def is_palindrome_number(n):
    return str(n) == str(n)[::-1]''')

    print("\n🧪 Test Cases:")
    print("Input: is_palindrome_number(121) → Output: True")
    print("Input: is_palindrome_number(123) → Output: False")

    print("\n📝 Explanation:")
    print("A palindrome number reads the same backward and forward.")


def armstrong_number_program():
    print("🧠 Program: Check Armstrong Number (3-digit)\n")

    print("📄 Code:")
    print('''\
def is_armstrong(n):
    if not (100 <= n <= 999):
        return False
    return sum(int(digit)**3 for digit in str(n)) == n''')

    print("\n🧪 Test Cases:")
    print("Input: is_armstrong(153) → Output: True")
    print("Input: is_armstrong(123) → Output: False")

    print("\n📝 Explanation:")
    print("Armstrong numbers are equal to the sum of the cubes of their digits.")


def greatest_of_three_program():
    print("🧠 Program: Find Greatest of Three Numbers\n")

    print("📄 Code:")
    print('''\
def greatest(a, b, c):
    return max(a, b, c)''')

    print("\n🧪 Test Cases:")
    print("Input: greatest(5, 12, 9) → Output: 12")
    print("Input: greatest(3, 2, 1) → Output: 3")

    print("\n📝 Explanation:")
    print("The function uses the built-in max() function to find the largest number.")


def count_digits_program():
    print("🧠 Program: Count Digits in a Number\n")

    print("📄 Code:")
    print('''\
def count_digits(n):
    return len(str(abs(n)))''')

    print("\n🧪 Test Cases:")
    print("Input: count_digits(12345) → Output: 5")
    print("Input: count_digits(-789)  → Output: 3")

    print("\n📝 Explanation:")
    print("Convert the number to string (ignoring negative sign) and count the characters.")


def fibonacci_sequence_program():
    print("🧠 Program: Print Fibonacci Sequence (n terms)\n")

    print("📄 Code:")
    print('''\
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence''')

    print("\n🧪 Test Cases:")
    print("Input: fibonacci(5) → Output: [0, 1, 1, 2, 3]")
    print("Input: fibonacci(7) → Output: [0, 1, 1, 2, 3, 5, 8]")

    print("\n📝 Explanation:")
    print("Each number is the sum of the two preceding ones, starting from 0 and 1.")


def palindrome_string_program():
    print("🧠 Program: Check Palindrome String\n")

    print("📄 Code:")
    print('''\
def is_palindrome_string(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]''')

    print("\n🧪 Test Cases:")
    print("Input: is_palindrome_string('Madam')     → Output: True")
    print("Input: is_palindrome_string('Hello')     → Output: False")
    print("Input: is_palindrome_string('nurses run') → Output: True")

    print("\n📝 Explanation:")
    print("The string is converted to lowercase and spaces are removed.")
    print("Then we check if it's equal to its reverse.")

def count_vowels_program():
    print("🧠 Program: Count Vowels in a String\n")

    print("📄 Code:")
    print('''\
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)''')

    print("\n🧪 Test Cases:")
    print("Input: count_vowels('Hello World') → Output: 3")
    print("Input: count_vowels('Python')      → Output: 1")

    print("\n📝 Explanation:")
    print("Iterates through the string and counts characters that are vowels.")

def reverse_string_program():
    print("🧠 Program: Reverse a String\n")

    print("📄 Code:")
    print('''\
def reverse_string(s):
    return s[::-1]''')

    print("\n🧪 Test Cases:")
    print("Input: reverse_string('hello') → Output: 'olleh'")
    print("Input: reverse_string('abc')   → Output: 'cba'")

    print("\n📝 Explanation:")
    print("Uses Python slicing to reverse the string.")