import random

options = ["Rock", "Paper", "Scissor"]

while True:
    ucount = 0
    ccount = 0

    player = int(input('''
    Game Start....
    1. Yes
    2. No | Exit
    '''))

    if player == 1:
        for a in range(1, 6):
            player_choice = int(input('''
            1 Rock
            2 Scissor
            3 Paper
            '''))

            if player_choice == 1:
                playerch = "Rock"
            elif player_choice == 2:
                playerch = "Scissor"
            elif player_choice == 3:
                playerch = "Paper"
            else:
                print("Invalid choice!")
                continue

            computer = random.choice(options)

            print("Computer Value:", computer)
            print("Your Choice:", playerch)

            if computer == playerch:
                print("Game Draw!")
            elif (playerch == "Rock" and computer == "Scissor") or \
                 (playerch == "Paper" and computer == "Rock") or \
                 (playerch == "Scissor" and computer == "Paper"):
                print("Yay! You win!!")
                ucount += 1
            else:
                print("Oops! Computer wins!")
                ccount += 1

        print("\nFinal Score: You =", ucount, "| Computer =", ccount)
        if ucount > ccount:
            print("🎉 You are the overall winner!")
        elif ucount < ccount:
            print("💻 Computer is the overall winner!")
        else:
            print("🤝 It's a tie overall!")

    else:
        break
