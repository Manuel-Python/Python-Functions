def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid 'int' is entered.

    :param prompt: The string that the user will see, when
        they're prompted to enter the value
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)
answer = 5

print("Please pick a number between 1 and 10: ")
guess = get_integer(": ") #ctrl j to get doc strings

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have guessed incorrectly")
else:
    print("You got it first time")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have guessed incorrectly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have guessed incorrectly")
# else:
#     print("You got it first time")