class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def get_weakness(self):
        return self.weakness

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You kill " + self.name + " using a " + combat_item)
            return True
        else:
            print("You are killed by " + self.name)
            return False

    def steal(self):
        print("You steal from " + self.name)
        money = 0
        money = money + 1
        print("You now have $" + str(money))


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.respect = 0

    def get_respect(self):
        return self.respect

    def set_respect(self, respect):
        self.respect = respect

    def hug(self):
        print("You hug " + self.name)
        self.respect = self.respect + 1
        print("Your respect with " + self.name + " is now at " +
              str(self.respect))

    def gift(self):
        print("What would you like to gift?")
        gift = input()
        print("You gift " + self.name + " a " + gift)
        self.respect = self.respect + 2
        print("Your respect with " + self.name + " is now at " +
              str(self.respect))
