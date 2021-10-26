import turtle
import pandas as pd

# squirrel_census = pd.read_csv('squirrels.csv')

# print(squirrel_census.value_counts("Primary Fur Color"))
# guessed = []
# score = 0
# screen = turtle.Screen()
# screen.title("US state game")
# state_list  = pd.read_csv("50_states.csv")
# screen.addshape('blank_states_img.gif')
# turtle.shape('blank_states_img.gif')

# def check_answer(answer,score):
#     pen = turtle.Turtle()
#     pen.up()
#     if sanitized_answer not in guessed:
#         # try:
#             row = state_list[state_list["state"] == answer]
#             pen.goto(row.x,row.y)
#             pen.write(answer)
#             score +=1
#             guessed.append(answer)
#         # except:
#             print("Try again")
    
#     return score


# while len(guessed) <50:
#     answer =screen.textinput(title="Name a state", prompt=f'{len(guessed)}/50')
#     sanitized_answer = answer.title()
#     print(sanitized_answer)
#     check_answer(sanitized_answer,score)
#     pd.DataFrame(guessed).to_csv("guessed.csv")

# turtle.mainloop()
# import turtle
# import pandas

# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)

# data = pandas.read_csv("50_states.csv")
# all_states = data.state.to_list()
# guessed_states = []

# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
#                                     prompt="What's another state's name?").title()
#     if answer_state == "Exit":
#         missing_states = []
#         for state in all_states:
#             if state not in guessed_states:
#                 missing_states.append(state)
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states_to_learn.csv")
#         break
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(int(state_data.x), int(state_data.y))
#         t.write(answer_state)


