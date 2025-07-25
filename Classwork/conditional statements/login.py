data={
'prasanth@gmail.com':'123@',
'Dinesh@gmail.com':'789',
'Sanjay@gmail.com':'456',
}


email,pwd=input("Enter the email and pwd:").split()
if email in data and pwd in data[email]:
    print('login successful')
print(email,pwd)




#Enter the email and pwd:prasanth@gmail.com   123@
#login successful
#prasanth@gmail.com 123@
