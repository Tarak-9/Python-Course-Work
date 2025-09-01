'''class shopping:
   discount = 10

   def product(self,price,name):
      self.price=price
      self.name=name


user1=shopping()
user2=shopping()

user1. product(34000,'Laptop')
user2. product(56000,'phone')

print(shopping.discount)
shopping.discount = 15
print(shopping.discount)
print(user1.price)'''


'''class Login:

   def password(self, password):
           self.password=password
   def updatepassword(self, new_password):
           self.password=new_password
   def display(self):
           print(self.password) 

dinesh = Login()
sanjay = Login()

dinesh.password("Dinesh123")
dinesh.display()'''


'''class Book:
    def __init__ (self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def display(self):
        print("Book Details:".center(50,'*'))
        print(f"Book Title:{self.title}\n Book Author:{self.author}\n Book Price:${self.price}\n")

b=Book('TARAK','MYSELF',999)

b.display()'''

'''class Car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
        self.odometer=0

    def drive(self, distance):
        self.odometer += distance

    def show_odometer(self):
        print(f"Odometer :{self.odometer} distance")


car1=Car("Benz","GLD300")
car1.drive(80)
car1.drive(30)
car1.show_odometer

car1.show_odometer()'''



'''class Movie:
    def __init__(self,name,genre,rating):
        self.name=name
        self.genre=genre
        self.rating=rating

    def is_suitable(self):
        if self.rating < 12:
            print(f"{self.name} is Suitable")
        else:
            print(f"{self.name} is not suitable")
    
m1=Movie("DEVARA","Action",  9)

m1.is_suitable()'''

'''class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def discount(self,percent):
        self.price-=self.price*(percent/100)

    def show_price(self):
        print(f"Discounted Price:{self.price}")

p1=Product("SmartPhone",25000)
p1.discount(20)
p1.show_price()'''

'''class Temp:
    def __init__(self,celsius):
        self.celsius= celsius

    def  fahrenheit(self):
        return (self.celsius*9/5 )+32
    
    def to_celsius(self,fahrenheit):
        return(fahrenheit- 32)*5/9
    
temp=Temp(30)
print("Fahrenheit:",temp.fahrenheit())
print("Celsius from 98F:",temp.to_celsius(98))'''

'''class Item:
    def __init__(self,name,quantity):
        self.name=name
        self.quantity=quantity

    def update_quantity(self, amount):
        self.quantity +=amount

    def display(self):
        print(f"{self.name}:{self.quantity} in stock")

item=Item("Smart Phone",80)
item.update_quantity(-10)
item.display()''' 







