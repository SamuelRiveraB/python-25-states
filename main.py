# with open('weather_data.csv') as data:
#     weather = data.readlines()
#
#     print(weather)

# import csv
# with open('weather_data.csv') as data:
#     wt = csv.reader(data)
#     temps = []
#     for row in data:
#         temps.append(row)
#     print(temps)

import pandas

# data = pandas.read_csv('weather_data.csv')
# temp_list = data["temp"].to_list()
# print(data['temp'].max())
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp_f = monday.temp * 9/5 + 32
# print(monday_temp_f)

# data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
#
# cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
# gray = len(data[data["Primary Fur Color"] == "Gray"])
# black = len(data[data["Primary Fur Color"] == "Black"])
#
# print(cinnamon)
# print(gray)
# print(black)
#
# data_dic = {
#     "Fur Color": ["Cinnamon", "Gray", "Black"],
#     "Count": [cinnamon, gray, black]
# }
#
# df = pandas.DataFrame(data_dic)
# df.to_csv("squirrel_count.csv")

from turtle import Screen
import turtle

screen = Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=491)
img = "blank_states_img.gif"
screen.bgpic(img)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

guessed = []

while len(guessed) < 50:
    answer = screen.textinput(title=f"{len(guessed)}/50 States Guessed", prompt="What's another states' name?").title()
    if answer == "Exit":
        missing_states = []
        for st in states:
            if st not in guessed:
                missing_states.append(st)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in states and answer not in guessed:
        guessed.append(answer)
        text = turtle.Turtle()
        text.hideturtle()
        text.up()
        state = data[data.state == answer]
        text.goto(int(state.x), int(state.y))
        text.write(state.state.item())


turtle.mainloop()

