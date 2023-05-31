with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Write
with open("my_file.txt", mode="w") as file:
    file.write("New text.")

# Append
with open("my_file.txt", mode="a") as file:
    file.write("\nNewest text.")

# Create file
with open("new_file.txt", mode="w") as file:
    file.write("Newer text.")
