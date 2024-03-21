import random, string

pass_length = int(input("Provide the password length: "))

ch= string.ascii_letters + string.digits + string.punctuation

password = "" 

for index in range(pass_length):
    password = password + random.choice(ch)
print("{}".format(password))
print("Display password:", password)
