import string
import random
length=int(input("enter the length of password"))
if length < 8 or length > 126:
    print("length should be between 8 and 126")
else:
    password_pool=string.ascii_letters+string.digits+string.punctuation
    password_pool=random.sample(password_pool,length)
    password_pool="".join(password_pool)
print(f'Your length is {password_pool}')