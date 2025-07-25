items=['coffee','ice cream', 'samosa', 'idly']
stocks=[20,50,40,0]
distance=[13,4,9,12]
rating=[3.2,4.4,4.3,1]
cost=[150,60,20,40]
veg=[True,True,False,True]
time=[40,10,25,15]


data=input("Enter the item: ")
ind=items.index(data)
if distance[ind]<5 and rating[ind]>4 and cost[ind]<500 and veg[ind] and time[ind]
      print('time,veg,cost ,distance and rating applied')
elif distance[ind]<5 and rating[ind]>4 and cost[ind]<500 and veg[ind]:
       print('veg,cost ,distance and rating applied')
elif distance[ind]<5 and rating[ind]>4 and cost[ind]<500:
        print('cost ,distance and rating applied ')
elif distance[ind]<5 and rating[ind]>4:
    print('distance and rating applied)
elif distance[ind]>4:
    print('Rating applied')
elif  cost[ind]<500:
    print('cost applied')
elif
