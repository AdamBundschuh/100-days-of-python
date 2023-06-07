# FileNotFound
# KeyError
# IndexError
# TypeError

# try: Code to test
# except: Do this if there WAS an exception
# else: Do this if there WAS NOT an exception
# finally: Do this no matter what

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)


