# Author: Bradley Sundberg
# Purpose: The Tech Academy - Python Project

def start(nice=0, mean=0, name=""):
    # Get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)


def describe_game(name):
    """
    Check if this is a new game or not.
    If it is new, get the user's name.
    If it is not a new game, thank the player for
    playing again and continue with the game.
    """
    if name != "":
        print("\nThank you for playing again, {}.".format(name))
    else:
        stop = True
        while stop:
            name = input("\nWhat is your name? \n>>> ").capitalize()
            if name != "":
                print("\nWelcome, {}!".format(name))
                print("\nIn this game, you will be greeted "
                      "\nby several different people. "
                      "\nYou can choose to be nice or mean.")
                print("But at the end of the game, your fate "
                      "\nwill be sealed by your actions.")
                stop = False
    return name


def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a "
                     "\nconversation. Will you be nice "
                     "\nor mean? (N/M) \n>>> ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice += 1
            stop = False
        elif pick == "m":
            print("\nThe stranger glares at you menacingly and storms off...")
            mean += 1
            stop = False
        else:
            print("\nPlease enter 'N' for Nice or 'M' for Mean.")
    score(nice, mean, name)


def show_score(nice, mean, name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))


def score(nice, mean, name):
    if nice > 2:
        win(nice, mean, name)
    elif mean > 2:
        lose(nice, mean, name)
    else:
        nice_mean(nice, mean, name)


def win(nice, mean, name):
    print("\nNice job, {}! You win! "
          "\nEveryone loves you and you've made lots of friends along the way!".format(name))
    again(nice, mean, name)


def lose(nice, mean, name):
    print("\nAhhh too bad, game over! "
          "\n{}, you live in a dirty beat-up van by the river, wretched and alone!".format(name))
    again(nice, mean, name)


def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        elif choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for 'YES', (N) for 'NO':")


def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice, mean, name)


if __name__ == "__main__":
    start()
