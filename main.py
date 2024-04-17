import json
import re

# region DB
database = []


def read_database_from_file():
    try:
        with open("db.json", "r") as f:
            input = f.read()
            global database
            database = json.loads(input)
    except:
        write_to_database([])
    return database


def write_to_database(record):
    with open("db.json", "w") as f:
        f.write(json.dumps(record, indent=4))


def append_to_database(record):
    global database
    database = read_database_from_file()
    database.append(record)
    write_to_database(database)


def remove_from_database(record):
    global database
    print(f'removed {record[0], record[1], record[2]} from database')
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

# region UI
def ask_for_record(firstname, lastname, phone_number):
    if not verify_record(firstname, lastname, phone_number):
        print("Invalid, must fill out all fields")
        return
    else:
        print(f'added {firstname, lastname, phone_number} to database')
        append_to_database((firstname, lastname, phone_number))


def ask_field_to_find(type, value):
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


# endregion

# region verify fields
def verify_record(firstname, lastname, phone_number):
    if len(firstname) < 1 or len(lastname) < 1 or len(phone_number) < 9:
        return False
    else:
        if not verify_name(firstname):
            print('First name is invalid')
            return False
        elif not verify_name(lastname):
            print('Last name is invalid')
            return False
        elif not verify_phone_number(phone_number):
            print('Phone number is invalid')
            return False
        else:
            return True


def verify_name(name):
    pattern = r'^[a-zA-Z\-\' ]+$'
    return re.match(pattern, name)


def verify_phone_number(phone_number):
    pattern = r'^(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
    return re.match(pattern, phone_number)


def print_database_usage():
    print('Usage:')
    print('cls                          (clears screen)')
    print('add [fname] [lname] [phone]  (add a new contact record)')
    print('list                         (list all records)')
    print('find [value]                 (find and show the first record that matches the search)')
    print('del [value]                  (delete the first record that matches the search)')
    print('quit                         (quit the CLI)')


# endregion

def start_app():
    print("Welcome to the database!")
    print_database_usage()
    while True:
        user_input = input('>>')
        try:
            command = user_input.strip().split()

            match command[0].lower():
                case inp if inp == 'add' and len(command) == 4:
                    ask_for_record(command[1], command[2], command[3])
                case inp if (inp == 'list' or inp == 'ls'):
                    list_database()
                case inp if inp == 'find' and len(command) == 2:
                    ask_field_to_find('find', command[1])
                case inp if inp == 'del' and len(command) == 2:
                    ask_field_to_find('delete', command[1])
                case inp if inp == 'quit':
                    break
                case inp if inp == 'cls':
                    print("\n" * 100)
                case _:
                    print_database_usage()
        except:
            print("Invalid input, please refer to below")
            print_database_usage()


if __name__ == '__main__':
    start_app()
