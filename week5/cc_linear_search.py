def linear_search_dictionary(my_dictionary, target):
    for x in my_dictionary:
        if my_dictionary[x] == target:
            print("Found at", x)
            return x
    print("Target not found in the dictionary")
    return -1

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)