import json
import re


# region DB
class Database:
    def __init__(self):
        self.__filename = "db.json"
        self.__database = []

    def __read_database_from_file(self):
        try:
            with open(self.__filename, "r") as f:
                input = f.read()
                # global database
                self.__database = json.loads(input)
        except:
            self.__write_to_database([])
        return self.__database

    def __write_to_database(self, record):
        with open(self.__filename, "w") as f:
            f.write(json.dumps(record, indent=4))

    def __append_to_database(self, record):
        # global database
        self.__database = self.__read_database_from_file()
        self.__database.append(record)
        self.__write_to_database(self.__database)

    def __remove_from_database(self, record):
        # global database
        print(f'removed {record[0], record[1], record[2]} from database')
        self.__database.remove(record)
        self.__write_to_database(self.__database)

    def __find_in_database(self, record):
        # global database
        self.__database = self.__read_database_from_file()
        for element in self.__database:
            if element[0].lower() == record.lower():
                return element
            if element[1].lower() == record.lower():
                return element
            if element[2].lower() == record.lower():
                return element

        return

    def list_database(self):
        # global database
        self.__database = self.__read_database_from_file()
        if not self.__database:
            print("No data in the database, try adding some!")
        else:
            print('listing all records in the database:')
        for element in self.__database:
            self.__print_record(element)

    def __print_record(self, record):
        print(record[0])
        print(record[1])
        print(record[2])
        print('______________________________')

    # endregion

    # region UI
    def __ask_for_record(self, firstname, lastname, phone_number):
        if not self.__verify_record(firstname, lastname, phone_number):
            print("Invalid, must fill out all fields")
            return
        else:
            print(f'added {firstname, lastname, phone_number} to database')
            self.__append_to_database((firstname, lastname, phone_number))

    def __ask_field_to_find(self, type, value):
        record = self.__find_in_database(value)
        if record is not None:
            if type == 'find':
                print('record found: ')
                self.__print_record(record)
                return
            elif type == 'delete':
                print('record removed')
                self.__remove_from_database(record)
        else:
            print(f'No instance of "{value}" found in the database')

    # endregion

    # region verify fields
    def __verify_record(self, firstname, lastname, phone_number):
        if len(firstname) < 1 or len(lastname) < 1 or len(phone_number) < 9:
            return False
        else:
            if not self.__verify_name(firstname):
                print('First name is invalid')
                return False
            elif not self.__verify_name(lastname):
                print('Last name is invalid')
                return False
            elif not self.__verify_phone_number(phone_number):
                print('Phone number is invalid')
                return False
            else:
                return True

    def __verify_name(self, name):
        pattern = r'^[a-zA-Z\-\' ]+$'
        return re.match(pattern, name)

    def __verify_phone_number(self, phone_number):
        pattern = r'^(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
        return re.match(pattern, phone_number)

    def __print_database_usage(self):
        print()
        print('Usage:')
        print('cls                          (clears screen)')
        print('add [fname] [lname] [phone]  (add a new contact record)')
        print('list                         (list all records)')
        print('find [value]                 (find and show the first record that matches the search)')
        print('del [value]                  (delete the first record that matches the search)')
        print('quit                         (quit the CLI)')

    # endregion

    def start_app(self):
        print("Welcome to the database!")
        self.__print_database_usage()
        while True:
            user_input = input('>>')
            try:
                command = user_input.strip().split()

                match command[0].lower():
                    case inp if inp == 'add' and len(command) == 4:
                        self.__ask_for_record(command[1], command[2], command[3])
                    case inp if (inp == 'list' or inp == 'ls'):
                        self.list_database()
                    case inp if inp == 'find' and len(command) == 2:
                        self.__ask_field_to_find('find', command[1])
                    case inp if inp == 'del' and len(command) == 2:
                        self.__ask_field_to_find('delete', command[1])
                    case inp if inp == 'quit':
                        break
                    case inp if inp == 'cls':
                        print("\n" * 100)
                    case _:
                        self.__print_database_usage()
            except:
                print("Invalid input, please refer to below")
                self.__print_database_usage()
