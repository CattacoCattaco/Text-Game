answer = ""

items = []

permanent_items = []

injuries = []

health = 9

endings_collected = []
endings = ["Burning to death in chimney","Dying of self inflicted poison","Dying of self inflicted blunt force trauma","Dying from falling in a pit","Dying from sitting in glass","Dying from picking up glass","Cheating","Dying from falling into a very deep pit","Dying from jumping into a well","Surviving then burning to death in chimney"]

deaths_collected = []
deaths = ["Burning to death in chimney","Dying of self inflicted poison","Dying of self inflicted blunt force trauma","Dying from falling in a pit","Dying from sitting in glass","Dying from picking up glass","Cheating","Dying from falling into a very deep pit","Dying from jumping into a well","Surviving then burning to death in chimney"]

good_endings_collected = []
good_endings = []

new = True

def die():
  global health
  global answer
  global new
  print("\n\nYou died with:")
  for item in items:
    print(item)
  for item in permanent_items:
    print(item)
  print("\nYou sustained:")
  for injury in injuries:
    print(injury)
  print(f"\nEndings achieved:{len(endings_collected)}/{len(endings)}:")
  print(f"\tDeaths collected: {len(deaths_collected)}/{len(deaths)}")
  print(f"\tNon-deaths collected: {len(good_endings_collected)}/{len(good_endings)}")
  new_game_menu()

def new_game_menu():
  global health
  global answer
  global new
  print("\n"*3)
  continueing = input("Do you wish for another chance?: ")
  while continueing.lower() not in ["y", "yes", "sure", "yeah", "yes please", "n", "no", "nope", "nah", "no thanks"]:
    continueing = input("I'm sorry. May you please rephrase?: ")
  if continueing.lower() in ["y", "yes", "sure", "yeah", "yes please"]:
    new = False
    path_start()
  else:
    print("With that end, as many stories do, your story comes to a propper close. The end.")

def path_start():
  global health
  global answer
  global new
  global items
  global injuries
  health = 9
  items = []
  injuries = []
  if "Cheater's anguish" in permanent_items:
    health -= 6
    print("Those who cheat never prosper.")
    removing = input("Do you wish to reverse the curse by abandoning cheating?: ")
    while removing.lower() not in ["y", "yes", "sure", "yeah", "yes please", "n", "no", "nope", "nah", "no thanks"]:
      removing = input("I'm sorry. May you please rephrase?: ")
    if removing.lower() in ["y", "yes", "sure", "yeah", "yes please"]:
      permanent_items.remove("Cheater's anguish")
      print("You shall lose the curse if you don't continue to cheat.")
  if new is True:
    answer = input("You are a village idiot. Today you noticed that your doors, windows, and roof are all at odd angles. Do you:\nA: Go inside\nor\nB: Run away: ").upper()
  if new is False:
    answer = input("You are a village idiot. You just woke up and noticed that your doors, windows, and roof are all at odd angles. This feels familiar. Do you:\nA: Go inside\nor\nB: Run away: ").upper()
  while answer not in ["A", "B"]:
    answer = input("I'm sorry. May you please choose an option?: ")
  if answer == "A": 
    path_a()
  if answer == "B": 
    path_b()

def path_a(): 
  global health
  global answer
  global new
  global items
  global injuries
  answer = input("You go inside to find all of your belongings have been tampered with. Do you:\nA: Search for an intrudor within your house\nB: Go outside and seek out the criminal\nor\nC: Run away").upper()
  while answer not in ["A", "B", "C"]:
    answer = input("I'm sorry. May you please choose an option?: ")
  if answer == "A": 
    path_aa()
  if answer == "B": 
    path_ab()
  if answer == "C": 
    path_b()

def path_aa():
  global health
  global answer
  global new
  global items
  global injuries
  answer = input("The only thing you find is a card which you grab. Do you:\nA: Go outside and seek out the criminal\nB: Tear the card up\nor\nC: Run away: ").upper()
  items.append("Card")
  while answer not in ["A", "B", "C"]:
    answer = input("I'm sorry. May you please choose an option?: ")
  if answer == "A": 
    path_ab()
  if answer == "B": 
    path_aab()
  if answer == "C": 
    path_b()
 
def path_aab():
  global health
  global answer
  global new
  global items
  global injuries
  answer = input("You no longer have a card I guess. Do you:\nA: Go outside and seek out the criminal\nB: Explore your chimney\nor\nC: Run away: ").upper()
  items.remove("Card")
  while answer not in ["A", "B", "C"]:
    answer = input("I'm sorry. May you please choose an option?: ")
  if answer == "A": 
    path_ab()
  if answer == "B": 
    path_aabb()
  if answer == "C": 
    path_b()

def path_aabb():
  global health
  global answer
  global new
  global items
  global injuries
  if "Fire resistant armor" in permanent_items:
    health+=20
  health-=25
  injuries.append("Burning in chimney")
  if health <= 0:
    print("You crawl into your lit chimney and burn to death.")
    if "Burning to death in chimney" not in endings_collected:
      endings_collected.append("Burning to death in chimney")
      deaths_collected.append("Burning to death in chimney")
      print("\nEnding unlocked: Burning to death in chimney")
    die()
  else:
    answer = input("You crawl into your chimney and survive somehow maybe you should just stay since you've cheated death. Do you:\nA: Stay\nB: Stay\nor\nC: Stay: ").upper()
    if "Surviving then burning to death in chimney" not in endings_collected:
      endings_collected.append("Surviving then burning to death in chimney")
      deaths_collected.append("Surviving then burning to death in chimney")
      print("\nEnding unlocked: Surviving then burning to death in chimney")
    while answer not in ["A", "B", "C"]:
      answer = input("I'm sorry. May you please choose an option?: ")
    if answer == "A": 
      path_aabb()
    if answer == "B": 
      path_aabb()
    if answer == "C": 
      path_aabb()

def path_ab():
  global health
  global answer
  global new
  global items
  global injuries
  answer = input("You go out and find a rock. It looks kind of neat and shiny. Do you:\nA: Explore further\nB: Attempt to shatter the rock\nor\nC: Run away: ").upper()
  items.append("Rock")
  while answer not in ["A", "B", "C"]:
    answer = input("I'm sorry. May you please choose an option?: ")
  if answer == "A": 
    path_aba()
  if answer == "B": 
    path_abb()
  if answer == "C": 
    path_b()

def path_aba():
  global health
  global answer
  global new
  global items
  global injuries
  answer = input("You encounter a set of three berries. One is red, another is green, and another is purple. Do you:\nA: Eat the red one\nB: Eat the green one\nC: Eat the purple one\nD: Explore further\nor\nE: Run away: ").upper()
  items.append("Red berry")
  items.append("Green berry")
  items.append("Purple berry")
  while answer not in ["A", "B", "C", "D"]:
    answer = input("I'm sorry. May you please choose an option?: ")
  if answer == "A": 
    path_abaa()
  if answer == "B": 
    path_abab()
  if answer == "C": 
    path_abac()
  if answer == "D": 
    path_abad()
  if answer == "E": 
    path_b()

def path_abaa():
  global health
  global answer
  global new
  global items
  global injuries
  health+=2
  answer = input("You eat the red berry. You feel healthier. Do you:\nA: Continue\nor\nB: Run away: ").upper()
  items.remove("Red berry")
  while answer not in ["A", "B"]:
    answer = input("I'm sorry. May you please choose an option?: ")
  if answer == "A": 
    path_abad()
  if answer == "B": 
    path_b()

def path_abab():
  global health
  global answer
  global new
  global items
  global injuries
  answer = input("You eat the green berry. You feel nothing. Maybe this has another use. Do you:\nA: Explore further\nor\nB: Run away: ").upper()
  items.remove("Green berry")
  while answer not in ["A", "B"]:
    answer = input("I'm sorry. May you please choose an option?: ")
  if answer == "A": 
    path_abad()
  if answer == "B": 
    path_b()

def path_abac():
  global health
  global answer
  global new
  global items
  global injuries
  health-=3
  if health <= 0:
    print("You eat the purple berry and feel your health deteriate. You die.")
    if "Dying of self inflicted poison" not in endings_collected:
      endings_collected.append("Dying of self inflicted poison")
      deaths_collected.append("Dying of self inflicted poison")
      print("\nEnding unlocked: Dying of self inflicted poison")
    die()
  answer = input("You eat the purple berry and feel your health deteriate Do you:\nA: Explore further\nor\nB: Run away: ").upper()
  items.remove("Purple berry")
  while answer not in ["A", "B"]:
    answer = input("I'm sorry. May you please choose an option?: ")
  if answer == "A": 
    path_abad()
  if answer == "B":
    path_b()

def path_abad():
  global health
  global answer
  global new
  global items
  global injuries
  if "Green berry" in items:
    answer = input("You go further and find a well. You can't see the bottom. Do you:\nA: Throw the green berry in\nB: Explore further\nor\nC: Run away: ").upper()
    while answer not in ["A", "B", "C"]:
      answer = input("I'm sorry. May you please choose an option?: ")
    if answer == "A": 
      path_abada1()
    if answer == "B": 
      path_abadb()
    if answer == "C": 
      path_b()
  else:
    answer = input("You go further and find a well. You can't see the bottom. Do you:\nA: Jump in\nB: Explore further\nor\nC: Run away: ").upper()
    while answer not in ["A", "B", "C"]:
      answer = input("I'm sorry. May you please choose an option?: ")
    if answer == "A": 
      path_abada2()
    if answer == "B": 
      path_abadb()
    if answer == "C": 
      path_b()

def path_abada1():
  global health
  global answer
  global new
  global items
  global injuries
  answer = input("You throw the green berry in. Out comes an object. It appears to be a book. You read the cover one letter at a time. You read, \"C H E A T _ C O D E S . T X T\". You don't know what it means. Do you:\nA: Jump in the well\nB: Explore further\nor\nC: Run away: ").upper()
  items.append("cheat_codes.txt")
  while answer not in ["A", "B", "C"]:
    answer = input("I'm sorry. May you please choose an option?: ")
  if answer == "A": 
    path_abaa()
  if answer == "B": 
    path_abac()
  if answer == "C": 
    path_b()

def path_abada2():
  global health
  global answer
  global new
  global items
  global injuries
  health-=191
  injuries.append("Jumping into well")
  if health <= 0:
    print("You jump into the well. You die.")
    if "Dying from jumping into a well" not in endings_collected:
      endings_collected.append("Dying from jumping into a well")
      deaths_collected.append("Dying from jumping into a well")
      print("\nEnding unlocked: Dying from jumping into a well")
    die()
  else:
    answer = input("You throw the rock at your head. You are weak now. Do you:\nA: Explore further\nB: Attempt to shatter the rock again\nor\nC: Run away: ").upper()
    while answer not in ["A", "B", "C"]:
      answer = input("I'm sorry. May you please choose an option?: ")
    if answer == "A": 
      path_aba()
    if answer == "B": 
      path_abb()
    if answer == "C": 
      path_b()

def path_abadb():
  global health
  global answer
  global new
  global items
  global injuries
  health-=191
  injuries.append("Falling into pit")
  permanent_items.append("Feather")
  if health <= 0:
    print("You explore further but unfortunately you fall into a very deep pit. On your way down you do find a feather and put it into your pocket though so that's nice.")
    if "Dying from falling into a very deep pit" not in endings_collected:
      endings_collected.append("Dying from falling into a very deep pit")
      deaths_collected.append("Dying from falling into a very deep pit")
      print("\nEnding unlocked: Dying from falling into a very deep pit")
    die()
  else:
    answer = input("You throw the rock at your head. You are weak now. Do you:\nA: Explore further\nB: Attempt to shatter the rock again\nor\nC: Run away: ").upper()
    while answer not in ["A", "B", "C"]:
      answer = input("I'm sorry. May you please choose an option?: ")
    if answer == "A": 
      path_aba()
    if answer == "B": 
      path_abb()
    if answer == "C": 
      path_b()

def path_abb():
  global health
  global answer
  global new
  global items
  global injuries
  health-=5
  injuries.append("Throwing shiny rock at head")
  if "Rock" in items:
    items.remove("Rock")
    items.append("Broken rock")
  else:
    items.remove("Broken rock")
    items.append("Broken-er rock")
  if health <= 0:
    print("You throw the rock at your head. It causes you to die.")
    if "Dying of self inflicted blunt force trauma" not in endings_collected:
      endings_collected.append("Dying of self inflicted blunt force trauma")
      deaths_collected.append("Dying of self inflicted blunt force trauma")
      print("\nEnding unlocked: Dying of self inflicted blunt force trauma")
    die()
  else:
    answer = input("You throw the rock at your head. You are weak now. Do you:\nA: Explore further\nB: Attempt to shatter the rock again\nor\nC: Run away: ").upper()
    while answer not in ["A", "B", "C"]:
      answer = input("I'm sorry. May you please choose an option?: ")
    if answer == "A": 
      path_aba()
    if answer == "B": 
      path_abb()
    if answer == "C": 
      path_b()

def path_b():
  global health
  global answer
  global new
  global items
  global injuries
  health-=3
  injuries.append("Falling in a pit")
  if health <= 0:
    print("You run away. You're almost out when you fall into a pit of glass shards. You die from your combined injuries.")
    if "Dying from falling in a pit" not in endings_collected:
      endings_collected.append("Dying from falling in a pit")
      deaths_collected.append("Dying from falling in a pit")
      print("\nEnding unlocked: Dying from falling in a pit")
    die()
  else:
    answer = input("You run away. You're almost out when you fall into a pit of glass shards. You are weak now. Do you:\nA: Attempt to get up\nB: Sit\nor\nC: Pick up a shard: ").upper()
    while answer not in ["A", "B", "C"]:
      answer = input("I'm sorry. May you please choose an option?: ")
    if answer == "A": 
      path_ba()
    if answer == "B": 
      path_bb()
    if answer == "C": 
      path_bc()

def path_ba():
  global health
  global answer
  global new
  global items
  global injuries
  answer = input("You get up. You notice two doors, a statue, and an unlit torch around. Do you:\nA: Go through the left door\nB: Go through the right door\nC: Look at the statue\nor\nD: Attempt to grab the torch: ").upper()
  while answer not in ["A", "B", "C", "D"]:
    answer = input("I'm sorry. May you please choose an option?: ")
  if answer == "A": 
    path_baa()
  if answer == "B": 
    path_bab()
  if answer == "C": 
    path_bac()
  if answer == "D": 
    path_bad()

def path_baa():
  global health
  global answer
  global new
  global items
  global injuries
  answer = input("You go through the left door. . Do you:\nA: Go through the left door\nB: Go through the right door\nC: Look at the statue\nor\nD: Attempt to grab the torch: ").upper()
  while answer not in ["A", "B", "C", "D"]:
    answer = input("I'm sorry. May you please choose an option?: ")
  if answer == "A": 
    path_baa()
  if answer == "B": 
    path_bab()
  if answer == "C": 
    path_bac()
  if answer == "D": 
    path_bad()

def path_bb():
  global health
  global answer
  global new
  global items
  global injuries
  health -= 2
  injuries.append("Sitting in glass")
  if health > 5:
    answer = input("You sit there and bleed out a bit. Other than that, nothing changes. Do you:\nA: Attempt to get up\nB: Sit\nor\nC: Pick up a shard: ").upper()
    while answer not in ["A", "B", "C"]:
      answer = input("I'm sorry. May you please choose an option?: ")
    if answer == "A": 
      path_ba()
    if answer == "B": 
      path_bb()
    if answer == "C": 
      path_bc()
  elif health > 3:
    answer = input("You sit there and bleed out. You should maybe get up at some point. Do you:\nA: Attempt to get up\nB: Sit\nor\nC: Pick up a shard: ").upper()
    while answer not in ["A", "B", "C"]:
      answer = input("I'm sorry. May you please choose an option?: ")
    if answer == "A": 
      path_ba()
    if answer == "B": 
      path_bb()
    if answer == "C": 
      path_bc()
  elif health > 0:
    answer = input("You sit there and bleed out some more. You should probably get up. Do you:\nA: Attempt to get up\nB: Sit\nor\nC: Pick up a shard: ").upper()
    while answer not in ["A", "B", "C"]:
      answer = input("I'm sorry. May you please choose an option?: ")
    if answer == "A": 
      path_ba()
    if answer == "B": 
      path_bb()
    if answer == "C": 
      path_bc()
  else:
    print("You sit for some more time and bleed to death.")
    if "Dying from sitting in glass" not in endings_collected:
      endings_collected.append("Dying from sitting in glass")
      deaths_collected.append("Dying from sitting in glass")
      print("\nEnding unlocked: Dying from sitting in glass")
    die()

def path_bc():
  global health
  global answer
  global new
  global items
  global injuries
  health -= 6
  injuries.append("Picking up glass shards")
  if health <= 0:
    print("You cut your hand while picking up the glass shard and drop it. You try again and again until you have bled to death.")
    items.append("Shard")
    if "Dying from picking up glass" not in endings_collected:
      endings_collected.append("Dying from picking up glass")
      deaths_collected.append("Dying from picking up glass")
      print("\nEnding unlocked: Dying from picking up glass")
    die()
  else:
    answer = input("You cut your hand while picking up the glass shard and drop it. You try again and again until you just give up. You suddenly realise that it has turned to night. The door to a new path has opened. Do you:\nA: Attempt to get up\nB: Sit\nor\nC: Check what you have in your bag: ").upper()
    while answer not in ["A", "B", "C"]:
      answer = input("I'm sorry. May you please choose an option?: ")
    if answer == "A": 
      path_bca()
    if answer == "B": 
      path_bcb()
    if answer == "C": 
      path_bcc()

def path_bcb():
  global health
  global answer
  global new
  global items
  global injuries
  health -= 2
  injuries.append("Sitting in glass")
  if health > 5:
    answer = input("You sit there and bleed out a bit. Other than that, nothing changes. Do you:\nA: Attempt to get up\nB: Sit\nor\nC: Pick up a shard: ").upper()
    while answer not in ["A", "B", "C"]:
      answer = input("I'm sorry. May you please choose an option?: ")
    if answer == "A": 
      path_bca()
    if answer == "B": 
      path_bcb()
    if answer == "C": 
      path_bc()
  elif health > 3:
    answer = input("You sit there and bleed out. You should maybe get up at some point. Do you:\nA: Attempt to get up\nB: Sit\nor\nC: Pick up a shard: ").upper()
    while answer not in ["A", "B", "C"]:
      answer = input("I'm sorry. May you please choose an option?: ")
    if answer == "A": 
      path_bca()
    if answer == "B": 
      path_bcb()
    if answer == "C": 
      path_bc()
  elif health > 0:
    answer = input("You sit there and bleed out some more. You should probably get up. Do you:\nA: Attempt to get up\nB: Sit\nor\nC: Pick up a shard: ").upper()
    while answer not in ["A", "B", "C"]:
      answer = input("I'm sorry. May you please choose an option?: ")
    if answer == "A": 
      path_bca()
    if answer == "B": 
      path_bcb()
    if answer == "C": 
      path_bc()
  else:
    print("You sit for some more time and bleed to death.")
    if "Dying from sitting in glass" not in endings_collected:
      endings_collected.append("Dying from sitting in glass")
      deaths_collected.append("Dying from sitting in glass")
      print("\nEnding unlocked: Dying from sitting in glass")
    die()

def path_bcc():
  global health
  global answer
  global new
  global items
  global injuries
  if "cheat_codes.txt" in items:
    cheating = input("You get the sudden urge to use the book you found in the well. Another part of you wonders if this could have negative consequences. Do you use it?: ")
    while cheating.lower() not in ["y", "yes", "sure", "yeah", "yes please", "n", "no", "nope", "nah", "no thanks"]:
      cheating = input("I'm sorry. May you please rephrase?: ")
    if cheating.lower() in ["y", "yes", "sure", "yeah", "yes please"]:
      health+=8*8*8*8*8*8*8*8
      print("")
  health -= 70
  injuries.append("Picking up glass shards")
  if health <= 0:
    print("You cut your hand while picking up the glass shard and drop it. You try again and again until you have bled to death.")
    items.append("Shard")
    if "Dying from picking up glass" not in endings_collected:
      endings_collected.append("Dying from picking up glass")
      deaths_collected.append("Dying from picking up glass")
      print("\nEnding unlocked: Dying from picking up glass")
    die()
  else:
    print("You check what you have in your bag. You do so very slowly You are bleeding. You should DIE. You have clearly cheated though so you don't. Good job. You cheated. Joke's on you. All you get is increased vulnarability. Maybe that's actually what you need though. You pass out")
    permanent_items.append("Cheater's anguish")
    if "Cheating" not in endings_collected:
      endings_collected.append("Cheating")
      deaths_collected.append("Cheating")
      print("\nEnding unlocked: Cheating")
    die()

path_start()