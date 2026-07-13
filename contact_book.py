contacts = {}

BANNER = """
╔══════════════════════════════════════════════╗
║         AADIIW CYBER CONSOLE v1.0           ║
║      Ethical Cybersecurity Portfolio        ║
╚══════════════════════════════════════════════╝
"""

while True:
    print(BANNER)
    print("[01] ➜ Add Contact")
    print("[02] ➜ View Contacts")
    print("[03] ➜ Search Contact")
    print("[04] ➜ Delete Contact")
    print("[05] ➜ About")
    print("[00] ➜ Exit")

    choice = input("\nSYSTEM > ")

    if choice == "1":
        name = input("CONTACT NAME  > ")
        number = input("PHONE NUMBER  > ")
        contacts[name] = number
        print("\n[✓] Contact saved successfully.\n")

    elif choice == "2":
        if contacts:
            print("\n========== CONTACT DATABASE ==========")
            for name, number in contacts.items():
                print(f"• {name} : {number}")
            print("======================================")
        else:
            print("\n[!] Database is empty.\n")

    elif choice == "3":
        name = input("SEARCH NAME > ")
        if name in contacts:
            print(f"\n[FOUND] {name} : {contacts[name]}\n")
        else:
            print("\n[!] Contact not found.\n")

    elif choice == "4":
        name = input("DELETE NAME > ")
        if name in contacts:
            del contacts[name]
            print("\n[✓] Contact deleted.\n")
        else:
            print("\n[!] Contact not found.\n")

    elif choice == "5":
        print("""
═══════════════════════════════════════
 Developer : AADIIW
 GitHub    : Aadiiw2977
 Role      : Python & Cybersecurity Student
 Mission   : Learn • Build • Secure
 Version   : 1.0
═══════════════════════════════════════
""")

    elif choice == "0":
        print("\nSession Closed. Keep Learning. 🚀")
        break

    else:
        print("\n[!] Invalid command.\n")
