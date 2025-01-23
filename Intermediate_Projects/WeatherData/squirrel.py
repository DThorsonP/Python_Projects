"""
From Squirrel_Census.csv take the 'Primary Fur Color' column and 
use pandas to get a count total of each kind of squirrel and
put it into a new csv called squirrel_count.csv

"""

import pandas

data = pandas.read_csv("Squirrel_Census.csv")
gray_squirrels_count = len(data[data['Primary Fur Color'] == "Gray"])
black_squirrels_count = len(data[data['Primary Fur Color'] == "Black"])
red_squirrels_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
# print(gray_squirrels_count)
# print(black_squirrels_count)
# print(red_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
