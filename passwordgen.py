import secrets
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbol = "!@#$%^&*"

all_chars = lower + upper + digits + symbol
length = int(input("enter password length:"))

password = [

    secrets.choice(lower),
    secrets.choice(upper),
    secrets.choice(digits),
    secrets.choice(symbol),
]

password+=[secrets.choice(all_chars)
for in range(length-4)]

secrets.system random().shuffle(password)

password="".join (password)
print("secure password:",password)