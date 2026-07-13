import os

while True:
    print("\n━━━━━━━━━━━━━━━━━━━━")
    print("📂 FILE MANAGER")
    print("━━━━━━━━━━━━━━━━━━━━")
    print("1. Create File")
    print("2. Read File")
    print("3. Delete File")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        name = input("File name: ")
        with open(name, "w") as f:
            text = input("Write text: ")
            f.write(text)
        print("✅ File created.")

    elif choice == "2":
        name = input("File name: ")
        if os.path.exists(name):
            with open(name, "r") as f:
                print("\n📄 File Content:")
                print(f.read())
        else:
            print("❌ File not found.")

    elif choice == "3":
        name = input("File name: ")
        if os.path.exists(name):
            os.remove(name)
            print("🗑️ File deleted.")
        else:
            print("❌ File not found.")

    elif choice == "4":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice.")
