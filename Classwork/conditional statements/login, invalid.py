data={
'prasanth@gmail.com':'123@',
'Dinesh@gmail.com':'789',
'Sanjay@gmail.com':'456',
}


email,pwd=input("Enter the email and pwd:").split()
if data.get(email)== pwd:
    print('login successful')
else:
    print('Invalid Login')



#Enter the email and pwd:prasanth@gmail.com  123@
#login successful
#Enter the email and pwd: tarak@gmail.com  777@
#Invalid Login
