num=input("Enter the number:")
vol='aeiouAEIOU'

for i in num:
    if i in vol:
        print('vowels')
    else:
        print('consonants')
