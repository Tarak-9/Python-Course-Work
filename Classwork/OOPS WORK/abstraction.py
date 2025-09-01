from abc import ABC ,abstractmethod

class Upload(ABC):
    @abstractmethod
    def compress(self):
        pass

class Image(Upload):
    def compress(self):
        print("Image is compressed to 2MB")

class Reel(Upload):
    def compress(self):
        print("Reel is compressed to 3MB")

r=Reel()
i=Image()

r.compress()
i.compress()

'''from abc import ABC, abstractmethod


class Booking(ABC):
    @abstractmethod
    def reserved(self):
        pass

class Train(Booking):
    def reserved(self):
        print("Train is Booked ")

class Bus(Booking):
    def reserved(self):
        print("Bus is Booked")

t=Train()
b=Bus()

t.reserved()
b.reserved()'''


'''from abc import ABC,abstractmethod

class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass

class FoodOrder(Order):
    def process_order(self):
        print("Processing Food Order:Check chef availiability,estimate time,serving")

class GroceryOrder(Order):
    def process_order(self):
        print("Processing Grocery Order:Check inventory per item,bag&dispatch,out of delivery")

class MedicineOrder(Order):
    def process_order(self):
        print("Processing Medicine Order:Validate prescription,check expiry date ,delivery")

class CloudKitchenOrder(Order):
    def process_order(self):
        print("Processing CloudKitchen Order:Check availiablity of items")

class TiffinOrder(Order):
    def process_order(self):
        print("Processing Tiffin Order:Check availiability of tiffins ,deliver")

class PetSuppliesOrder(Order):
    def process_order(self):
        print("Processing petsupplies Order:Check pet product categories and grooming products")

class MeatOrder(Order):
    def process_order(self):
        print("Processing Meat Order:Confirm freshness,asign chilled")

class CakeOrder(Order):
    def process_order(self):
        print("Processing Cake Order:Custom baking,time-sensitive packing")

class PartyOrder(Order):
    def process_order(self):
        print("Processing Party Order:Bulk Cooking, team coordination")

class JuiceOrder(Order):
    def process_order(self):
        print("Processing Juice Order:Intermediate prep,cold packaging")

def handle_order(order:Order):
     order.process_order()
     

orders=[
    FoodOrder(),
    GroceryOrder(),
    MedicineOrder(),
    CloudKitchenOrder(),
    TiffinOrder(),
    PetSuppliesOrder(),
    MeatOrder(),
    CakeOrder(),
    PartyOrder(),
    JuiceOrder()
]

for order in orders:
    handle_order(order)'''



'''from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self,amount):
        pass

class CreditCardPayment(Payment):
    def make_payment(self,amount):
        print(f"Paid ${amount} using Credit Card.")

class PayPalPayment(Payment):
    def make_payment(self,amount):
        print(f"Paid ${amount} using PayPAl.")

def process_payment(payment,amount):
    payment.make_payment(amount)


process_payment(CreditCardPayment(),100)
process_payment(PayPalPayment(),200)'''


