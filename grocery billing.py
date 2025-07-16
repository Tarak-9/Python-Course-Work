products = {
    1: ["Rice", 60],
    2: ["Wheat Flour", 45],
    3: ["Sugar", 40],
    4: ["Milk", 25],
    5: ["Eggs (12 pcs)", 70],
    6: ["Cooking Oil", 130],
    7: ["Tea Powder", 90],
    8: ["Salt", 20],
    9: ["Bread", 30],
    10: ["Soap", 25]
}

print("------ Welcome to Grocery Store ------")
print("Here are the available products:\n")
print("Index\tProduct\t\t\tPrice (Rs.)")
for i in products:
    name = products[i][0]
    price = products[i][1]
    if len(name) < 8:
        print(i, "\t", name, "\t\t\t", price)
    elif len(name) < 16:
        print(i, "\t", name, "\t\t", price)
    else:
        print(i, "\t", name, "\t", price)

print("\nEnter the product indexes you want to buy (you can repeat indexes)")
index_list = list(map(int, input("Enter indexes (e.g. 1 2 2 5): ").split()))

cart = {}  # key: product index, value: quantity
i = 0
while i < len(index_list):
    index = index_list[i]
    if index in products:
        if index in cart:
            cart[index] = cart[index] + 1
        else:
            cart[index] = 1
    else:
        print("Invalid product index:", index)
    i = i + 1

print("\n-------- Your Bill --------")
print("Product\t\tQty\tPrice\tTotal")
total = 0

for index in cart:
    name = products[index][0]
    price = products[index][1]
    qty = cart[index]
    subtotal = price * qty
    total = total + subtotal

    if len(name) < 8:
        print(name, "\t\t", qty, "\t", price, "\t", subtotal)
    elif len(name) < 16:
        print(name, "\t", qty, "\t", price, "\t", subtotal)
    else:
        print(name, "", qty, "\t", price, "\t", subtotal)

print("\nTotal Amount to Pay: Rs.", total)
print("Thank you for shopping with us!")
