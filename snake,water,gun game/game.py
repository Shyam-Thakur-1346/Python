computer = -1   # computer chooses gun

choice = input("Enter your choice (snake / water / gun): ").lower()

youdict = {
    "snake": 1,
    "water": 0,
    "gun": -1
}

reverse_dict = {
    1: "snake",
    0: "water",
    -1: "gun"
}

you = youdict[choice]

print(f"You chose {reverse_dict[you]}")
print(f"Computer chose {reverse_dict[computer]}")

if computer == you:
    print("It's a draw")
else:
    if computer == -1 and you == 1:
        print("Computer wins")
    elif computer == -1 and you == 0:
        print("You win")
    elif computer == 1 and you == -1:
        print("You win")
    elif computer == 1 and you == 0:
        print("Computer wins")
    elif computer == 0 and you == 1:
        print("You win")
    elif computer == 0 and you == -1:
        print("Computer wins")
    else:
        print("Something went wrong")
