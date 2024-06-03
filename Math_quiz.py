import random
import math

#
def round_num(num):
    while True:

        if num - math.floor(num) >= 0.5:
            return math.ceil(num)

        else:
            return math.floor(num)
# checks for yes/no inputs
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def string_checker(user_response, valid_ans):
    while True:

        # Get user response and make sure its lowercase
        user_response = user_response.lower()

        for item in valid_ans:
            # check if the user response is a word in the lst
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list.

            elif user_response == item[0]:

                return item

        return "invalid"

# check if the int should be used
def int_check(int_question, low, high):
    while True:

        error = f"Please enter an integer that is greater than {low} and less than {high}"

        try:

            response = int(input(int_question))

            # Checks that the number is more than / equal to 13

            if response < low:

                print(error)

            if response > high:

                print(error)

            else:

                return response

        except ValueError:

            print(error)

# appends the answer for player history
def int_check_answer(int_question, low, high):
    while True:

        error = f"Please enter an integer that is greater than {low} and less than {high}"

        try:

            response = int(input(int_question))
            history_player.append(response)
            # Checks that the number is more than / equal to 13

            if response < low:

                print(error)

            if response > high:

                print(error)

            else:

                return response

        except ValueError:

            print(error)

# makes the question
def equation(num1, num2, ops):
    return f"{num1} {ops} {num2}"


# round counter

round_number = 0
max_rounds = 0
# todo define history list
points_number = 0
inccorect_point_number = 0

history_player = []
history_answer = []

#  instructions
want_instructions = yes_no("would you like to see the instructions enter yes or no ")

if want_instructions == "yes":
    print('''
***** Quiz *****
💠💠💠 Math quiz 💠💠💠

😎😎😎 Welocome to my math quiz 😎😎😎

This quiz will foucs on basic math questions 
some might be hard but try you best 

 (+) means you need to add the numbers together
 (-) means you need to minus the number together
 (*) means you need to times the numbers together
 (/) means you need to divide the numbers together
 
You stats will be shown at the end 

🫡🫡🫡G00D LUCK 

          ''')

max_rounds = int_check("how many Question would you like ?", 1, 10)
start = input("Press <enter> to begin")

valid = False
while not valid:

    round_number += 1

    print()
    print(f"💠💠💠 Question {str(round_number)} 💠💠💠")

    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    operation = ["+", "-", "*", "/"]

    # Select a random operator
    selected_operator = random.choice(operation)
    question = equation(num1, num2, selected_operator)
    print(question)

    if selected_operator == "+":
        answer = num1 + num2
    elif selected_operator == "-":
        answer = num1 - num2
    elif selected_operator == "*":
        answer = num1 * num2
    else:
        float_answer = num1 / num2
        answer = round_num(float_answer)
    history_answer.append(answer)

    if int_check_answer("", -1000, 10000) == answer:
        print("correct!")
        points_number += 1
    else:
        print("incorrect")
        inccorect_point_number += 1

# history list

    if round_number >= max_rounds:

        if yes_no("You have done this quiz!👍"
              "would you like to see your anwsers and stats? (Yes or no)") == "yes":
            print(f"The correct anwsers were {history_answer}\n"
                  f"Your anwers were {history_player}\n"
                  f"{points_number} correct\n"
                  f"{inccorect_point_number} inccorect")

        else:
            print("Thank you for taking this quiz 😊")




        valid = True



