# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("Hello")
#     print("How are you?")
#     print("Goodbye")
    
# greet()

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you {name}?")
#     print(f"Goodbye {name}")
    
# greet_with_name("Angela")

def greet_with(location, name):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
    
greet_with("Angela", "London")
greet_with(location="London", name="Angela")