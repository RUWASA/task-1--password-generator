import random
import string

def generate_password(length, chars=string.ascii_letters + string.digits + string.punctuation):

  password = ''.join(random.choice(chars) for _ in range(length))
  return password

# Get user input for password length
length = int(input("Enter the desired password length: "))

# Generate and print the password
password = generate_password(length)
print("Generated Password:", password)

