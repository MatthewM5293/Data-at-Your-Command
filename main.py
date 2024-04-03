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
        if element[0].lower() == record.lower():
            return element
        if element[1].lower() == record.lower():
            return element
        if element[2].lower() == record.lower():
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


def ask_for_record(firstname, lastname, phonenumber):
    isValid = False
    while not isValid:
        if verify_record(firstname, lastname, phonenumber):
            print("Invalid, must fill out all fields")
        else:
            isValid = True
            append_to_database((firstname, lastname, phonenumber))


def ask_field_to_find(type, value):
    # value = input(f"Enter value you want to {type} (Ex: Matt)\n>>>:: ")
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
    if len(firstname) < 1 or len(lastname) < 1 or len(phonenumber) < 9:
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


def print_database_usage():
    print('Usage:')
    print('add [fname] [lname] [phone]  (add a new contact record)')
    print('list                                             (list all records)')
    print('find [value]                               (find and show the first record that matches the search)')
    print('del [value]                                 (delete the first record that matches the search)')
    print('quit                                            (quit the CLI)')


# endregion

def startApp():
    print("Welcome to the database!")
    print_database_usage()
    while True:
        userInput = input()
        try:
            command = userInput.strip().split()

            match command[0].lower():
                case inp if inp == 'add' and len(command) == 4:
                    ask_for_record(command[1], command[2], command[3])
                    print('added new record to database')
                case inp if inp == 'list':
                    list_database()
                case inp if inp == 'find' and len(command) == 2:
                    ask_field_to_find('find', command[1])
                case inp if inp == 'del' and len(command) == 2:
                    ask_field_to_find('delete', command[1])
                case inp if inp == 'quit':
                    break
                case _:
                    print_database_usage()
        except ValueError:
            print_database_usage()


if __name__ == '__main__':
    startApp()
