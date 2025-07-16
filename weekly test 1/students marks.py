n=int(input())
data={}

for i in range(n):
    name,mark=input().split()
    mark=int(mark)
    data[name]=mark

print(data)
