# with open("weather_data.csv", "r") as data_file:
#     weather_data = data_file.readlines()
#     print(weather_data)

# import csv
#
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)

data_dict_one = data.to_dict()
# print(data_dict_one)

temp_list = data["temp"].to_list()
# print(temp_list)


# Get Row Data
row = data[data.day == "Monday"]
# print(row)

# Row with the highest temp
tmpr = data[data.temp == data.temp.max()]
print(tmpr)

high_temp_day = tmpr.day
# print(high_temp_day)

monday = data[data.day == "Monday"]
# print(monday)
far_temp = monday.temp * 1.8 + 32
print(far_temp)

# Create a dataframe from scratch

data_dict_two = {
    "students": ["Amy", "Adam", "Angela"],
    "scores": [76, 34, 55]
}

data = pandas.DataFrame(data_dict_two)
data.to_csv("new_data.csv")
