from time import sleep
import random

#TODO - Add a way to keep track of the player's money / create bet system.
#TODO - Add splits and double downs.
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

def Card_Pull_Message(ace, person, stage, end): # Stage is show/pulled cards, person is for dealer/player
    temp = random.choice(Cards)
    if temp == 11:
        print(f"{person} {stage} an Ace{end}", end = "")
        ace += 1
    elif temp == 10:
        print(f"{person} {stage} a {random.choice(Card_tens)}{end}", end = "")
    else:
        if temp == 8:
            print(f"{person} {stage} an {temp}{end}", end = "")
        else:
            print(f"{person} {stage} a {temp}{end}", end = "")
    return temp, ace

def Bust_Check(wallet, bet, hand, ace, temp, hit_stand_phase, person, person2, end):
        if hand + temp > 21 and ace > 0:
            hand = hand - 10 + temp
            ace -= 1
        elif hand + temp > 21 and temp == 11:
            hand += 1
            ace -= 1
        elif hand + temp == 21:
            hand += temp
            print(f"{person} got a blackjack! ({hand})")
            print("")  # Gap between next hit/stand phase
            hit_stand_phase = False
        elif hand + temp > 21:
            hand += temp  # Adding to check later if Player_Hand < 21 so we skip dealer Hit/Stand phase if not needed
            if end == "win!":
                person = " and"
                global wins
                wins += 1
                wallet += bet
            else:
                global losses
                losses += 1
                wallet -= bet
            print(f"{person} busted with {hand}! {person2} {end}", end = "")
            hit_stand_phase = False
        else:
            hand += temp
        if end == "win!" and hand < 22:
            print(f", now has {hand}.")
        return wallet, hand, ace, hit_stand_phase

#Important parameters for the game
GameRunning = True
Valid_Bet = False
round_index = int(1)
Cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Ace (1 or 11), 2-10, Jack, Queen, King
Card_tens = ["10", "Jack", "Queen", "King"]
wins = losses = ties = int(0)

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
    # Resetting variables for next round as well as setting them up for the first.
    Dealer_Hand = Dealer_Temp = Dealer_Ace = int(0)
    Player_Hand = Player_Temp = Player_Ace = int(0)
    Hit_Stand_Phase = Second_Dealer_Card = True
    Valid_Bet = False

    Wallet = int(input("What is your budget for playing blackjack? "))
    print(f"\nWins/Losses/Ties: {wins}/{losses}/{ties}")
    print(f"Round {round_index} of blackjack")
    Bet = int(input("How much would you like to bet? "))
    while not Valid_Bet:
        if Bet <= Wallet:
            Valid_Bet = True
        else:
            Bet = int(input("You don't have enough money to bet that much! Try again: "))

    # Dealer gets his first 2 cards with 1 hidden card stored in Dealer_Temp
    Dealer_Temp, Dealer_Ace = Card_Pull_Message(Dealer_Ace, "The dealer", "shows", " + a hidden card.\n")
    Dealer_Hand += Dealer_Temp
    print("")
    sleep(1)

    # Give player's initial 2 cards.
    for i in range (0,2):
        Player_Temp, Player_Ace = Card_Pull_Message(Player_Ace, "You", "pulled", "!\n")
        Player_Hand += int(Player_Temp)
        sleep(1)


    print("") # Gap between Dealer's cards and Player's Hit/Stand phase

    while Hit_Stand_Phase:
        if Player_Hand == 21:
            print(f"You got a blackjack! ({Player_Hand})\n")
            sleep(1)
            Hit_Stand_Phase = False
        else:
            print(f"You have {Player_Hand}, type \"H\" to Hit or \"S\" to Stand, type \"Q\" if you no longer wish to play. ", end = "")
            Hit_or_Stand = input()
            if Hit_or_Stand.lower() == "h":
                Player_Temp, Player_Ace = Card_Pull_Message(Player_Ace,"You", "pulled", "!\n")
                Wallet, Player_Hand, Player_Ace, Hit_Stand_Phase = Bust_Check(Wallet, Bet, Player_Hand, Player_Ace, Player_Temp, Hit_Stand_Phase, "You", "The dealer", "wins!")
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
                stage = "shows" if Second_Dealer_Card else "pulled"
                Dealer_Temp, Dealer_Ace = Card_Pull_Message(Dealer_Ace, "The dealer", stage, "")
                Second_Dealer_Card = False  # To prevent the dealer from "showing" the hidden card again
                Wallet, Dealer_Hand, Dealer_Ace, Hit_Stand_Phase = Bust_Check(Wallet, Bet, Dealer_Hand, Dealer_Ace, Dealer_Temp, Hit_Stand_Phase, "The dealer", "You", "win!")
                sleep (1)
            else:
                if Dealer_Hand > Player_Hand:
                    if Dealer_Hand == 21:
                        print(f"The dealer wins with a blackjack ({Dealer_Hand})! You had {Player_Hand}!")
                    else:
                        print(f"The dealer wins with a hand of {Dealer_Hand}, you had {Player_Hand}!")
                    losses += 1
                    Wallet -= Bet
                elif Dealer_Hand < Player_Hand:
                    print(f"You win with a hand of {Player_Hand}, congratulations! The dealer had {Dealer_Hand}!")
                    wins += 1
                    Wallet += Bet
                else:
                    print(f"It's a tie! Both you and the dealer had a hand of {Dealer_Hand}!")
                    ties += 1
                Hit_Stand_Phase = False
    sleep(3.5)
    print("\n" * 20)
    round_index += 1 # To keep track of round















