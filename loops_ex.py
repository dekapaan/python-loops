# exercise1
for x in range(100):
    if (x + 1) % 3 == 0 and (x + 1) % 5 == 0:
        print("FizzBuzz")
    elif (x + 1) % 5 == 0:
        print("Buzz")
    elif (x + 1) % 3 == 0:
        print("Fizz")
    else:
        print(x + 1)
print("")

# Task1
import random

num = random.randint(0, 10)
guesses_left = 2
guess = int(input("Guess a number from 0 - 10: "))

while guesses_left >= 0:
    if guess != num and guesses_left > 0:
        guess = int(input("Guess again: "))
    elif guess == num:
        print("You win!")
        break
    guesses_left -= 1
else:
    print("You lose")

# Task2
n = 5
for x in range(n):
    for z in range(x):
        print('* ', end="")
    print('')
for x in range(n, 0, -1):
    for z in range(x):
        print('* ', end='')
    print('')
