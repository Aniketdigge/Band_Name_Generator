import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240101.csv")

count = data.value_counts("Primary Fur Color")

data_dict = {
    "color":["Gray", "Cinnamon", "Black"],
    "count":[count[0], count[1], count[2]]
}

Squirrel_data = pandas.DataFrame(data_dict)
Squirrel_data.to_csv("squirrel_count.csv")

#Fur color, count, squirrel_count.csv