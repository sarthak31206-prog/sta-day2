user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]
squares = [num ** 2 for num in numbers]

print("The squares are:", squares)