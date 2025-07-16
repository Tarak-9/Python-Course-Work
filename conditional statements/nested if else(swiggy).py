items=['coffee','ice cream', 'samosa', 'idly']
stocks=[20,50,40,0]
data=input("Enter the item: ")

if data in items:
    
    ind=items.index(data)
    if stocks[ind]>0:
        print("Availiable")
    else:
        print(' out of stock.please try again ')
else:
    print('Item not availiable')
    


#Enter the item: coffee
#Availiable


#Enter the item: Tea
#Item not availiable


#Enter the item: idly
#out of stock.please try again 
