from time import sleep
import random

#TODO - Fix the "pulled a 8" when it's supposed to be "an 8" issue.
#TODO - Fix the recurring functions for the dealer's hidden card and the player's hit/stand phase.
#TODO - Add a way to keep track of wins/losses.
#TODO - Add a way to keep track of the player's money / create bet system.
#TODO - Mayhaps a GUI?

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

#Important parameters for the game
GameRunning = True
round_index = int(1)
Cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Ace (1 or 11), 2-10, Jack, Queen, King
Card_tens = ["10", "Jack", "Queen", "King"]
# Introduction to game
print(logo)
print("""Welcome to blackjack!
The goal of blackjack is simple.  All one needs to do to win is have a higher hand value than the dealer, without going over 21. 
Players are dealt two cards and can then choose to “hit” (receive additional cards) or “stand” (keep their current hand). 
The dealer also receives two cards, but only one is face up.
If a player’s hand exceeds 21, they “bust” and lose the game. If the dealer busts, all remaining players win. 
If neither the player nor the dealer busts, the player with the highest hand value wins.
""")
while GameRunning:
    print(f"Round {round_index} of blackjack")

    #Resetting variables for next round as well as setting them up for the first.
    Dealer_Hand = int(0)
    Dealer_Temp = int(0)
    Dealer_Ace = int(0)
    Player_Hand = int(0)
    Player_Temp = int(0)
    Player_Ace = int(0)
    Hit_Stand_Phase = True
    Second_Dealer_Card = True

    # Dealer gets his first 2 cards with 1 hidden card stored in Dealer_Temp
    Dealer_Temp = random.choice(Cards)
    if Dealer_Temp == 11: # Check to see if the card is an Ace.
        print("The dealer shows an Ace + a hidden card")
        Dealer_Ace += 1 # Add to ace counter to remove later if needed.
    elif Dealer_Temp == 10:
        print(f"The Dealer shows a {random.choice(Card_tens)} + a hidden card")
    else:
        print(f"The dealer shows a {Dealer_Temp} + a hidden card")
    Dealer_Hand += Dealer_Temp
    Dealer_Temp = random.choice(Cards) # Hidden card
    print("")
    sleep(1)

    # Give player's initial 2 cards.
    for i in range (0,2):
        Player_Temp = random.choice(Cards)
        if Player_Temp == 11:
            print("You pulled an Ace!")
            Player_Ace += 1
        elif Player_Temp == 10:
            print(f"You pulled a {random.choice(Card_tens)}!")
        else:
            print(f"You pulled a {Player_Temp}!")
        Player_Hand += int(Player_Temp)
        sleep(1)


    print("") # Gap between Dealer's cards and Player's Hit/Stand phase

    while Hit_Stand_Phase:
        if Player_Hand == 21:
            print(f"You got a blackjack! ({Player_Hand})")
            print("")
            sleep(1)
            Hit_Stand_Phase = False
        else:
            print(f"You have {Player_Hand}, type \"H\" to Hit or \"S\" to Stand, type \"Q\" if you no longer wish to play. ", end = "")
            Hit_or_Stand = input()
            if Hit_or_Stand.lower() == "h":
                Player_Temp = random.choice(Cards)
                if Player_Temp == 11:
                    print("You pulled an Ace!")
                    Player_Ace += 1
                elif Player_Temp == 10:
                    print(f"You pulled a {random.choice(Card_tens)}!")
                else:
                    print(f"You pulled a {Player_Temp}!")
                if Player_Hand + Player_Temp > 21 and Player_Ace > 0:
                    Player_Hand = Player_Hand - 10 + Player_Temp
                    Player_Ace -= 1
                elif Player_Hand + Player_Temp > 21 and Player_Temp == 11:
                    Player_Hand += 1
                    Player_Ace -= 1
                elif Player_Hand + Player_Temp == 21:
                    Player_Hand += Player_Temp
                    print(f"You got a blackjack! ({Player_Hand})")
                    print("") # Gap between player's stand and dealer's hit/stand phase
                    Hit_Stand_Phase = False
                elif Player_Hand + Player_Temp > 21:
                    Player_Hand += Player_Temp # Adding to check later if Player_Hand < 21 so we skip dealer Hit/Stand phase if not needed
                    print(f"You busted with {Player_Hand}! Dealer wins!")
                    Hit_Stand_Phase = False
                else:
                    Player_Hand += Player_Temp
            elif Hit_or_Stand.lower() == "s":
                print("") # Gap between player's stand and dealer's hit/stand phase
                Hit_Stand_Phase = False
            elif Hit_or_Stand.lower() == "q":
                print("Quitting game...")
                exit()
            else:
                print("Invalid input, try again!")

    Hit_Stand_Phase = True # Resetting hit stand phase for dealer's hit/stand phase or next turn.

    if Player_Hand <= 21 and Dealer_Hand < 17: # Basically if player is alive AND there's something to deal for dealer, otherwise no reason to go on
        while Hit_Stand_Phase:
            if Dealer_Hand < 17:
                if Second_Dealer_Card:
                    if Dealer_Temp == 11:
                        print(f"The dealer shows an Ace", end="")
                        Dealer_Ace += 1
                    elif Dealer_Temp == 10:
                        print(f"The dealer shows a {random.choice(Card_tens)}", end="")
                    else:
                        print(f"The dealer shows a {Dealer_Temp}", end="")
                    Second_Dealer_Card = False  # To prevent the dealer from showing the hidden card again
                else:
                    if Dealer_Temp == 11:
                        print(f"The dealer pulls an Ace", end = "")
                        Dealer_Ace += 1
                    elif Dealer_Temp == 10:
                        print(f"The dealer pulls a {random.choice(Card_tens)}", end = "")
                    else:
                        print(f"The dealer pulls a {Dealer_Temp}", end="")
                if Dealer_Hand + Dealer_Temp > 21 and Dealer_Ace > 0:
                    Dealer_Hand = Dealer_Hand - 10 + Dealer_Temp
                    Dealer_Ace -= 1
                elif Dealer_Hand + Dealer_Temp > 21 and Dealer_Temp == 11:
                    Dealer_Hand += 1
                    Dealer_Ace -= 1
                elif Dealer_Hand + Dealer_Temp == 21:
                    Dealer_Hand += Dealer_Temp
                elif Dealer_Hand + Dealer_Temp > 21:
                    print("\nThe dealer exceeded 21, You win, congratulations!")
                    Dealer_Hand += Dealer_Temp
                    Hit_Stand_Phase = False
                else:
                    Dealer_Hand += Dealer_Temp
                if Dealer_Hand < 22:
                    print(f", now has {Dealer_Hand}")
                Dealer_Temp = random.choice(Cards)
                sleep (1)
            else:
                if Dealer_Hand > Player_Hand:
                    if Dealer_Hand == 21:
                        print(f"The dealer wins with a blackjack ({Dealer_Hand})! You had {Player_Hand}")
                    else:
                        print(f"The dealer wins with a hand of {Dealer_Hand}, you had {Player_Hand}")
                elif Dealer_Hand < Player_Hand:
                    print(f"You win with a hand of {Player_Hand}, congratulations! The dealer had {Dealer_Hand}")
                else:
                    print(f"It's a tie! Both you and the dealer had a hand of {Dealer_Hand}!")
                Hit_Stand_Phase = False
    sleep(3.5)
    print("\n" * 20)
    round_index += 1 # To keep track of round















