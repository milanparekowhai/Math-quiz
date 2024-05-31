import random
import math


def round_num(num):
    while True:

        if num - math.floor(num) >= 0.5:
            return math.ceil(num)

        else:
            return math.floor(num)


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


def equation(num1, num2, ops):
    return f"{num1} {ops} {num2}"


round_number = 0
max_rounds = 0
# todo define history list
points_number = 0
inccorect_point_number = 0

history_player = []
history_answer = []

# todo introduce the quiz (no game)
want_instructions = yes_no("would you like to see the instructions enter yes or no ")

if want_instructions == "yes":
    print('''
***** Quiz *****
💠💠💠 Math quiz 💠💠💠

😎😎😎 Welocome to my math quiz 😎😎😎

This quiz will foucs on basic math questions 
some might be hard but try you best 

You stats will be shown at the end 

🫡🫡🫡G00D LUCK😊😫😫😫

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

    if int_check_answer("", -1000, 10000) == answer:
        print("correct!")
        points_number += 1
    else:
        print("incorrect")
        inccorect_point_number += 1

# todo append current question history to list

    if round_number >= max_rounds:
        print("You have done the test here are your stats\n"
              f"{points_number} Correct!\n\n"
              f"{inccorect_point_number} incorrect")
        history_see = input("Would you like to see your answers?")
        if history_see == "yes":
            print(f'''the correct answers were {history_answer}
your answers were        {history_player}''')
        else:
            pass
        # todo ask if the user wants history, for loop print history
        valid = True



