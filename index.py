def add_person():
    name = input("Enter the Name: ")
    age = input("Enter the Age: ")
    email = input("Enter the Email: ")

    person = {"Name": name, "Age": age, "Email": email}
    return person


def display_person(people):
    for i, person in enumerate(people):
        print(i + 1, person['Name'], "|", person['Age'], "|", person['Email'])


def delete_contact(people):
    if not people:
        print("No contacts to delete.")
        return

    display_person(people)

    while True:
        number = input("Enter the contact number to delete: ")
        try:
            number = int(number)
            if number < 1 or number > len(people):
                print("Invalid Number, please enter a valid number.")
            else:
                break
        except:
            print("Invalid input! Please enter a number.")

    people.pop(number - 1)
    print("Person Deleted Successfully!")


def search_contact(people):
    search_name = input("Enter the Search Name: ").lower()
    result = [person for person in people if search_name in person['Name'].lower()]

    if result:
        display_person(result)
    else:
        print("No contact found.")


print("Hi! Welcome to My Contact List")
people = []

while True:
    print("Total Contacts:", len(people))
    command = input("Enter: Add, Delete, Search, Q (Quit): ").lower()

    if command == 'add':
        person = add_person()
        people.append(person)
        print("Contact Added!")
    elif command == 'delete':
        delete_contact(people)
    elif command == 'search':
        search_contact(people)
    elif command == 'q':
        break
    else:
        print("Invalid Command")
