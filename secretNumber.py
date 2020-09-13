secret = 5

guess = int(input("Time to play a game! It's called - What's the secret Number? "
                  "It is a number between 1 and 10, just guess: "))

if guess == secret:
    print("Wow, you got it dude - the number is 5!")

else:
    print("Sorry bro, that's not correct.")
