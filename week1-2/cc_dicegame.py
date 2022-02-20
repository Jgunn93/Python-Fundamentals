import random

high_score = 0

def dice_game():
    while True:
        global high_score
        print("Current High Score: ", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        user_input = input("Enter your choice: ")
        print("")

        if user_input == "1":
            dice_roll_one = random.randint(1, 6)
            print("You roll a...", dice_roll_one)
            dice_roll_two = random.randint(1, 6)
            print("You roll a...", dice_roll_two)
            print("")
            both_roll = dice_roll_one + dice_roll_two
            print("You have rolled a total of: ",
                dice_roll_one + dice_roll_two)

            if both_roll > high_score:
                print("")
                print("New high score!\n")
                high_score = both_roll
            else:
                print("")
            continue
        else:
            print("Goodbye!")
            break
dice_game()