rows = 5  # You can change the height if needed

# Function to print one row of 'T'
def print_T_row(i):
    for j in range(rows):
        if i == 0:
            print("*", end="")  # Top horizontal line
        elif j == rows // 2:
            print("*", end="")  # Center vertical line
        else:
            print(" ", end="")

def print_R_row(i):
    for j in range(rows):
        if j == 0:
            print("*", end="")  # Left vertical line
        elif (i == 0 or i == rows // 2) and j < rows - 1:
            print("*", end="")  # Top and middle horizontal lines
        elif j == rows - 1 and i != 0 and i < rows // 2:
            print("*", end="")  # Right vertical curve
        elif i - j == 1 and i > rows // 2:
            print("*", end="")  # Diagonal leg
        else:
            print(" ", end="")

# Function to print one row of 'A'
def print_A_row(i):
    for j in range(rows * 2 - 1):
        if j == rows - 1 - i or j == rows - 1 + i:
            print("*", end="")  # Left and right diagonals
        elif i == rows // 2 and (j > rows - 1 - i and j < rows - 1 + i):
            print("*", end="")  # Horizontal bar in the middle
        else:
            print(" ", end="")

def print_K_row(i):
    for j in range(rows):
        if j == 0:
            print("*", end="")  # Left vertical line
        elif j == rows - 2 - i:
            print("*", end="")  # Upper diagonal
        elif i >= rows // 2 and j == i - (rows // 2) +1:
            print("*", end="")  # Lower diagonal
        else:
            print("  ", end="")

# Print both T and A side by side row by row
for i in range(rows):
    print_T_row(i)
    print("   ", end="")
    print_A_row(i)
    print("   ", end="")
    print_R_row(i)
    print("   ", end="")
    print_A_row(i)
    print("   ", end="")
    print_K_row(i)
    print()
