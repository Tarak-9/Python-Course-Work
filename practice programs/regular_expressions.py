'''import re
res = re.split(r'[,:/0;]','dinesh,sanjay;jaswanth/mohith0tarak')
print(res)'''


'''import re 
text = 'Java Programming Language'
res =re.sub(r'[A-Z]','*',text)

print(res)'''


import re
text='Sanjay is a good boy.He lives in KPHB.He loves food.Heart Hacker sanjay.Sanjay mobile no 9876543210.Everyone loves sanjay.'
res=re.findall(r'A-Za-z0-9')


def validate_name(name):
    pattern = r'^[A-Za-z] {2,25} ( [A-Za-z] {2,25})+$'
    return bool(re.fullmatch(pattern, name))

def validate_email(email):
    pattern = r'^[a-z0-9._]+@[a-z.-]+\.[a-z]{2,3}$'
    return bool(re.fillmatch(pattern, email))

def validate_phone(phone):
    pattern = r'^(?:\=91|0)?[6-9]\d{9}$'
    return bool(re.fullmatch(pattern, phone))

def validate_password(password):
    pattern=r'^(?=.*[A-Z]) (?=.*[a-z])(?=.*\d)(?=.*[@$!%?&_-]) [A-Za-z\d@$!%*?&]{8, }$'
    return bool(re,fullmatch(pattern, password))

def validate_username(username):
    pattern=r'^[A-Za-z0-9](5,15)$'
    return bool(re,fullmatch(pattern, username))
