# add [fname] [lname] [phone]
# list
# find [value]
# del [value]
# quit
# import json
#
# database = []
#
#
# def read_database_from_file():
#     with open("Database/database.json", "r") as f:
#         input = f.read()
#         database = json.loads(input)
#         return database
#
#
# def print_database():
#     print(database)
#
#
# def write_to_database(record):
#     with open("Database/database.json", "w") as f:
#         f.write(json.dumps(record, indent=4))
#
#
# def append_to_database(record):
#     database = read_database_from_file()
#     database.append(record)
#
#     with open("Database/database.json", "a") as f:
#         f.write(json.dumps(database, indent=4))
#
#
# def remove_from_database(record):
#     find_in_database(record)
#     database.remove(record)
#
#
# def find_in_database(record):
#     database = read_database_from_file()
#     for element in database:
#         if element == record:
#             return element
