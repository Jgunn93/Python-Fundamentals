import random

#workshop 5 with bubblesort and quicksort etc

def guess_random_number(tries, start, stop):  #task 1 guess number through user input
    num = random.randint(start,stop)
    # print(num)
    while tries != 0:
        print(tries,"Tries remaining")
        guess = int(input("Please guess what number we are thinking of: "))
        if num == guess:
            print("You guessed it!")
            return guess
        elif guess < num:
            print("Guess higher!")
        elif guess > num:
            print("Guess Lower!")
        tries -= 1
    print("You ran out of tries!")
    return
# guess_random_number(5,0,10)

#task 2, linear search
# print(help(range))


def guess_random_num_linear(tries,start,stop):
    target_num = random.randint(start,stop)
    print("the number to guess is:",target_num)
    for num in range(start,stop +1):
        tries -= 1
        # print(tries +1)                   #test to make sure tries is being done properly
        print("You have",tries +1,"remaining guesses.")
        print("The current guess is:",num)
        if num == target_num:
            print("That is the correct number")
            return
        elif num > target_num or num < target_num:
            print('That guess is incorrect')
        if tries == 0:
            print("You have run out of guesses")
            return

# guess_random_num_linear(5,0,10)

#task 3 binary search

def guess_random_num_binary(tries,start,stop):
    target_num = random.randint(start,stop)
    print("Random number to find:", target_num)
    lower_bound = start
    upper_bound = stop
    while lower_bound <= upper_bound:
        tries -= 1
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = pivot

        if pivot_value == target_num:
            print("Found it!",target_num)
            return pivot
        elif pivot_value > target_num:
            print("Guessing lower!")
            upper_bound = pivot - 1
        elif pivot_value < target_num:
            print("Guessing higher!")
            lower_bound = pivot + 1
        if tries == 0:
            print("Your program failed to find the number.")
            return

guess_random_num_binary(5,0,100)
