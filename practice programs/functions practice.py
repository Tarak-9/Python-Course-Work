'''def add(a,b):
    return a+b

print(f"The sum of:{add(5,10)}")'''


'''def square(a):
    return a**2

print( square(6))'''

'''def squares(a,b):
    return (a*a,b*b)

print(squares(8,9))'''    


'''def area(r):
    return 3.14*r*r

print(area(4))'''


'''def greet(name):
    print(f"Hello {name}")

name=input()
greet(name)'''


'''def temp(celsius):
    return celsius * 9/5 + 32
celsius = float(input())
print(f"Temperature in Fahreinheit:{temp(celsius)}")'''



'''def mul(a,b,c):
    return a*b*c

a,b,c=list(map(int,input().split()))

print(mul(a,b,c))

print(f"multiplication of:{mul(4,5,6)}")'''

'''def interest(p,t,r):
    return p*t*r/100

p,t,r=tuple(map(int,input().split(',')))
print(interest(p,t,r))'''


'''def length(s):
    l=0
    for i in s:
        l += 1
    return l

s = input()
print(length(s))'''


'''def double(l):
    for i in range(len(l)):
      l[i]=l[i]*2
    return l  
 
l = list(map(int,input().split()))
print(double(l))'''

'''def double(l):
    res=[]
    s=set()
    for i in l:
        if i not in s:
            res.append(i*2)
            s.add(i)
    return res


l=list(map(int,input().split()))
print(double(l))'''


'''def removei(l,val):
    while val in l:
        l.remove(val)
    return l

l=list(map(int,input().split()))
val=int(input())
print(removei(l,val))'''


'''from itertools import combinations,permutations
from collections import deque

print(list(combinations([1,2,3,4,5,6,7,8,9],4)))
print(list(permutations([1,2,3,4,5,6,7,8,9],5)))'''


'''from itertools import combinations,permutations
from collections import deque

l=[3,4,5,1,2]
res=list(combinations([1,2,3,4,5],3))
k=6
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        print(l[i],l[j])'''

'''from collections import deque

l=[1,2,3,4,5,6,7,8]
d=deque(l)

print(d)

print(d.pop())
d.append(7)
print(d)
print(d.popleft())
d.appendleft(12)
print(d)
print(d.pop())
d.append(15)
print(d)'''
  