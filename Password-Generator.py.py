import string
import random
p1 = string.ascii_lowercase
p2=string.ascii_uppercase
p3=string.digits
p4=string.punctuation
# combine all characters
password_letters = list(p1+p2+p3+p4)
password_len = int(input("Enter the length of your password : "))
if password_len<=0:
    print("Password length must be greater than 0.")
else:
    random.shuffle(password_letters)


password_generator = "".join(password_letters[0:password_len])
print("Your Generated Password is :", password_generator)


