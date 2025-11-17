# # if statements
# age = 18
# if age >= 18:
#     print('You are eligible to vote!')
    
# fruit = 'apple'
# if fruit == 'apple':
#     print('Your a Fav Fruit')

# name = 'CodeQueen'
# if name == 'CodeQueen':
#     print('You are a Developer')




# # if Else
# age = 16
# if age >= 18:
#     print('Youre a eligible to vote!')
# else:
#     print('You are not eligible!')
    
    
# num = input('Enter Your Number')
# if num % 2 == 0:
#     print('Even Number')
# else:
#     print('Odd Number')
    

# username = input('Enter Your Username')
# password = input('Enter Your Password')

# if username == 'admin' and password == '12345':
#     print('login successful')
# else: 
#     print('Login failed!')
    
    
# mypassword = 'mnbvcxz12345'
# if len(mypassword) > 6:
#     print('Strong Password')
# else:
#     print('Weak Password')



# # if elif-else
# marks = 91
# if marks >= 90:
#     print('A Grade')
# elif marks >= 80:
#     print('B Grade')
# elif marks >= 70:
#     print('C Grade')
# else:
#     print('F Grade')
    

# age = 20
# if age < 15:
#     print('Child')
# elif age < 25:
#     print('Teenager')
# elif age < 50:
#     print('Adult')
# else:
#     print('Senior Citizen')
    
    
# temp = 18
# if temp >= 30:
#     print('its Hot!')
# elif temp >= 20:
#     print('Warm')
# elif temp >= 10:
#     print('Cool')
# else:
#     print('Its cold')
    
# age = 20
# is_student = True
# if age < 12:
#     print('Child')
# elif age <= 25 and is_student:
#     print('Student')
# elif age <= 60:
#     print('Adult')
# else:
#     print('Senior')


# # Nested if
# fruit = 'Apple'
# color = 'Red'
# if fruit == 'Apple':
#     if color == 'Red':
#         print('Red Apple')
#     else:
#         print('green Apple')

# elif fruit == 'Banana':
#     if color == 'Yellow':
#         print('Yellow banana')
#     else:
#         print('Green Banana')
# else:
#     print('Other fruit')




# Simple Quiz Game 
score = 0
print('Welcome to the Simple Quiz Game!')
print('Answer the following questions by typing a, b, c, or d.\n')

# Q1
print('1. What is the capital of France?')
print('a) Berlin')
print('b) Madrid')
print('c) Paris') 
print('d) Rome')
answer = input('Your Answer: ').lower()
if answer == 'c':
    print('Correct')
    score += 1
else:
    print('Wrong! The correct answer is c) Paris')
    
# Q2
print('2. Which Programming language is this game written in?')
print('a) Java')
print('b) C++')
print('c) JS') 
print('d) Python')
answer = input('Your Answer: ').lower()
if answer == 'd':
    print('Correct')
    score += 1
else:
    print('Wrong! The correct answer is d) Python')
    
# Q1
print('1. What is 10 + 5?')
print('a) 10')
print('b) 15')
print('c) 9') 
print('d) 21') 
answer = input('Your Answer: ').lower()
if answer == 'b':
    print('Correct')
    score += 1
else:
    print('Wrong! The correct answer is b) 15')
    
# Final Score
print(f'Your Final Score is: {score} out of 3')
if score == 3:
    print('Excellent!')
elif score == 2:
    print('Good')
else:
    print('Better Luck Next Time!')