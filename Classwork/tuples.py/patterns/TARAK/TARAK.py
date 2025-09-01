name = "TARAK"

# Print each row (0 to 4) for all letters
for i in range(5):  # 5 rows per letter
    line = ""
    for char in name:
        pattern = letters.get(char.upper(), ["     "]*5)  # default blank if letter not found
        line += pattern[i] + "  "  # Add spacing between letters
    print(line)
