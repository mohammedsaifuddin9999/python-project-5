name =  input("Type your name: ")
print("Welcome", name, "to this adventure...")

answer = input("You are on a dirt road, it has come to an end and you can go left or right, which way would you like to go ? ").lower()


if answer == "left":
    answer = input("You came to a river, you can walk around it or swim across? Type walk to walk to walk around or swim to swim across: ")
    
    if answer == "swim":
        print("You are eaten by an alligator, You lose...")

    elif answer == "walk":
        print("You have walked many miles and got lost, sorry you are out of the game ")

    else:
        print("Not a valid option . You lose.")

elif answer == "right":
    answer = input("You came to a bridge and it looks scary would you like to cross it  or head back (cross/back)? ")

    if answer == "cross":
    
        answer = input("You meet a stranger on other side of a bridge, would you like to talk or not? (yes/no)")

        if answer == "yes":
            print("You talk to a stranger and he is happy from you and he gives you the gold. -You win-")

        elif answer == "no":
            print("You ignored the stranger and got lost in the forest. ")

    else:
        print("Not a valid option . You lose.")
        
elif answer == "back":
    print("You lose")

else:
    print("Not a valid option . You lose.")


print("THANK YOU FOR PLAYING", name.upper())