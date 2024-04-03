import json
import re

# region DB
database = []


def read_database_from_file():
    try:
        with open("Database/database.json", "r") as f:
            input = f.read()
            global database
            database = json.loads(input)
    except:
        write_to_database("")
    return database


def write_to_database(record):
    with open("Database/database.json", "w") as f:
        f.write(json.dumps(record, indent=4))


def append_to_database(record):
    global database
    database = read_database_from_file()
    database.append(record)
    write_to_database(database)


def remove_from_database(record):
    global database
    database.remove(record)
    write_to_database(database)


def find_in_database(record):
    global database
    database = read_database_from_file()
    for element in database:
        if element[0] == record:
            return element
        if element[1] == record:
            return element
        if element[2] == record:
            return element

    return


def list_database():
    global database
    database = read_database_from_file()
    if not database:
        print("No data in the database, try adding some!")
    else:
        print('listing all records in the database:')
    for element in database:
        print_record(element)


def print_record(record):
    print(record[0])
    print(record[1])
    print(record[2])
    print('______________________________')


# endregion

def db_options():
    print("\nWhat would you like to do?")
    print(" 1) Add record \n 2) List all records\n 3) Find record \n 4) Delete record \n 5) Quit")


def ask_for_record():
    isValid = False
    while not isValid:
        firstname = input("Enter first name>>>:: ").strip()
        lastname = input("Enter last name>>>:: ").strip()
        phonenumber = input("Enter phone number>>>:: ").strip()
        if not verify_record(firstname, lastname, phonenumber):
            print("Invalid, must fill out all fields")
        else:
            print("Thank you for")
            isValid = True
            return (firstname, lastname, phonenumber)


def ask_field_to_find(type):
    value = input(f"Enter value you want to {type} (Ex: Matt)\n>>>:: ")
    record = find_in_database(value)
    if record is not None:
        if type == 'find':
            print('record found: ')
            print_record(record)
            return
        elif type == 'delete':
            print('record removed')
            remove_from_database(record)
    else:
        print(f'No instance of "{value}" found in the database')


# region verify fields
def verify_record(firstname, lastname, phonenumber):
    if len(firstname) < 1 or len(lastname) < 1 or len(phonenumber) < 10:
        return False
    else:
        if verify_name(firstname) and verify_name(lastname) and verify_phone_number(phonenumber):
            return True


def verify_name(name):
    pattern = r'^[a-zA-Z\-\' ]+$'
    return re.match(pattern, name)


def verify_phone_number(phone_number):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return re.match(pattern, phone_number)


# endregion

def startApp():
    print("Welcome to the database!")
    quitapp = False
    while True:
        db_options()
        userInput = input()
        try:
            int_option = int(userInput.strip())

            match int_option:
                case inp if inp == 1:
                    record = ask_for_record()
                    append_to_database(record)
                case inp if inp == 2:
                    list_database()
                case inp if inp == 3:
                    ask_field_to_find('find')
                case inp if inp == 4:
                    ask_field_to_find('delete')
                case inp if inp == 5:
                    break
                case inp if inp > 5:
                    print('Invalid input! Must be a number from 1 to 5!')
                case inp if inp <= 0:
                    print('Invalid input! Must be a number from 1 to 5!')

        except ValueError as ex:
            print(ex)
            print("Invalid input! Must be a number.")


if __name__ == '__main__':
    startApp()
