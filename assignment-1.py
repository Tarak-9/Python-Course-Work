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






'''Enter Pizza ID: 1021
enter customer name: mohith
Enter customer number: 1234567891
Enter Pizza Name: chicken
Enter Price (INR): 200
Enter Pizza Type (e.g., Veg/Non-Veg): non-veg
Enter Size (e.g., Small/Medium/Large): large
Enter Toppings (comma-separated): onion,cheese
Enter Crust Type (e.g., Cheese Burst, Thin Crust): cheese burst
enter the number of coupons: 2
enter number of available discount: 2
Enter Discount Percentage(e.g.,10%): 20
Payment will be Online or cash: online

Output:

pizza_id, customer_name, customer_number: 1021,mohith,1234567891
discount_Percentage: 20.00%
Customer name:mohith 
Contact No: 1234567891
Price:₹200.0 
Discount Percentage: 20.0% 
Order Details: Customer ordered - chicken, Customer toppings -['onion', 'cheese'],bill payment
