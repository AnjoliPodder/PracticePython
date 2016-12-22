'''
Solution by: Anjoli Podder
December 2016

http://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/08_ClassDesign/Adventure/Project10.pdf

You will write a very simple text adventure game. As designed, it
contains no puzzles, and your program’s responses are not required to be clever.
Your program must consist of four classes: TextAdventure, Room, Character, and an
Exception subclass. You must also have a main() function designed to run the game.
'''

# text_desc must contain, in order, the integer id of the room, the adjective that describes the
# room, and a mix of strings which may describe exits or items in the room
# For example "white S17 feather curtain paintbrush W18 E20"


class Character:
    def __init__(self, inventory_list=[], room_id=-1):
        self.inventory_list = inventory_list
        self.room_id = room_id

    def get_inventory(self):
        if not self.inventory_list:
            return "You are not carrying anything"
        if len(self.inventory_list) == 1:
            return "You are carrying a " + self.inventory_list[0] + ". "
        else:
            inv_string = "You are carrying "
            for ix, i in enumerate(self.inventory_list):
                if ix == len(self.inventory_list) - 1:
                    inv_string += "and a " + i + ". "
                else:
                    inv_string += "a " + i + ", "
            return inv_string


class Room:
    def __init__(self, text_desc="0 bare"):
        room_info = text_desc.split(" ")
        self.roomid = 0
        self.exits = {}
        self.items = []
        self.adjective = ""
        for ix, el in enumerate(room_info):
            if len(el) == 0:
                pass
            elif ix == 0:
                self.roomid = el
            elif ix == 1:
                self.adjective = el
            elif el[0] in "NSEW":
                self.exits[el[0]] = el[1:len(el)+1]
            else:
                self.items.append(el)

    def desc_exits(self):
        directions = []
        for e in self.exits:
            if e == "N":
                directions.append("north")
            elif e == "S":
                directions.append("south")
            elif e == "E":
                directions.append("east")
            elif e == "W":
                directions.append("west")
        if not directions:
            return "There are no exits here. "
        elif len(directions) == 1:
            return "There is an exit to the " + directions[0] + ". "
        else:
            exit_string = "There are exits to the "
            for ix, d in enumerate(directions):
                if ix == len(directions)-1:
                    exit_string += "and " + d + ". "
                else:
                    exit_string += d + ", "
            return exit_string

    def desc_items(self):
        if not self.items:
            return "There are no items here. "
        elif len(self.items) == 1:
            return "You see a " + self.items[0] + ". "
        else:
            exit_string = "You see "
            for ix, e in enumerate(self.items):
                if ix == len(self.items)-1:
                    exit_string += "and a " + e + ". "
                else:
                    exit_string += "a " + e + ", "
            return exit_string

    def desc_room(self):
        return "You are in a " + self.adjective + " room.\n" + self.desc_items() + "\n" + self.desc_exits()


class TextAdventure:
    def __init__(self, filename):
        game = open(filename, "r")
        game_lines = game.readlines()
        self.rooms = {}
        for ix, line in enumerate(game_lines):
            room = Room(line.replace("\n", ""))
            self.rooms[room.roomid] = room
        game.close()
        self.character = Character(room_id=min(list(self.rooms.keys())))

    def look(self):
        roomid = self.character.room_id
        room = self.rooms[roomid]
        print(room.desc_room())
        return

    def inventory(self):
        return self.character.get_inventory()

    def drop(self, item):
        if item in self.character.inventory_list:
            self.character.inventory_list.remove(item)
            self.rooms[self.character.room_id].items.append(item)
            print("You dropped the %s." % item)
        else:
            print("You're not carrying a %s" % item)

    def pickup(self, item):
        if item in self.rooms[self.character.room_id].items:
            self.rooms[self.character.room_id].items.remove(item)
            self.character.inventory_list.append(item)
            print("You picked up the %s." % item)
        else:
            print("You can't see a %s in this room." % item)

    def move(self, direction):
        if direction in self.rooms[self.character.room_id].exits:
            self.character.room_id = self.rooms[self.character.room_id].exits[direction]
            print("You moved %s." % direction)
            print(self.rooms[self.character.room_id].desc_room())
        else:
            print("There is no exit that way.")

    def help(self):
        print("Here are a list of valid commands:\n"
              "L or look - print a description of the room you are in\n"
              "I or inventory - print your inventory\n"
              "P blah or pickup blah - pick up the item called blah\n"
              "D blah or drop blah - drop the item called blah\n"
              "N or north - go north\n"
              "S or south - go south\n"
              "E or east - go east\n"
              "W or west - go west\n"
              "Q or quit - quit\n"
              "H or help - print this list of commands\n")

    def prompt(self):
        actions = input("Enter a command (H for help): ").split(" ")
        if len(actions) == 0 or len(actions) > 2:
            print("That was not a valid move")
            return False
        elif actions[0].lower() in ["l", "look"]:
            self.look()
            return False
        elif actions[0].lower() in ["i", "inventory"]:
            self.inventory()
            return False
        elif actions[0].lower() in ["n", "north"]:
            self.move("N")
            return False
        elif actions[0].lower() in ["s", "south"]:
            self.move("S")
            return False
        elif actions[0].lower() in ["e", "east"]:
            self.move("E")
            return False
        elif actions[0].lower() in ["w", "west"]:
            self.move("W")
            return False
        elif actions[0].lower() in ["h", "help"]:
            self.help()
            return False
        elif actions[0].lower() in ["q", "quit"]:
            print("Thanks for playing! Bye for now.\n")
            return True
        elif len(actions) == 1:
            print("That was an invalid move")
            return False
        elif actions[0].lower() in ["p", "pickup"]:
            self.pickup(actions[1])
            return False
        elif actions[0].lower() in ["d", "drop"]:
            self.drop(actions[1])
            return False
        else:
            print("That was an invalid move")
            return False


def main():
    while True:
        filename = input("Enter a text adventure filename: ")
        try:
            ta = TextAdventure(filename)
            break
        except FileNotFoundError:
            print("There is no file called %s" % filename)
    print("Welcome to this Generic Text Adventure!\n"
          "You may explore and collect any items you find.\n"
          "There's no winning, just exploration.\n"
          "Valid commands are:\n"
          "L or look - print a description of the room you are in\n"
          "I or inventory - print your inventory\n"
          "P blah or pickup blah - pick up the item called blah\n"
          "D blah or drop blah - drop the item called blah\n"
          "N or north - go north\n"
          "S or south - go south\n"
          "E or east - go east\n"
          "W or west - go west\n"
          "Q or quit - quit\n"
          "H or help - print this list of commands\n\n"
          "Capitalization doesn't matter\n")
    ta.look()
    quitnow = False
    while not quitnow:
        quitnow = ta.prompt()

if __name__ == "__main__":
    main()
