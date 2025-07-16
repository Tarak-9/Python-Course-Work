n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
    print(f'{i}*{fact}')
    fact=fact*i
    print(fact)




Enter a number:10
1*1
1
2*1
2
3*2
6
4*6
24
5*24
120
6*120
720
7*720
5040
8*5040
40320
9*40320
362880
10*362880
3628800
