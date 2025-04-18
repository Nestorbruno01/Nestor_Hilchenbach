import time
name = input("What is your name?")
print(f"Welcome to the forest {name}.")
time.sleep(1)
print("You have spent all day hiking. It is dark already. You try to get to the hill to sleep in the small house on top.")
time.sleep(1)
print("You reach a crossroad. What path do you choose?")
time.sleep(1)
print("1: You go straight through the forest. It is very dense and it is hard to see very far.")
time.sleep(1)
print("2: You walk along the river. It is easier to walk along, but it will be way further.")
time.sleep(1)
path_choice = input("Which path do you want to choose?")
while path_choice not in ["1", "2"]:
    path_choice = input("Invalid choice. Please only select between 1 and 2.")

if path_choice == "1":
    print("You walk straight through the forest.")
    time.sleep(1)
    print("The plants keep getting thicker and it becomes harder to move forward. ")
    time.sleep(1)
    print("After a while you get very tired. But you find a small tree with a shiny red fruit. Do you want to eat it?")
    time.sleep(1)
    print("1: Yes I'll try the mysterious fruit")
    time.sleep(1)
    print("2: No, I'll stay safe")

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
    print("You continue your way. After a little while you hear something moving in the bushes")
    time.sleep(1)
    print("The steps come much closer and then you see it. It's a large grizzly.")
    time.sleep(1)
    print("What do you choose to do?")
    time.sleep(1)
    print("1: You try to sneak away")
    time.sleep(1)
    print("2: You try to calm the bear down with some nuts out of your bag")
    time.sleep(1)

    bear_choice = input("What do you choose? (1 or 2)")
    while bear_choice not in ["1", "2"]:
        bear_choice = input("Invalid choice. Please only select between 1 and 2.")

    if bear_choice == "1":
            print("Oh no. It has seen you. Time to run!")
            time.sleep(1)
            print("Where do you want to run?")
            time.sleep(1)
            print("1: You try to hide on a tree")
            time.sleep(1)
            print("2 You run into a nearby cave.")
            hide_choice = input("What do you choose? (1 or 2)")
            while hide_choice not in ["1", "2"]:
                hide_choice = input("Invalid choice. Please only select between 1 and 2.")
            if hide_choice == "1" and fruit_choice == "1":
                print("Great. Your fast and the grizzly can't reach you. After a while you can leave.")
            elif hide_choice == "1" and fruit_choice == "2":
                print("You quickly try to run to the tree and jump on try to pull yourself up, but you're too tired...")
                time.sleep(1)
                print("The grizzly gets you. Game over..")
                quit()
            elif hide_choice == "2":
                 print("You quickly slide through the tiny holes in the cave. The bear is too big to fit. You escape.")
            else: print("Please choose a number from 1 to 2.")
    elif bear_choice == "2":
        print("He slowly approaches you as you lay the handful of nuts out in front of him. He appears to be friendly and lays down on his back.")
        time.sleep(1)
        print("1: You try to cuddle with him?")
        time.sleep(1)
        print("2: You walk away.")
        cuddle_choice = input("What do you want to do? (1 or 2)")
        while cuddle_choice not in ["1", "2"]:
            cuddle_choice = input("What do you want to do? (1 or 2)")
        if cuddle_choice == "1":
            print(f"Why would you try to cuddle with a grown grizzly, {name}? Not a good idea..")
            time.sleep(1)
            print("He crushes you. Game over..")
            quit()
        elif cuddle_choice == "2":
            print("Smart choice. You continue on your way..")
        else: print("Please choose a number from 1 to 2.")
    else: print("Please choose a number from 1 to 2.")
elif path_choice == "2":
    print("After a couple of moments you arrive by the water.")
    time.sleep(1)
    print("The moon is clear as it reflects on the clear water.")
    time.sleep(1)
    print("You can hear wolves howling from far away")
    time.sleep(1)
    print("You feel a little thirsty. Do you want to have a drink from the water?")
    time.sleep(1)
    print("1: Yes, you try to have a little.")
    time.sleep(1)
    print("2: No, you rather stay away.")
    drink_choice = input("What do you want to do? (1 or 2)")
    while drink_choice not in ["1", "2"]:
        drink_choice = input("Invalid choice. Please only select between 1 and 2.")
    if drink_choice == "1":
        print("You fill up your water")
        time.sleep(1)
        print("After a little while your stomach starts to make weird noises")
        time.sleep(1)
        print("There was something in the water. You start to feel a little sick.")
        time.sleep(1)
    elif drink_choice == "2":
        print("You don't drink anything and continue on your way..")
    else: print("Please choose a number from 1 to 2.")
    print("After a little while the walking becomes harder and harder,...")
    time.sleep(1)
    print("... as the trail slowly vanishes and you have to climb make your way through mud.")
    time.sleep(1)
    print("You get tired and decide to take a rest. But its cold and you find some dry wood from a tree nearby")
    time.sleep(1)
    print("1: You decide to make a little fire to warm yourself up")
    time.sleep(1)
    print("2: You rather leave it.")
    fire_choice = input("What do you want to do? (1 or 2)")
    while fire_choice not in ["1", "2"]:
        fire_choice = input("Invalid choice. Please only select between 1 and 2.")
    if fire_choice == "1":
        print("The fire feels good. Your warming up quickly.")
        time.sleep(1)
        print("But as you sit there, you can here the wolves coming closer and closer.")
        time.sleep(1)
        print("They seem to have noticed the fire from afar. What do you want to do")
        time.sleep(1)
        print("1: You try to run away as fast as possible.")
        time.sleep(1)
        print("2: You hide in the nearby bushes.")
        wolves_choice = input("What do you want to do? (1 or 2)")
        while wolves_choice not in ["1", "2"]:
            wolves_choice = input("Invalid choice. Please only select between 1 and 2.")
        if wolves_choice == "1" and drink_choice == "1":
            print("You try to run away. But after a couple meters you lose your energy. You feel sick from the water")
            time.sleep(1)
            print("The wolves catch you. Game over..")
            quit()
        elif wolves_choice == "1" and drink_choice == "2":
            print("You try to run away and race up the water.")
            time.sleep(1)
            print("You don't look behind and just keep running. After a while you cant hear them anymore.")
            time.sleep(1)
            print("You got away...")
        elif wolves_choice == "2":
            print("You hide behind a large bush and watch as the wolves reach the fire.")
            time.sleep(1)
            print("The wolves try to smell you, but the smoke is limiting their senses.")
            time.sleep(1)
            print("You sneak away and continue your way up the river..")
        else: print("Please choose a number from 1 to 2.")
    elif fire_choice == "2" and drink_choice == "1":
        print("You decide to keep going and not to take a rest.")
        time.sleep(1)
        print("Your stomach keeps getting worse as you continue your way")
        time.sleep(1)
        print("Your legs get weaker as you start to stumble from exhaustion")
        time.sleep(1)
        print("You quickly lose your consciousness. ")
        time.sleep(1)
        print("You will not be reaching the house today. Game over..")
        quit()
    elif fire_choice == "2" and drink_choice == "2":
        print("You decide not to take a rest and continue")
        time.sleep(1)
        print("Your tired but you keep going.")
    else: print("Please choose a number from 1 to 2.")
else: print("Please choose a number from 1 to 2.")
time.sleep(1)
print("And then you can finally see it. A small house appears right on top of the hill.")
time.sleep(1)
print("You get excited and use your last bits of energy to climb the last couple of steps.")
time.sleep(1)
print("As you reach the top you see the last challenge..")
time.sleep(1)
print("The house is located on the other side of river.")
time.sleep(1)
print("You decide to place stones to step on them.")
while True:
    try:
        stones = int(input("How many stones do you want to use (Choose a number from 0 to 10"))
        if 0<= stones <= 10:
            break
        else:
            print("Please choose a number from 0 to 10.")
    except ValueError:
        print("This is not a number. Please choose a number from 0 to 10.")
if stones <=2:
    print("You did not use enough stones. As you try to make the last jump, you fall into the river.")
    time.sleep(1)
    print("Game over..")
    quit()
elif stones >=8:
    print("You placed too many stones and have blocked the river.")
    time.sleep(1)
    print("The water rises over the stones and flushes you in the water.")
    time.sleep(1)
    print("Game over..")
    quit()
else:
    print("It works! You jump over the stones and cross the river safely")
time.sleep(1)
print("You made it! You reach the house and finally can take a rest.")
time.sleep(1)
print("Now get some well deserved sleep, because the next night is already coming")
time.sleep(1)
print("Thanks for playing!")






