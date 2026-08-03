# # 1. **Question:** What is the `input()` function in Python used for?
# # input function used to take input from user as a string
#
# user_input = input('enter your name:')
#
# print(user_input)
#
#
# ### 2. **Question:** How can you accept an integer as input from the user using
# #`input()`?
# user_input = int(input('enter an integer or age'))
# print(user_input)
#
#
# ### 3. **Question:** How do you accept a float input from the user?
# user_input = float(input('enter the float'))
# print(user_input)
#
# ### 4. **Question:** How can you take multiple space-separated values as input?
# user_input = input('enter anything').split()
# print(user_input)
#
# numbers = list(map(int, input("Enter numbers: ").split()))
#
# print(numbers)
#
# ### 5. **Question:** How do you check if a number entered by the user is positive,
# # negative, or zero?
#
# user_input = int(input('enter the number is positive or negative'))
# if user_input > 0 :
#     print('number is positive')
# elif user_input < 0 :
#     print('number is negative')
# else:
#     print('number is zero')
#
#
# ### 6. **Question:** How do you convert user input to a list of integers?
# # using list comprehension
#
# user_input = [int(x) for x in input('enter the number comprehension').split() ]
# print(user_input)
#
#
# ### 7. **Question:** How do you accept a string input and print it in uppercase?
# user_input = str(input('enter your name').upper())
# print(user_input)
#
# ## 8. **Question:** Write a Python program that accepts a string and prints the
# ## number of vowels in it.
#
# user_input = str(input('enter the string'))
# vow = 'aeiou'
# count = 0
# for char in user_input:
#     if char.lower() in vow :
#         count += 1
#
# print(count)
#
# # using generator expression
# user_input = str(input('enter the sting'))
# vow = 'aeiou'
# count = sum(1 for char in user_input if char.lower() in vow)
# print(count)


# user_input = str(input('enter the sting'))
# if user_input == user_input[::-1]:
#     print(f'this is plaindrom {user_input} string {user_input[::-1]}',)
# else:
#     print('this is not plaindrome')


### 16. **Question:** Write a program that checks if the input number is a prime
# number.


# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
# else:
#     print("Not a prime number")


# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
#     print("Factorial:", factorial)


### 21. **Question:** How do you prevent a user from entering an empty string?
## **Answer:**

user_input = str(input('enter the string input')).strip()
if not user_input:
    print(input('input can not be empty'))
else:
    print(f'input is {user_input}')
