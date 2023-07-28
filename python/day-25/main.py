# # with open("weather data.csv", "r") as weather:
# #     weather_list = weather.readlines()
# #     weather_report = []
# #     for data in weather_list:
# #         data = data.strip()
# #         weather_report.append(data)
# # print(weather_list)
# # print(weather_report)
#
# # import csv
# # with open("weather data.csv") as data_file:
# #     temperatures = []
# #     data = csv.reader(data_file)
# #     for row in data:
# #         temperature = row[1]
# #         if row[1] != "temp":
# #             temperatures.append(int(temperature))
# # print(temperatures)
#
# import pandas
# # data = pandas.read_csv("weather data.csv")
# # data_dict = data.to_dict()
# # data_list = data["temp"].to_list()
# #
# # print(data["temp"].mean())
# # print(data["temp"].min())
# # print(data[data.temp == data.temp.max()])
# # print(data_dict)
# # print(data_list)
#
# # monday = data[data.day == "Monday"]
# # print(f"temperature is {((monday.temp[0]) * 9/5) + 32}F")
#
# my_dict = {
#     "students" : ["dayo", "lamidi", "tunde", "taiwo"],
#     "scores" : [24, 32, "NaN", 45],
# }
#
# data = pandas.DataFrame(my_dict)
# data.to_csv('broadsheet.csv')
# print(data)
#
import pandas

data = pandas.read_csv("squirell_data.csv")
fur_color = data["Primary Fur Color"]
# fur_color = fur_color.value_counts()
# fur_color.to_csv("fur_colors.csv")
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray = len(data[data["Primary Fur Color"] == "Gray"])

my_dict = {
    "Fur Color" : ["Black","Cinnamon", "Gray"],
    "Count" : [black, cinnamon, gray],
}
print(my_dict)
results = pandas.DataFrame(my_dict)
results.to_csv("results.csv")

print(black)