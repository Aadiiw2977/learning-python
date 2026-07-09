import random
import string

print("━━━━━━━━━━━━━━━━━━━━")
print("🔐 PASSWORD GENERATOR")
print("━━━━━━━━━━━━━━━━━━━━")

length = int(input("Password Length: "))

characters = string.ascii_letters + string.digits + "!@#$%^&*"

password = ""

for i in range(length):
    password += random.choice(characters)

print()
print("✅ Your Password:")
print(password)
