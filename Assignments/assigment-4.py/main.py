import my_programs as mp

function_map = {
    1: mp.factorial_program,
    2: mp.check_prime_program,
    3: mp.palindrome_number_program,
    4: mp.armstrong_number_program,
    5: mp.greatest_of_three_program,
    6: mp.count_digits_program,
    7: mp.fibonacci_sequence_program,
    8: mp.palindrome_string_program,
    9: mp.count_vowels_program,
    10: mp.reverse_string_program
}
while True:
    print('''
------ FUNCTION MENU ------
1. Find the Factorial of a number
2. Check if a number is prime number
3. Check if number is a palindrome number
4. Armstrong number program
5. Find greatest of three numbers program
6. Count Digits program
7. Check if fibonacci sequence program
8. Check if a string is palindrome string
9. Count vowels in a string
10. Implement reverse a string program
0. Exit
---------------------------''')
    
    choice = int(input("Enter your choice: "))
    if choice > 0 and choice <= len(function_map):
        function_map[choice]()
    elif choice == 0:
        print("Exiting program. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")