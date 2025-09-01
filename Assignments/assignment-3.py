def ask_question(ques_num, question, options, correct_answer):
    print(f"\nQuestion {ques_num}: {question}")
    for key in options:
        print(f"{key}: {options[key]}")
    answer = input("Your Answer (A/B/C/D): ").strip().upper()
    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"Wrong! The correct answer is '{correct_answer}'")
        return 0

def run_quiz():
    score = 0

    questions = [
        ("Which Python error is shown for infinite recursion",
         {'A': "MemoryError", 'B': "RecursionError", 'C': "NameError", 'D': "ValueError"}, 'B'),

        ("Which operation rebinds the local reference?",
         {'A': ".append()", 'B': "=+= with int", 'C': "del", 'D': "x = 10"}, 'D'),

        ("What does a return statement do in a function?",
         {'A': "Starts the function", 'B': "Skips the function", 'C': "Terminates and sends back a value", 'D': "Assigns a new function"}, 'C'),

        ("What does the continue statement do in a loop?",
         {'A': "Exits the loop entirely", 'B': "Skips the current iteration", 'C': "Pauses the loop", 'D': "Repeats the loop"}, 'B'),

        ("Which one is incorrect?",
         {'A': "def greet(name=\"Guest\")", 'B': "def sum(x=5, y):", 'C': "def hello(name=\"Hi\")", 'D': "def login(user=\"admin\")"}, 'B'),

        ("What can a user-defined function contain?",
         {'A': "Only loops", 'B': "Only print statements", 'C': "Statements to perform a task", 'D': "Only return statements"}, 'C'),

        ("What is recursion in Python?",
         {'A': "A type of loop", 'B': "A function that calls itself", 'C': "A module import", 'D': "A built-in library"}, 'B'),

        ("Which types are mutable in Python?",
         {'A': "Lists", 'B': "Tuples", 'C': "Strings", 'D': "Integers"}, 'A'),

        ("Which of the following is a built-in function?",
         {'A': "sum_numbers", 'B': "custom_add()", 'C': "multiply_list()", 'D': "print()"}, 'D'),

        ("What is Pass by Reference?",
         {'A': "Reference of variable is passed", 'B': "Only values are copied", 'C': "Pointers are ignored", 'D': "Variables are deleted"}, 'A'),

        ("Changing a global variable inside a function without `global` keyword will?",
         {'A': "Change global value", 'B': "Throw error", 'C': "Modify local copy", 'D': "Reset variable"}, 'C'),

        ("Can a function have both *args and **kwargs?",
         {'A': "No", 'B': "Yes", 'C': "Sometimes", 'D': "Only if *args comes last"}, 'B'),

        ("Which of the following is a valid user-defined function name?",
         {'A': "1function", 'B': "function#", 'C': "my_function", 'D': "my function"}, 'C'),

        ("What does slicing a list do?",
         {'A': "Modifies it", 'B': "Creates a copy", 'C': "Creates tuple", 'D': "Deletes it"}, 'B'),

        ("Which is true about default arguments?",
         {'A': "Must be passed", 'B': "Must be first", 'C': "Can be skipped", 'D': "Can’t be used with keyword"}, 'C'),

        ("If the function used in filter() always returns False, what will the output be?",
         {'A': "All elements will be removed", 'B': "All elements will be kept", 'C': "Only unique elements will remain", 'D': "It will raise an error"}, 'A'),

        ("What type of data structure does *args store its values in?",
         {'A': "List", 'B': "Dictionary", 'C': "Tuple", 'D': "Set"}, 'C'),

        ("Which type of function is print()?",
         {'A': "User-defined", 'B': "Class method", 'C': "Built-in", 'D': "Global function"}, 'C'),

        ("What is the key difference between break and continue?",
         {'A': "break skips, continue exits", 'B': "break exits, continue skips", 'C': "Both exit the loop", 'D': "Both skip iterations"}, 'B'),

        ("What is result of modifying an integer inside a function?",
         {'A': "Global change", 'B': "Local only", 'C': "Error", 'D': "Prints same value"}, 'B'),
    ]

    print("Welcome to the Python Quiz Game!")

    for i in range(len(questions)):
        q, options, ans = questions[i]
        score += ask_question(i + 1, q, options, ans)

    print(f"\nFinal Score: {score} / {len(questions)}")
    if score == len(questions):
        print("Perfect! Keep It Up!")
    elif score >= 15:
        print("Great job! Almost there!")
    elif score >= 10:
        print(" Good effort! Keep practicing.")
    else:
        print("Review Python basics and try again!")
        
run_quiz()
