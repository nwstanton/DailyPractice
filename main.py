import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(750, 500)
turtle.shape(image)


guessed_states = []
states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()

print(all_states)
while len(guessed_states) <50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 guessed", prompt="whats another states name")
    answer_state = answer_state.title()

    if answer_state in all_states:
        state_lbl = turtle.Turtle()
        state_lbl.hideturtle()
        state_lbl.penup()
        state_cor = states_data[states_data.state == answer_state]
        state_lbl.goto(int(state_cor.x), int(state_cor.y))
        state_lbl.write(f"{answer_state}")
        guessed_states.append(answer_state)
        all_states.remove(answer_state)
    elif answer_state == "Exit":
        break
output_file = pandas.DataFrame(all_states)
output_file.to_csv("states_to_learn.csv")


screen.exitonclick()