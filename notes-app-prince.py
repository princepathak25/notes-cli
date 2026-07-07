# CLI Notes App 
import time

def display_banner():
    print("\n🗒️✨ Welcome to Notes ✨🗒️")
    print("Stay organized. Stay legendary.\n")

def show_menu():
    print("🔸 What would you like to do?")
    print("1️⃣ Add a note")
    print("2️⃣ View all notes")   
    print("3️⃣ Delete a note")
    print("4️⃣ Exit\n")

def add_note(notes):
    title = input("📝 Enter the note title: ")
    body = input("📄 Enter the note content: ")
    notes.append({"title": title, "body": body})
    print("✅ Note added successfully!\n")
    time.sleep(1)

def view_notes(notes):
    if not notes:
        print("📭 No notes found!\n")
    else:
        print("\n📚 Your Notes:")
        for i, note in enumerate(notes, start=1):
            print(f"{i}. 📌 {note['title']} - {note['body']}")
        print()
    time.sleep(2)

def delete_note(notes):
    if not notes:
        print("📭 No notes to delete.\n")
        return
    try:
        num = int(input("🗑️ Enter the note number to delete: "))
        if 1 <= num <= len(notes):
            removed = notes.pop(num - 1)
            print(f"❌ Deleted: {removed['title']}\n")
        else:
            print("⚠️ Invalid number!\n")
    except ValueError:
        print("❗ Please enter a valid number.\n")
    time.sleep(1.5)

def main():
    notes = []
    display_banner()

    while True:
        show_menu()
        choice = input("👉 Choose an option (1-4): ")

        if choice == '1':
            add_note(notes)
        elif choice == '2':
            view_notes(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            print("\n👋 Thanks for using Prince’s Notes App. Stay creative and thoughtful!")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
