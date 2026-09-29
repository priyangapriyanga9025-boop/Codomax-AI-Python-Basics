# Day 3 - Python Programming

# While Loop
print("While Loop:")
number = 1

while number <= 5:
    print(number)
    number += 1

# Function
def greet(name):
    print("Hello", name)

greet("Priyanga")

# List Operations
numbers = [10, 20, 30, 40, 50]

print("\nList:", numbers)
print("First element:", numbers[0])
print("Total elements:", len(numbers))
print("Sum:", sum(numbers))

# Even and Odd Numbers
print("\nEven and Odd Numbers:")

for number in numbers:
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")
