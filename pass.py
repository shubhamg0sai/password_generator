import random 
import string

print("""
    ======================
    | Password Generator |
    ======================
""")
#Taking input for the length of password
lgth = int(input("Enter the password length: \n"))

#getting the lowecases in ASCII table
low = string.ascii_lowercase

#getting the uppercases in ASCII table
up = string.ascii_uppercase

#getting the punctuations in ASCII table
syb = string.punctuation

#getting the numbers in ASCII table
n = string.digits

#adding them to form a password
add = low + up + syb + n

#returns the length of string 
tmp = random.sample(add,lgth)

#using the join method
pwd = "".join(tmp)

#Printing the ouput
print(f'Your Random password is {pwd}')
