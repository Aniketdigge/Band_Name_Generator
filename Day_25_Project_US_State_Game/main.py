import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()

Is_game_on = True

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
Correct_guess = []
Score = 0

while(len(Correct_guess) < 50):
    answer_state = screen.textinput(title=f"{len(Correct_guess)}/50 Correct State", prompt=f"What's another state's name?")
    #answer_state = "ohio"
    title_answer_state = answer_state.title()

    if(title_answer_state == "Exit"):
        data_dict = {
            "States To Learn":[]
        }
        for state_to_learn in all_state:
            if state_to_learn not in Correct_guess:
                data_dict["States To Learn"].append(state_to_learn)
                
        State_data = pandas.DataFrame(data_dict)
        State_data.to_csv("state_to_learn.csv")
        break
        

    if(title_answer_state in all_state):
        Correct_guess.append(title_answer_state)
        answer = data[data.state == title_answer_state]
        X = int(answer["x"])
        Y = int(answer["y"])
        Txt = turtle.Turtle()
        Txt.hideturtle()
        Txt.speed('slowest')
        Txt.penup()
        Txt.goto(X, Y)
        Txt.pendown()
        Txt.write(title_answer_state)


#state_to_learn.csv

