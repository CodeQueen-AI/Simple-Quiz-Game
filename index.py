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
