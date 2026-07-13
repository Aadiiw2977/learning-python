import random
import string

print("╔══════════════════════════════════════╗")
print("║      AADIIW PASSWORD GENERATOR       ║")
print("║      Python Security Toolkit         ║")
print("╚══════════════════════════════════════╝")

length = int(input("\nPASSWORD LENGTH > "))

characters = string.ascii_letters + string.digits + "!@#$%^&*"

password = ""

for i in range(length):
    password += random.choice(characters)

print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("GENERATED PASSWORD")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(password)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
