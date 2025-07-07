# """
# # Program to display a diagram showing how Python works (Input → Processing → Output)

# print("+" + "-"*48 + "+")
# print("|{:^48}|".format("How Python Works"))
# print("+" + "-"*48 + "+")
# print("|{:^48}|".format("Input → Processing → Output"))
# print("+" + "-"*48 + "+")
# print("|{:^48}|".format("Input: Getting data from user"))
# print("|{:^48}|".format("↓"))
# print("|{:^48}|".format("Processing: Python processes the input"))
# print("|{:^48}|".format("↓"))
# print("|{:^48}|".format("Output: Displays the result"))
# print("+" + "-"*48 + "+")
# """
# """
# 2.2. Write a program to input 2 numbers from the users and display the output of below mentioned operations in a proper format.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

sum_result = a + b
subtract_result = a - b
multiply_result = a * b
modulo_result = a % b
floor_result = a // b

print("Results:")
print("-------")
print(f"Sum: {sum_result}")
print(f"Subtract: {subtract_result}")
print(f"Multiply: {multiply_result}")
print(f"Modulo: {modulo_result}")
print(f"Floor Division: {floor_result}")
# """
# """
# #3. Write a program to take a number input from the user and display whether the number is even or odd.
# a=int(input("enter the number"))
# if a%2==0:
#     print("number is even")
# else:
#     print("number is odd")
# """
# '''
# #4. Write a program to take a number input from the user and display the result of some mathematical calculations as mentioned below. 
# num=int(input("enter the number"))
# print("square of number is",num**2)
# square_root=num**1/2
# print("square root of number is",square_root)
# print("cube of number is",num**3)
# print(num*3,num*4,num*5)
# exp_val=int(input("enter the value"))
# print("number raised to the power of value is",num**exp_val)
# '''
# '''
# #5. Solve the below mentioned expressions in a python program. Feel free to take input of the required variables to solve the expressions.
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# c=int(input("enter the number"))
# first_eqn= a*2+2*a*b+b*2
# print(first_eqn)
# second_eqn= a*5+2*a*b*c+b*3
# print(second_eqn)
# third_eqn=a*7+5*a*b*c+b*7
# print(third_eqn)
# '''
# '''
# #6. Write a program to input the number of 5 subjects from the user, calculate the average, total, percentage and division of the students on the basis of specifications mentioned below.
# a = int(input("enter marks"))
# b = int(input("enter marks"))
# c = int(input(" enter marks"))
# d = int(input(" enter marks"))
# e = int(input(" enter marks"))
# sum = a+b+c+d+e
# print (sum)
# percentage = (a+b+c+d+e)/500*100
# print (percentage)
# if percentage>=0 and percentage<=44:
#     print("fail")
# elif percentage>=45 and percentage<=49:
#         print("3rd division")
# elif percentage>50 and percentage<=59:
#         print("2nd division")
# elif percentage >=60 and percentage <=79:
#         print ("1st division")
# else:
#         print ("distinction")
# '''
# '''
# #7. Write a program to display the prime number between 2 numbers input by the users. Also print the sum of all the prime numbers. [Hint: Prime numbers are the one which are either divisible by 1 or themselves. 3, 5, 7, 11, etc are some of the examples.]
# a=int(input("enter the number"))
# b=int(input("enter the number"))
# if a > b:
#     print("The starting number should be less than or equal to the bing number.")
# else:
#     primes = []
#     prime_sum = 0

#     for num in range(a,b + 1):
#         if num > 1:
#             is_prime = True
#             for i in range(2, int(num**0.5) + 1):
#                 if num % i == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 primes.append(num)
#                 prime_sum += num

#     print(f"Prime numbers between {a} and {b}: {primes}")
#     print(f"Sum of all prime numbers between {a} and {b}: {prime_sum}")
# '''
# '''
# #8. Write a program which will find all such numbers that are divisible by 7 but are not a multiple of 5, 
# #between 2000 and 3200 (both included). The numbers should be printed on the output screen. Also try the same program by replacing 2000 and 3200 by taking input for them from the users.
# a=2000
# b=3200
# number=[]
# for i in range(a,b,1):
#     if i%7==0 and i%5!=0:
#       number.append(i)
# print("the number between 200 and 3200 are",number)
# a=int(input("enter the first number"))
# b=int(input("enter the second number"))
# number=[]
# for i in range(a,b,1):
#     if i%7==0 and i%5!=0:
#       number.append(i)
# print(f"the number between {a} and {b} are",number)
# '''
# """
# #9. Write a program to find the factorial of any number taken as an input from the user. Try to validate the user input whether it is a number or not and then only perform the operation. In case of other than number as an input, display an error as “Not a number.”. [Hint: few available functions to identify the input is a number or not are ‘isdigit(), isnumeric(), etc.]
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# user_input = input("Enter a number to find its factorial: ")

# if user_input.isdigit():
#     number = int(user_input)
#     result = factorial(number)
#     print(f"The factorial of {number} is: {result}")
# else:
#     print("Not a number.")
# """
# """
# sum_even = 0
# sum_odd = 0

# while True:
#     user_input = input("Enter a number (or type 'exit' to finish): ")

#     if user_input.lower() == 'exit':
#         break

#     if user_input.isdigit() or (user_input[0] == '-' and user_input[1:].isdigit()):
#         number = int(user_input)

#         if number % 2 == 0:
#             sum_even += number
#         else:
#             sum_odd += number
#     else:
#         print("Invalid input. Please enter a valid number.")

#     continue_program = input("Do you want to continue? (yes/no): ").lower()
#     if continue_program != 'yes':
#         break

# print(f"Sum of even numbers: {sum_even}")
# print(f"Sum of odd numbers: {sum_odd}")
# """
# """
# 11. Write a program to create a number guessing game for the user. The program should ask the user to input a number. The program specifications are as mentioned below.
# I.	The program should generate a random number for the answer.
# II.	The program should prompt the user for a number input.
# III.	The program should provide the feedback to the user after each guesses (e.g. “Too high”, “Too low” or “Correct number”).
# IV.	The program should check the user input for 5 times and allow the users to guess for at most 5 times if their input don’t match the answer number.
# V.	If the user is not able to guess the answer within 5 times, the program should display “Game Over” message and exit.
# """
# """
# answer = 42
# attempts = 5

# print("Guess the number between 1 and 100.")

# for i in range(attempts):
#     guess = input(f"Attempt {i+1}: Enter your guess: ")
#     if not guess.isdigit():
#         print("Please enter a valid number.")
#         continue
#     guess = int(guess)
#     if guess < answer:
#         print("Too low")
#     elif guess > answer:
#         print("Too high")
#     else:
#         print("Correct number!")
#         break
# else:
#     print("Game Over. The number was:", answer)
# # """
