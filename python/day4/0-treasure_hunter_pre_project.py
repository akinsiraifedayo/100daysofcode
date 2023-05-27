# Author: Ifedayo Akinsira-Olumide
row1 = ["❤️", "❤️", "❤️"]
row2 = ["❤️", "❤️", "❤️"]
row3 = ["❤️", "❤️", "❤️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? \n")
rows = len(map[1])
columns = len(map)
if (int(position[0]) <= rows) and (int(position[1]) <= columns):
  horizontal = int(position[0])
  vertical = int(position[1])
  map[vertical - 1][horizontal - 1] = "🪙"
  print(f"{row1}\n{row2}\n{row3}")
else:
  print("You entered an unvalid input")
