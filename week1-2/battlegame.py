wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"
exit = "exit"

wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 300

wizaard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 299

dragon_hp = 300
dragon_damage = 50

while True:
    while True:
        print("1)    Wizard")
        print("2)    Elf")
        print("3)    Human")
        print("4)    Orc")
        print("5)    Exit")
        character = input("Choose your character: ").lower()
        if character in ("1", "wizard"):
            character = wizard
            my_hp = wizard_hp
            my_damage = wizaard_damage
            break
        elif character in ("2", "elf"):
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif character in ("3", "human"):
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif character in ("4", "orc"):
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        elif character == "5":
            print("Goodbye!")
            exit = True
            break
        else:
            print("Unknown character")
    if exit != True:
        print("You have chosen the character: " + character)
        print("Health: ", my_hp)
        print("Damage: ", my_damage)

    while True:
        if exit == True:
            break

        dragon_hp = dragon_hp - my_damage
        print("The", character, "damaged the Dragon!")
        print("The Dragon's hitpoints are now:", dragon_hp)

        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break
        my_hp = my_hp - dragon_damage
        print("The Dragon strikes back at the " + character)
        print("The", character, "'s hitpoints are now", my_hp,)
        if my_hp <= 0:
            print("The", character, "has lost the battle.")
            break

    restart = input("Would you like to play again? (Y/N)").lower()
    if restart in ("no", "n"):
        print("Thanks for playing!")
        break