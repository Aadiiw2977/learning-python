import os

while True:
    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("📂 SMART NOTES MANAGER")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("1. Create Note")
    print("2. Read Note")
    print("3. Delete Note")
    print("4. Exit")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━")

    choice = input("Choose (1-4): ")

    if choice == "1":
        filename = input("📝 Note Name: ")
        text = input("✍️ Write Note: ")

        with open(filename + ".txt", "w") as file:
            file.write(text)

        print("✅ Note Saved Successfully!")

    elif choice == "2":
        filename = input("📖 Note Name: ")

        if os.path.exists(filename + ".txt"):
            with open(filename + ".txt", "r") as file:
                print("\n📄 Note Content")
                print("━━━━━━━━━━━━━━━━━━")
                print(file.read())
                print("━━━━━━━━━━━━━━━━━━")
        else:
            print("❌ Note Not Found!")

    elif choice == "3":
        filename = input("🗑️ Note Name: ")

        if os.path.exists(filename + ".txt"):
            os.remove(filename + ".txt")
            print("✅ Note Deleted!")
        else:
            print("❌ Note Not Found!")

    elif choice == "4":
        print("👋 Thanks for using Smart Notes Manager!")
        break

    else:
        print("❌ Invalid Option!")
