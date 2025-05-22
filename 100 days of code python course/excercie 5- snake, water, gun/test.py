
def test():
    global user_input
    try:
        user_input = int(input("Enter 0 for Snake, 1 for Water and 2 for Gun: "))



    except ValueError as v:
        print("None")
    print(user_input)
test()


