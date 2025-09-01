def calculate_bmi(weight,height):
 return weight(height*height)

print('%2f'%(calculate_bmi(70,1.75)))
print('%2f%'%(calculate_bmi(90,1.8)))


def filter_even(numbers):
 res=[]
 for i in numbers:
  if i%2==0:
   res.append(1)
 return res
print()
