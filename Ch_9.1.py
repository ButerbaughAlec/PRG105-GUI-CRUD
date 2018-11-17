import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    try:
        input_file = open("name_file.dat", 'rb')
        names = pickle.load(input_file)
    except (FileNotFoundError, IOError):
        print("The file was not found.")
        names = {}

    option = 0

    while option != QUIT:
        option = menu()

        if option == LOOK_UP:
            look_up(names)
        elif option == ADD:
            add(names)
        elif option == CHANGE:
            change(names)
        elif option == DELETE:
            delete(names)
        elif option == QUIT:
            save(names)


def menu():
    print()
    print('Name and Email Address lookup')
    print('------------------------------')
    print('1. Look up a name')
    print('2. Add a new name')
    print('3. Change an email address')
    print('4. Delete a name')
    print('5. Quit the program\n')
    print()

    option = int(input("Please enter your option number between 1 and 5:"))
    return option


def look_up(names):
    name = input('Enter a name: ')
    print(names.get(name, 'Not found.'))


def add(names):
    name = input('Enter a name:')
    email = input('Enter an email address:')
    if name not in names:
        names[name] = email
    else:
        print("That name has already been added.")


def change(names):
    name = input('Enter a name:')
    if name in names:
        email = input('Enter a new email address:')
        names[name] = email
    else:
        print("That email has already been added.")


def delete(names):
    name = input('Enter a name:')
    if name in names:
        del names[name]
    else:
        print("That name was not found.")


def save(names):
    print("The file has been updated with your newest changes.")
    save_file = open("name_file.dat", 'wb')
    pickle.dump(names, save_file)
    save_file.close()


main()
