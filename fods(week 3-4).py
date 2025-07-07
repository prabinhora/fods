# #1. Write a program to create a function which accepts 2 numbers and displays the sum, difference,
# #product and the remainder values.
# a=int(input("enter the 1st number"))
# b=int(input("enter the 1st number"))
# sum=a+b
# print(sum)
# differnece=a-b
# print(differnece)
# product=a*b
# print(product)
# rem=a%b
# print(rem)
# """
# 2. Write a program to create separate functions for below mentioned mathematical calculations
# which would return the values back to the program. The functions should accept the 2 number which
# are inputs from the user and passed to them. The program should display the output in a proper
# format.
# I. Addition
# II. Subtraction
# III. Multiplication
# IV. Division
# V. Modulo division
# VI. Floor division
# """
# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     return x / y if y != 0 else "Error: Division by zero"

# def modulo(x, y):
#     return x % y if y != 0 else "Error: Division by zero"

# def floor_divide(x, y):
#     return x // y if y != 0 else "Error: Division by zero"

# print("Enter two numbers:")
# num1 = float(input("Number 1: "))
# num2 = float(input("Number 2: "))

# print("\nResults:")
# print("Addition:", add(num1, num2))
# print("Subtraction:", subtract(num1, num2))
# print("Multiplication:", multiply(num1, num2))
# print("Division:", divide(num1, num2))
# print("Modulo Division:", modulo(num1, num2))
# print("Floor Division:", floor_divide(num1, num2))
# """
# 3. Write a program to create a function which will accept a parameter and return the factorial of the
# number. The output should be displayed in a proper format.
# # """
# def factorial(n):
#     if n < 0:
#         return "Error: Factorial is not defined for negative numbers."
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# num = int(input("Enter a number to calculate its factorial: "))
# result = factorial(num)
# print("The factorial of", num, "is:", result)
# """
# 4. Write a function to accept a list of numbers and print the occurrence of each number. The function
# should be tested well in the program by calling and sending various list of numbers.
# # """
# def count_occurrences(numbers):
#     occurrences = {}
#     for number in numbers:
#         if number in occurrences:
#             occurrences[number] += 1
#         else:
#             occurrences[number] = 1
    
#     for number, count in occurrences.items():
#         print(f"Number {number} occurs {count} time(s).")

# count_occurrences([1, 2, 2, 3, 4, 4, 4, 5])
# count_occurrences([10, 20, 10, 30, 20, 10])
# count_occurrences([5, 5, 5, 5, 5])
# count_occurrences([])
# count_occurrences([1, 2, 3, 4, 5, 1, 2, 1])
# """

# 5. Write a function to accept a list of names and return the sorted order of names back.
# # """
# def sort_names(names):
#     return sorted(names)

# names_list = ["Alice", "Charlie", "Bob", "Eve", "David"]
# sorted_names = sort_names(names_list)
# print("Sorted names:", sorted_names)
# """
# 6. Write a function to accept a 2 parameters, one is the list of cities and another is the city that the
# user wants to search. The function should search the city in the list of cities and return the index of
# the list where the city is available. If the city is not available, the program should return a proper
# message.
# # """
# def find_city(cities, target):
#     try:
#         index = cities.index(target)
#         return f"'{target}' found at index {index}"
#     except ValueError:
#         return f"'{target}' not found in the list"

# cities_list = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
# print(find_city(cities_list, "Chicago"))
# print(find_city(cities_list, "Seattle"))
# print(find_city(cities_list, "Houston"))
# """
# 7. Write a function word_frequency(sentence) that takes a sentence as input and returns a
# dictionary containing the frequency of each word in the sentence. [Hint: split the sentence into
# words and iterate to check the word frequency.]
# # """
# def find_city(cities, target):
#     try:
#         index = cities.index(target)
#         return f"'{target}' found at index {index}"
#     except ValueError:
#         return f"'{target}' not found in the list"

# cities_list = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
# print(find_city(cities_list, "Chicago"))
# print(find_city(cities_list, "Seattle"))
# print(find_city(cities_list, "Houston"))
# """
# 8. Write a program to accept a list of numbers from the user and should return a list by removing
# the duplicate values, if any.
# # """
# def remove_duplicates(numbers):
#     return list(set(numbers))

# user_input = input("Enter a list of numbers separated by spaces: ")
# numbers_list = list(map(int, user_input.split()))
# unique_numbers = remove_duplicates(numbers_list)
# print("List after removing duplicates:", unique_numbers)
# """
# 9. Write a program to ask the details of 5 books (title, author, ISBN, cost), add them in the
# dictionary and print them.
# # """
# books = {}

# for i in range(5):
#     title = input("Enter book title: ")
#     author = input("Enter author: ")
#     isbn = input("Enter ISBN: ")
#     cost = float(input("Enter cost: $"))
#     books[isbn] = {'title': title, 'author': author, 'cost': cost}

# print("\nBook Collection:")
# for isbn, details in books.items():
#     print(f"Title: {details['title']}, Author: {details['author']}, ISBN: {isbn}, Cost: ${details['cost']:.2f}")
# """
# 10. Create a program to ask a user to give continuous input of numbers until they like. The
# program should keep on segregating the user input numbers into even and odd lists separately.
# Once the user completes the input and opts for exiting the program, the program should display
# the separate list of even and odd lists in a proper format.
# # """
# even_numbers = []
# odd_numbers = []

# while True:
#     user_input = input("Enter a number (or type 'exit' to finish): ")
    
#     if user_input == 'exit':
#         break
    
#     number = int(user_input)
    
#     if number % 2 == 0:
#         even_numbers.append(number)
#     else:
#         odd_numbers.append(number)

# print("Even Numbers:", even_numbers)
# print("Odd Numbers:", odd_numbers)
# """
# 11. Write a program to generate a card guessing game for the users in an interesting way. The
# card should have property such as name and value (e.g. ace 10). Specifications are as mentioned
# below.
# I. The program should have a list of card values like 2, 3, 4,…., Jack, Queen, King, Ace
# II. The program should have a list of card suits like heart, diamond, club, spades.
# III. The program should randomly pick up a number and a suit and keep as an answer in a
# separate list.
# IV. The program should ask the player to guess the card value and the suit.
# V. The program should check the player guessed value with the computer answer value. If
# both the parts don’t match, the program should show a broken heart and game over to the
# player. If any one of the part of answer matches, the program should show a smily face to
# the player. If both the guesses of the player matches with the program answer, the
# program should show a heart and a smily face to the user.
# """
import random

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

answer = [random.choice(values), random.choice(suits)]

print("Guess the card!")
guess_value = input("Enter card value: ")
guess_suit = input("Enter card suit: ")

if guess_value == answer[0] and guess_suit == answer[1]:
    print("Correct! :) <3")
elif guess_value == answer[0] or guess_suit == answer[1]:
    print("Partial match :)")
else:
    print("Wrong :(")

print("The card was:", answer[0], "of", answer[1])
