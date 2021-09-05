import os
import time

def take_notes():
    os.system("cls")
    print("Please enter your notes below:")
    notes = []
    while True:
        user_input = input()
        if user_input == "!END!":
            break
        notes.append(user_input)

    filename = "Notes/" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    with open(filename, "w") as file:
        file.write("\n".join(notes))
    print("\nNotes taken.")

def view_notes():
    os.system("cls")
    files = {}
    index = 1
    for file in os.listdir("Notes"):
        files[index] = file
        index += 1

    if files:
        print("id filename            content")
        for index, file in files.items():
            with open("Notes/" + file) as f:
                content = f.read().replace("\n", "; ")
            if len(content) < 50:
                print(str(index) + "  " + file + " " + content)
            else:
                print(str(index) + "  " + file + " " + content[:50] + "...")

        file_id = input("Enter the id of the file you want to open: ")
        file = files[int(file_id)]

        os.system("cls")
        print("Content in " + file + ":")
        with open("Notes/" + file, "r") as f:
            print(f.read())

    else:
        print("No notes available.")

def main():
    os.system("cls")
    print("Welcome to Note Taker!")
    while True:
        print("Menu:")
        print("  [1]: Take new notes")
        print("  [2]: View old notes")
        print("  [3]: Exit")
        option = int(input("Select menu option: "))
        if option == 1:
            take_notes()
        elif option == 2:
            view_notes()
        elif option == 3:
            break
        else:
            print("Invalid option. Please try again.")
    print("Thank you for using Note Taker, have a great day!")

main()
