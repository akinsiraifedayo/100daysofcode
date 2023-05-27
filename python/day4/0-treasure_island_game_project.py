# Author: Ifedayo Akinsira-Olumide
print("Welcome to Treasure Island\nYour Mission is to FInd the Treasure")
decision = str.lower(input("\nYou are at a crossroad, where do you want to go?\n 'left' or 'right'\n"))
if decision == "left":
  decision = str.lower(input("\nYou take the left of the crossroad and the journey is quite enjoyable as it is peaceful\n all of a sudden you hear a roar of something really big and you can feel the whole ground shaking aggressively. What do you want to do? \n'run' or 'hide'\n"))

  if decision == "run":
    decision = str.lower(input("\nYou immediately start running as fast as possible with all your strength, you run really quick but you then get to a dead end.\nYou see a very brown river and also a canoe by the side. what is your decision?\n 'swim' , 'continue running' or 'take the canoe'\n"))

    if decision == "swim":
      decision = str.lower(input("\nYou start to swim but then you hear a very large splash in the water what do you want to do? 'stay still underwater' or 'swim faster'\n"))
      if decision == "stay still underwater":
        decision = str.lower(input("\nYou immediately stayed still underwater and the dinasour cannot see you because the water is brown\nIt swims past you and keeps going forward till it leaves the river and keeps going forward\nWhat do you want to do?\n 'swim back' or 'swim forward'\n"))
        if decision == "swim back":
          decision = str.lower(input("\nYou swim back and escape the pursuit of the dinasour! There's no other treasure more precious than your life. Congratulations\nDo not feel bad, if i offered you 1 trillion dollars but you would die tomorrow, I'm sure you'd stil choose your life over 1 trillion haha."))

        elif decision == "swim forward":
          print("\nYou decide to swim forward and the dinasour feels something is moving very far behind it. It runs to you and eats you!\n GAME OVER!\n")
          exit()
        else:
          print("You entered an incorrect input")
          exit()

      elif decision == "swim faster":
        print("\nYou decide to hide and anxiously wait for what made the roar and 30 seconds later a dinosaur comes and it immediately smells you and eats you\n GAME OVER!\n")
        exit()
      else:
        print("You entered an incorrect input")
        exit()

    elif decision == "continue running":
      print("\nYou continue running but the dinasour reaches the river and sees you from far, it catches up to you in an instant and eats you!\n GAME OVER!\n")
      exit()

    elif decision == "take the canoe":
      print("\nYou take the canoe but the dinasour reaches the river and sees you, It immediately locks onto you and smashes you to meat paste\nGAME OVER!\n")
      exit()
    else:
      print("You entered an incorrect input")
      exit()


  elif decision == "hide":
    print("\nYou decide to hide and anxiously wait for what made the roar and 30 seconds later a dinosaur comes and it immediately smells you and eats you\n GAME OVER!\n")
    exit()
  else:
    print("You entered an incorrect input")
    exit()


elif decision == "right":
  print("\nYou take the right turn but not long from when you took it, \nA dinosaur also takes the right turn, sees you and eats you.\n GAME OVER!\n")
  exit()
else:
  print("You entered an incorrect input")
  exit()


