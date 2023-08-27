import turtle as t
import pandas
screen = t.Screen()
img = 'blank_states_img.gif'
t.addshape(img)
bg = t.shape(img)



pen = t.Turtle()
pen.hideturtle()
pen.hideturtle()
count = 0
data = pandas.read_csv('50_states.csv')
states = data['state'].to_list()
while count < 50:
    state = (screen.textinput(prompt="ENTER A STATE",title="Guess a state")).title()
    print(state)

    if state in states:
        pen.penup()
        row = data[data['state'] == state]
        pen.goto(int(row.x), int(row.y))
        pen.pendown()
        pen.write(state,font=('Arial', 8, 'normal'))
        states.remove(state)
        count += 1
screen.exitonclick()