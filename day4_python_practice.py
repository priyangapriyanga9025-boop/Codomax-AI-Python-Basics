# Day 4 - Python Practice Programs

# 1. Check Even or Odd
number = 10

if number % 2 == 0:
    print("10 is Even")
else:
    print("10 is Odd")


# 2. Find Largest Number
a = 25
b = 15

if a > b:
    print("Largest number:", a)
else:
    print("Largest number:", b)


# 3. Sum of Numbers
numbers = [10, 20, 30, 40, 50]

total = sum(numbers)

print("Sum of numbers:", total)


# 4. Factorial
number = 5
factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial of 5:", factorial)


# 5. Simple Calculator
num1 = 20
num2 = 10

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
