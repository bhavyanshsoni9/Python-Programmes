
class Unexpected_Input(Exception):
    pass

while True:
    a = input("Enter any value between 5 and 9: ")
    if('quit' in a):
        print("Correct!")

    elif(a == '999'):
        break

    elif(a<"5" or a>"9"):
        raise Unexpected_Input("Enter any value in between 5 and 9! Understood")

    else:
        print("Correct!")

