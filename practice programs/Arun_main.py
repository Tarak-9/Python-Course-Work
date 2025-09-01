# main.py

import Arun_my_programs as mp

def main():
    programs = {
        1: mp.guess_the_number_program,
        2: mp.simple_calculator_program,
        3: mp.operators_examples_program,
        4: mp.admin_password_program,
        5: mp.frequency_counter_program,
        6: mp.shopping_cart_program,
        7: mp.vowel_replacer_bot_program,
        8: mp.student_marks_program,
        9: mp.number_pattern_program,
        10: mp.star_letter_z_program
    }

    while True:
        print("\n📜 Program Menu:")
        for num, func in programs.items():
            print(f"{num}. {func.__name__.replace('_', ' ').title()}")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == "0":
            print("Exiting...")
            break
        elif choice.isdigit() and int(choice) in programs:
            print("\n" + "="*50)
            programs[int(choice)]()
            print("="*50)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
