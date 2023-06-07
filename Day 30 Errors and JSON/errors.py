# FileNotFound
# KeyError
# IndexError
# TypeError

# try: Code to test
# except: Do this if there WAS an exception
# else: Do this if there WAS NOT an exception
# finally: Do this no matter what

try:
    file = open("a_file.txt")
    a_dict = {"key":"value"}
    print(a_dict["xyz"])
except FileNotFoundError as error_message:
    file = open("a_file.txt", mode="w")
    file.write("Something")
    print(f"There was an error: {error_message}")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    print("There were no errors or exceptions.")
finally:
    file.close()
    print("File was closed.")
