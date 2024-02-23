import random
small_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
           'o','p','q','r','s','t','u','v','w','x','y','z']
capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
                   'O','P','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['@','#','$','&','*','(',')','!']
print("Welcome to password generator")
length =int(input("length of password:\n"))
n_small_letters=int(input("How many small letters you want in your password?\n"))
n_capital_letters=int(input("How many capital letters you want in your password?\n"))
n_numbers=int(input("How many numbers you want in your password?\n"))
n_symbols=int(input("How many symbols you want in your password?\n"))
password_list=[]
for i in range(1,n_capital_letters+1):
    char=random.choice(capital_letters)
    password_list+=char
    
for i in range(1,n_small_letters+1):
    char=random.choice(small_letters)
    password_list+=char

for i in range (1,n_numbers+1):
    char=random.choice(numbers)
    password_list+=char

for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password_list+=char

random.shuffle(password_list)    
password=""
for char in password_list:
    password+=char   
print("Generated password:",password)