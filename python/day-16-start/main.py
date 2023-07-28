# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable
table = prettytable.PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows([["Pikachu", "Electric"], ["Squirtle", "Water"], ["Charmander", "Fire"]])
table.add_column(
    fieldname= "Test Column",
    column = ["Test Pikachu", "Test Powerful", "Mandatory"]
)
table.add_column("Added", ["name", "gender", "class"])
table.align = "l"
print(table)