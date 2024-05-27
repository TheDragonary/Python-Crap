from room import Room
from character import Enemy
from character import Friend

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

dining_hall = Room("Dining Hall")
dining_hall.set_description(
    "A large room with ornate golden decorations on each wall")

ballroom = Room("Ballroom")
ballroom.set_description(
    "A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

print("There are " + str(Room.number_of_rooms) + " rooms to explore")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("gun")

skelly = Friend("Skelly", "A cool skeleton")
skelly.set_conversation("Rattle me bones!")
skelly.set_respect(0)

dining_hall.set_character(dave)
ballroom.set_character(skelly)

current_room = kitchen
dead = False
while dead == False:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        print("What do you want to say?")
        text = input()
        print('You say "' + text + '" to ' + inhabitant.name)
        inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                # What happens if you win?
                print("You defeated the enemy!")
                current_room.set_character(None)
            else:
                # What happens if you lose?
                print("Game Over")
                dead = True
        elif inhabitant is not None and isinstance(inhabitant, Friend):
            print(inhabitant.name + " doesn't want to fight with you")
        else:
            print("There is no one here to fight with")
    elif command == "hug":
        if inhabitant is not None and isinstance(inhabitant, Friend):
            inhabitant.hug()
        elif inhabitant is not None and isinstance(inhabitant, Enemy):
            print(
                "You go to hug " + inhabitant.name +
                " and you feel a sharp pain in your chest. You are bleeding out. This is why you don't hug enemies!"
            )
            dead = True
        else:
            print(
                "There's no one to hug so you hug yourself. Loner."
            )
    elif command == "gift":
        if inhabitant is not None and isinstance(inhabitant, Friend):
            inhabitant.gift()
        elif inhabitant is not None and isinstance(inhabitant, Enemy):
            print(
                "You thought you could befriend " + inhabitant.name +
                " by giving them a gift. Surely they'll be your friend now. WRONG! "
                + inhabitant.name + " rejects your gift and kills you")
            dead = True
        else:
            print("What would you like to gift?")
            gift = input()
            print(
                "You take out a " + gift +
                " from your inventory, wrap it up in a gift box, give it to yourself and unwrap it. "
                + gift.capitalize() +
                " has been added back into your inventory. You should try giving it to a friend if you have any."
            )