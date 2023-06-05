list_1 = [line.strip() for line in open('file1.txt')]
list_2 = [line.strip() for line in open('file2.txt')]

result = [int(num) for num in list_1 if num in list_2]

# Write your code above 👆

print(result)
