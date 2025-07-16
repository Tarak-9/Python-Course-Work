credentials=("admin","python123")
username=input()
password=input()
if credentials[0]==username and credentials[1]==password:
        print("Login successful")
else:
        print("Access denied")
