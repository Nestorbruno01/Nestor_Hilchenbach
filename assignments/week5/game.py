# --- Game State ---
import time
def delay_print(message):
    print(message)
    time.sleep(2)
    pass

inventory = []

items_in_beach = [
    {"name": "Driftwood", "type": "material", "description": "Piece of wood from the water. Good for building", "Usability": True},
    {"name": "Coconut", "type": "food", "description": "Hydrating and nutritious. ", "Usability": True},
    {"name": "Bottle", "type": "tool", "description": "You can save some water or maybe send a message..", "Usability": False},
    {"name": "Seashell", "type": "material", "description": "beautiful, but not very useful. Nice to collect.", "Usability": False}
]
items_in_jungle = [
    {"name": "Vines", "type": "rope", "description": "Strong and flexible. Can be used to tie stuff.", "Usability": True},
    {"name": "Banana", "type": "food", "description": "Sweet and delicious.", "Usability": True},
    {"name": "Stick", "type": "material", "description": "Small piece of wood.", "Usability": True},
    {"name": "Rock", "type": "tool", "description": "Solid and heavy. Might be useful", "Usability": False},
]
items_at_cliff = [
    {"name": "old logs", "type": "material", "description": "The remains of an old fishermans house", "Usability": True},
    {"name": "Leaf", "type": "material", "description": "Could maybe used as a rain cover.", "Usability": False},
    {"name": "compass", "type": "navigator", "description": "Can guide you over the ocean. IF it works..", "Usability": True},
    {"name": "rope", "type": "rope", "description": "Use it to tie stuff together.", "Usability": True}
]


# length shall be larger than max inventory size if there is only one room
MAX_INVENTORY_SIZE = 5
rooms = {
    "beach": items_in_beach,
    "jungle": items_in_jungle,
    "cliff": items_at_cliff,
}
#define starting point
current_room = "beach"
# --- Functions ---
def move_to(location):
    global current_room

    if location in rooms:
        current_room = location
        print(f"You have moved to {current_room}")
    else:
        print("Location does not exist. Try Beach, Jungle or Cliff. ")

def show_inventory():
    print("Inventory:")
    for item in inventory:
        print(f"- {item['name']}")
    # list all names of items in the inventory, consider the case when the list is empty
    pass

def show_room_items():
    # list all items in current room
    for item in rooms[current_room]:
        print(f"- {item["name"]}")
    pass

def pick_up(item_name):
    global inventory
    room_items = rooms[current_room]
    # pick up an item from the room if inventory limit is not met yet
    item_to_pick = None
    for item in room_items:
        if item["name"].lower() == item_name.lower():
            item_to_pick = item
            break
    if not item_to_pick:
        print(f"There is no {item_name} at the {room}.")
        return
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your inventory is full. Drop something first.")
        return
    for owned_item in inventory:
        if owned_item["name"].lower() == item_name.lower():
            print(f"You already have {item_name} in your inventory.")
            return
    inventory.append(item_to_pick)
    print(f"You have picked up {item_name}.")
    pass


def drop(item_name):
    # drop an item from your inventory, at the same time append it back to the list of items for the room
    global inventory
    item_to_drop = None
    for item in inventory:
        if item["name"].lower() == item_name.lower():
            item_to_drop = item
            break
    if not item_to_drop:
        print(f"There is no {item_name} in the inventory.")
        return
    inventory.remove(item_to_drop)
    print(f"You dropped {item_name}.")
    pass

def examine(item_name):
    # you can only examine an item if it's in your inventory or if it is in the room
    room_items = rooms[current_room]
    examine_item = None
    for item in inventory + room_items:
        if item["name"].lower() == item_name.lower():
            examine_item = item
            break
    if not examine_item:
        print(f"There is no {item_name} in the inventory or this room.")
        return
    print(f"{item_name}:")
    print(f"-{examine_item['description']}")
    pass


def build_raft():
    # You need two pieces of wood and one type of string
    material_count = 0
    has_rope = False
    has_navigator = False
    has_food = False

    for item in inventory:
        if item["type"] == "material" and item["Usability"] is True:
            material_count += 1
        if item["type"] == "rope" and item["Usability"] is True:
            has_rope = True
        if item["type"] == "navigator" and item["Usability"] is True:
            has_navigator = True
        if item["type"] == "food" and item["Usability"] is True:
            has_food = True
    if material_count >= 2 and has_rope and has_navigator and has_food:
        delay_print("You have tied the material with the ropes together.")
        delay_print("Using the navigator you are able to get home. ")
        delay_print("You survive. THanks for playing!")
        exit()
    else:
        if material_count < 2:
            print("You might need more wooden materials to keep you afloat")
        if not has_rope:
            print("You might need something to tie everything together.")
        if not has_navigator:
            print("You have to have something to navigate across the ocean")
        if not has_food:
            print("It is a long journey, you might want to bring some snacks!")
    pass



# --- Game Loop ---

def game_loop():
    delay_print("Welcome to the Inventory Game!")
    delay_print("You are stranded on a small island in the middle of the ocean.")
    delay_print("There is a beach, a small jungle and a cliff. ")
    delay_print("To escape you will have to build a raft to get home.")
    delay_print("Good Luck, Adventurer")
    delay_print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            # You can also rename the commands according to your own needs
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], move to [room], build raft, quit")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:]
            pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:]
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
        elif command.startswith("examine "):
            item_name = command[8:]
            examine(item_name)
        elif command.startswith("move to "):
            room_name = command[8:]
            move_to(room_name)
        elif command == "build raft":
            build_raft()
        elif command == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()
