salary = float(input())
if salary <= 250000:
  print(" No Tax")
elif salary >  250000 and salary <=500000:
  print(salary*0.05)
elif salary>500000 and salary <= 1000000:
  print(salary*0.02)
elif salary>1000000:
  print(salary*0.03)



  n=int(input())
  total = 0
  for _ in range(n):
    age=int(input())
    if age>=5 and age<= 18:
      total+=100
    elif age>= 19 and age<= 60:
      total += 150
    elif age > 60:
      total+=120
print(total)



units = int(input())
bill=0
if units<=100:
   bill+=units*1.5
elif units>100 and units<=200:
  bill+=150+(units-100)*2.5
elif units>200 and units<=500:
  bill+=400+(units-200)*4
else:
  bill+=1600+



  hours=int(input())
  fee=0

  if hours<=2:
    fee=30
elif hours>2 and hours<24:
    fee=30+(hours-2)*10
elif hours>=24:
    print(200)




name=input()
quantity=int(input())

if quantity==0:
  print("Out of Stock")
elif quantity<0 and quantity<11:
  print("Low Stock")
elif quantity>11 and quantity<50:
  print("In Stock")
else quantity>50:
  print("OverStocked")



n=int(input())

for row in range(n):
  for col in range(n):

    print((row+col)%2,end=' ')
  print()


  ch=int(input())
  ppl=int(input())
  if ch==1:
    print(ppl*500)
  elif ch==2:
    print(ppl*1300)
  elif ch==3:
    print(ppl*5000)





total=float(input())
if total<1000:
  print(total)
elif total<999 and total<5000:
  print(total-total*0.05)
elif total>4999 and total<10000:
  print(total-total*0.01)
elif total>=10000:
  print(total-total*0.15)


  pin=1234
  for _ in range(3):
     epin=int(input())
     if epin == pin:
           print("Acess Granted")
           break
     else:
       print("ATM Blocked.Please Try Again Later")


total_seats=int(input())
booked_seats=list(map(int,input().split()))
print(f'Total Seats:{total_seats}')
print(f'Booked Seats:{len(booked_seats)}')
print(f'Available:{total_seats-len(booked_seats)}')
    

