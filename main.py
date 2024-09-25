import turtle
import pandas


screen = turtle.Screen()
screen.title("US States")

image_url = r"\Users\maria\Documents\proyectos python\US-states-game\blank_states_img.gif"
screen.addshape(image_url)
turtle.shape(image_url)

count_states =0
game_is_on = True

answer_state = screen.textinput(title= f"{count_states}/50 States Correct", prompt="What´s another state´s name")


data = pandas.read_csv(r"C:\Users\maria\Documents\proyectos python\US-states-game\50_states.csv")
temp_list = data["state"].to_list()

def add_state():
    state_data = data[data['state'] == answer_state]
    x_coordinate = state_data.loc[0].at['x']
    y_coordinate = state_data.loc[0].at['y']
    new_state = turtle.Turtle()
    new_state.penup()
    new_state.hideturtle()
    new_state.goto(int(x_coordinate),int(y_coordinate))
    new_state.write(answer_state, align="center", font=("Courier", 10, "normal"))


while game_is_on:
    for state in temp_list:
        if answer_state == state:
            count_states += 1
            add_state()
            continue

        if count_states == 50:
            game_is_on=False

    answer_state = screen.textinput(title=f"{count_states}/50 States Correct", prompt="What´s another state´s name")

screen.exitonclick()