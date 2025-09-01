class number:
   def __init__(self,n):
      self.n=n

   def __add__(self,other):
      return self.n+other.n
   def __sub__(self,other):
      return self.n-other.n
   def __mul__(self,other):
      return self.n*other.n
   def __str__(self):
      return f"{self.n}"
   def __lt__(self,other):
      return self.n<other.n
   def __gt__(self,other):
      return self.n>other.n


number1=number(10)
number2=number(20)

print(number1+number2)
print(number1-number2)
print(number1*number2)
print(number1)
print(number1<number2)
print(number1>number2)

