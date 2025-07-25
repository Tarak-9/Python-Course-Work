n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
    print(f'{i}*{fact}')
    fact=fact*i
    print(fact)
