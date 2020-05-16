"""Write a program with an infine loop (with the option to type q to quit)
and a list of numbers. Each time through the loop ask the user to guess a
number on the list and ask them whether or not they guessed correctly.
"""

numbers=[11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or type q to quit: ")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("Please type an number or q to quit: ")
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")
    
"""or non-numbers example..."""


qs=["What is your name?" ,"What is your favorite color?" ,"What is your quest? "]
n=0
while True:
    print("Type q to quit")
    a=input(qs[n])
    if a=="q":
        break
    n=(n+1)%3
