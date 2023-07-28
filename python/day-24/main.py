# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#     file.close()

with open("my_file.txt", mode="a") as file:
    file.write("\nI am a boy")