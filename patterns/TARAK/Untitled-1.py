n=int(input ("Enter the size："))
for row in range (n):
    for col in range(n):
        if row+col==n-1 or row==col:
              print("*"，end=' ')
        else:
              print(' ', end=' ')
    print ()