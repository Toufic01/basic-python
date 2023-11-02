# Question 11: Print the first n natural numbers
def print_natural_numbers(n):
    for i in range(1, n + 1):
        print(i)

n = int(input("Enter the number: "))
print_natural_numbers(n)

# Question 12: Calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter the number: "))
print(factorial(n))

# Question 13: Generate a Fibonacci sequence of length n
def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    return fibonacci_sequence

n = int(input("Enter the number of terms: "))
print(generate_fibonacci_sequence(n))

# Question 14: Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

n = int(input("Enter the number: "))
print(is_prime(n))

# Question 15: Print the multiplication table of a number
def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

n = int(input("Enter the number: "))
print_multiplication_table(n)

# Question 16: Find the sum of even numbers between 1 and n
def sum_even_numbers(n):
    sum = 0
    for i in range(2, n + 1, 2):
        sum += i
    return sum

n = int(input("Enter the number: "))
print(sum_even_numbers(n))

# Question 17: Reverse a given number
def reverse_number(n):
    reversed_number = 0
    while n > 0:
        remainder = n % 10
        reversed_number = reversed_number * 10 + remainder
        n //= 10
    return reversed_number

n = int(input("Enter the number: "))
print(reverse_number(n))

# Question 18: Check if a string is a palindrome
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

n = input("Enter a string: ")
print(is_palindrome(n))

# Question 19: Generate a random number and let the user guess it
import random

def guess_random_number():
    random_number = random.randint(1, 100)
    print(f"The random number is: {random_number}")
    print("You have one attempt to guess the number between 1 and 100:")
    
    guess = int(input("Enter your guess:"))

    if guess == random_number:
        print("You guessed it! Congratulations!")
    else:
        print("Sorry, you didn't guess correctly. The random number was:", random_number)

guess_random_number()


# Question 20: Find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print(gcd(n1, n2))
