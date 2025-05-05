import time

#reoccuring constants
choice_message = "Which path do you want to choose?"
invalid_choice_message = "That is not a valid choice. Please try again."

#function for print delay
def print_delay(message, delay=1):
    print(message)
    time.sleep(delay)

#choosing paths
def get_path_choice():
    path_choice = input(choice_message)
    while path_choice not in ["1", "2"]:
        path_choice = input(invalid_choice_message)
    return path_choice
#defining the intro story
def intro():
    global name
    name = input("What is your name?")
    print_delay(f"Welcome to the forest {name}.")
    print_delay("You have spent all day hiking. It is dark already. You try to get to the hill to sleep in the small house on top.")
    print_delay("You reach a crossroad. What path do you choose?")
    print_delay("1: You go straight through the forest. It is very dense and it is hard to see very far.")
    print_delay("2: You walk along the river. It is easier to walk along, but it will be way further.")
    path_choice = get_path_choice()
    return path_choice
    get_path_choice()
#defining path 1
def path_1():
    print_delay("You walk straight through the forest.")
    print_delay("The plants keep getting thicker and it becomes harder to move forward. ")
    print_delay("After a while you get very tired. But you find a small tree with a shiny red fruit. Do you want to eat it?")
    print_delay("1: Yes I'll try the mysterious fruit")
    print_delay("2: No, I'll stay safe")
    fruit_choice = input("Which fruit do you want to choose? (1 or 2)")
    while fruit_choice not in ["1", "2"]:
        fruit_choice = input("Invalid choice. Please only select between 1 and 2.")

    if fruit_choice == "1":
        print("The fruit tastes great. It rejuvenates you and you have lots of new energy")
    elif  fruit_choice == "2":
        print("Ok: You stay safe, but you are still very exhausted.")
    else:
        print("Please choose a number from 1 to 2.")
    time.sleep(1)
    print_delay("You continue your way. After a little while you hear something moving in the bushes")
    print_delay("The steps come much closer and then you see it. It's a large grizzly.")
    print_delay("What do you choose to do?")
    print_delay("1: You try to sneak away")
    print_delay("2: You try to calm the bear down with some nuts out of your bag")

    bear_choice = input("What do you choose? (1 or 2)")
    while bear_choice not in ["1", "2"]:
        bear_choice = input("Invalid choice. Please only select between 1 and 2.")
    if bear_choice == "1":
            print_delay("Oh no. It has seen you. Time to run!")
            print_delay("Where do you want to run?")
            print_delay("1: You try to hide on a tree")
            print_delay("2 You run into a nearby cave.")
            hide_choice = input("What do you choose? (1 or 2)")
            while hide_choice not in ["1", "2"]:
                hide_choice = input("Invalid choice. Please only select between 1 and 2.")
            if hide_choice == "1" and fruit_choice == "1":
                print("Great. Your fast and the grizzly can't reach you. After a while you can leave.")
            elif hide_choice == "1" and fruit_choice == "2":
                print_delay("You quickly try to run to the tree and jump on try to pull yourself up, but you're too tired...")
                print("The grizzly gets you. Game over..")
                quit()
            elif hide_choice == "2":
                 print("You quickly slide through the tiny holes in the cave. The bear is too big to fit. You escape.")
            else: print("Please choose a number from 1 to 2.")
    elif bear_choice == "2":
        print_delay("He slowly approaches you as you lay the handful of nuts out in front of him. He appears to be friendly and lays down on his back.")
        print_delay("1: You try to cuddle with him?")
        print_delay("2: You walk away.")
        cuddle_choice = input("What do you want to do? (1 or 2)")
        while cuddle_choice not in ["1", "2"]:
            cuddle_choice = input("What do you want to do? (1 or 2)")
        if cuddle_choice == "1":
            print_delay(f"Why would you try to cuddle with a grown grizzly, {name}? Not a good idea..")
            print_delay("He crushes you. Game over..")
            quit()
        elif cuddle_choice == "2":
            print("Smart choice. You continue on your way..")
        else: print("Please choose a number from 1 to 2.")
    else: print("Please choose a number from 1 to 2.")
#defining path 2
def path_2():
    print_delay("After a couple of moments you arrive by the water.")
    print_delay("The moon is clear as it reflects on the clear water.")
    print_delay("You can hear wolves howling from far away")
    print_delay("You feel a little thirsty. Do you want to have a drink from the water?")
    print_delay("1: Yes, you try to have a little.")
    print_delay("2: No, you rather stay away.")
    drink_choice = input("What do you want to do? (1 or 2)")
    while drink_choice not in ["1", "2"]:
        drink_choice = input("Invalid choice. Please only select between 1 and 2.")
    if drink_choice == "1":
        print_delay("You fill up your water")
        print_delay("After a little while your stomach starts to make weird noises")
        print_delay("There was something in the water. You start to feel a little sick.")
    elif drink_choice == "2":
        print("You don't drink anything and continue on your way..")
    else: print("Please choose a number from 1 to 2.")
    print_delay("After a little while the walking becomes harder and harder,...")
    print_delay("... as the trail slowly vanishes and you have to climb make your way through mud.")
    print_delay("You get tired and decide to take a rest. But its cold and you find some dry wood from a tree nearby")
    print_delay("1: You decide to make a little fire to warm yourself up")
    print_delay("2: You rather leave it.")
    fire_choice = input("What do you want to do? (1 or 2)")
    while fire_choice not in ["1", "2"]:
        fire_choice = input("Invalid choice. Please only select between 1 and 2.")
    if fire_choice == "1":
        print_delay("The fire feels good. Your warming up quickly.")
        print_delay("But as you sit there, you can here the wolves coming closer and closer.")
        print_delay("They seem to have noticed the fire from afar. What do you want to do")
        print_delay("1: You try to run away as fast as possible.")
        print_delay("2: You hide in the nearby bushes.")
        wolves_choice = input("What do you want to do? (1 or 2)")
        while wolves_choice not in ["1", "2"]:
            wolves_choice = input("Invalid choice. Please only select between 1 and 2.")
        if wolves_choice == "1" and drink_choice == "1":
            print_delay("You try to run away. But after a couple meters you lose your energy. You feel sick from the water")
            print_delay("The wolves catch you. Game over..")
            quit()
        elif wolves_choice == "1" and drink_choice == "2":
            print_delay("You try to run away and race up the water.")
            print_delay("You don't look behind and just keep running. After a while you cant hear them anymore.")
            print_delay("You got away...")
        elif wolves_choice == "2":
            print_delay("You hide behind a large bush and watch as the wolves reach the fire.")
            print_delay("The wolves try to smell you, but the smoke is limiting their senses.")
            print("You sneak away and continue your way up the river..")
        else: print("Please choose a number from 1 to 2.")
    elif fire_choice == "2" and drink_choice == "1":
        print_delay("You decide to keep going and not to take a rest.")
        print_delay("Your stomach keeps getting worse as you continue your way")
        print_delay("Your legs get weaker as you start to stumble from exhaustion")
        print_delay("You quickly lose your consciousness. ")
        print_delay("You will not be reaching the house today. Game over..")
        quit()
    elif fire_choice == "2" and drink_choice == "2":
        print_delay("You decide not to take a rest and continue")
        print_delay("Your tired but you keep going.")
    else: print("Please choose a number from 1 to 2.")
#defining the outro
def outro():
    print_delay("And then you can finally see it. A small house appears right on top of the hill.")
    print_delay("You get excited and use your last bits of energy to climb the last couple of steps.")
    print_delay("As you reach the top you see the last challenge..")
    print_delay("The house is located on the other side of river.")
    print_delay("You decide to place stones to step on them.")
    while True:
        try:
            stones = int(input("How many stones do you want to use (Choose a number from 0 to 10"))
            if 0 <= stones <= 10:
                break
            else:
                print("Please choose a number from 0 to 10.")
        except ValueError:
            print("This is not a number. Please choose a number from 0 to 10.")
    if stones <= 2:
        print_delay("You did not use enough stones. As you try to make the last jump, you fall into the river.")
        print_delay("Game over..")
        quit()
    elif stones >= 8:
        print_delay("You placed too many stones and have blocked the river.")
        print_delay("The water rises over the stones and flushes you in the water.")
        print_delay("Game over..")
        quit()
    else:
        print_delay("It works! You jump over the stones and cross the river safely")
    print_delay("You made it! You reach the house and finally can take a rest.")
    print_delay("Now get some well deserved sleep, because the next night is already coming")
    print_delay("Thanks for playing!!")
#Defining the main function
def main():
    path_choice = intro()
    if path_choice == "1":
        path_1()
    elif path_choice == "2":
        path_2()
    outro()

main()
