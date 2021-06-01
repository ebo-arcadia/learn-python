secret_num = 10
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    user_guess = int(input("Guess a number: "))
    guess_count += 1
    if user_guess == secret_num:
        print("You win!")
        break
else:
    print("You failed!")