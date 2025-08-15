count = 1

while count <= 5:
    print("Count is:", count)
    count += 1  # Increment to avoid infinite loop




secret_word = "shyam"
guess_word = ""
guess_count=0
guess_limit=3
out_of_guesses=False

while guess_word != secret_word and not(out_of_guesses):
    if guess_count < guess_limit :
        guess_word = input("enter your guess: ")
        guess_count+=1
    else:
        out_of_guesses=True

if out_of_guesses:
    print("out of guesses,you lose")
else:
    print("you win!")                