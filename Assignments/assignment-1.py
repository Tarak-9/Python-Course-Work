pizza_id = input(f"Enter Pizza ID: ")
customer_name=input("enter customer name: ")
customer_number=int(input("Enter customer number: "))
pizza_name = str(input(f"Enter Pizza Name: "))
price = float(input(f"Enter Price (INR): "))
pizza_type = str(input(f"Enter Pizza Type (e.g., Veg/Non-Veg): "))
size = (input(f"Enter Size (e.g., Small/Medium/Large): "))
toppings = list(input(f"Enter Toppings (comma-separated): ").split(','))
crust_type = str(input(f"Enter Crust Type (e.g., Cheese Burst, Thin Crust): "))
coupons=int(input("enter the number of coupons: "))
available_discount=int(input("enter number of available discount: "))
discount_details=(coupons,available_discount)
discount_percentage = float(input(f"Enter Discount Percentage(e.g.,10%): "))
payment=input("Payment will be Online or cash: ")
order_details={
    'Customer ordered' : pizza_name,
    'Customer toppings' : toppings,
    'Payment' : payment
}

#output
print('\nOutput:\n')

#Using Comma Separation (sep=',')
print("pizza_id, customer_name, customer_number: "+ str(pizza_id), customer_name, customer_number, sep=',')

#Using Percentage Formatting (% operator)
print("discount_Percentage: %.2f%%" % discount_percentage)

#using f-strings(f"")
print(f"Customer name:{customer_name} \nContact No: {customer_number}\nPrice:₹{price} \nDiscount Percentage: {discount_percentage}% ")


#using.format()
print("Order Details: Customer ordered - {}, Customer toppings -{},bill payment".format(order_details['Customer ordered'],order_details["Customer toppings"],order_details["Payment"]))






