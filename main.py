import turtle
import pandas
screen = turtle.Screen()
screen.title("US States")

image_url = "\\Users\maria\Documents\proyectos python\\US-states-game\\blank_states_img.gif"
screen.addshape(image_url)
turtle.shape(image_url)

count_states =0
answer_state = screen.textinput(title= f"{count_states}/50 States Correct", prompt="What´s another state´s name")

data =pandas.read_csv(r"C:\Users\maria\Documents\proyectos python\US-states-game\blank_states_img.gif")
print(data)


screen.exitonclick()