#world rules
yes_no = ["yes","no"]
directions = ["left","right","forward","backward"]

#introduction
print("The sound of an AC kicking on wakes you.\n")
#time.sleep(2)
print("A moment later, the soft dripping sounds of water from above pitter patter beside you.\n")
print("You find yourself on the ground in a dark damp alley.\n")
name = input("A voice whispers in your head. 'Who are you?'\n\n")
print("\n")
print("'Hmm, " + name + ".'\n")
#time.sleep(3)
print("When the voice speaks again, it feels as if it's right behind you. 'What a mundane title. Did you choose it yourself?', it hisses.\n")
print("You turn around but nothing is there. It chuckles and the sound fades further into the darkness of the alleyway.\n")
#time.sleep(5)
print("'GET UP. GET UP. GET UP. GET UP.' The voice screams into your ear, right beside you.\n")
print("You jump to your feet. You are alone.\n")

#call to action
while True:
  response = ""
  response = input("The alley is damp but comfortable. It would be a shame to leave. What do you do?\n").lower()
  if response == "leave":
      print("'Fool.' You step away from the cool brick and look out towards the street.\n\n")
  elif response == "stay":
    print("You sit back down beneath the dripping AC unit and listen to the steady drops of water fall beside you. After a while, you feel comfortable in that cold dark.\n...\n..\n.")
    quit()
  else:
    print("A soft chuckle whispers against your cheek. 'Do you stay or leave, " + name + "?'\n\n")
    continue
  break


#part 1: a beginning
