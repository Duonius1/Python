from time import sleep
import random

#TODO - Add splits. This is a big one, but it's a big part of blackjack.
#TODO - Mayhaps a GUI? not a very graphic interface, but there technically is one?
#TODO - Add a way to change the amount of decks used in the game like most online casinos.
#TODO - Add a way to change the amount of players/bets in the game (After splits)
#TODO - Add side bets like insurance, 21+3, etc.

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
def number_validation(message):
    while True:
        userinput = input(message)
        try:
            float(userinput)
            return userinput
        except ValueError:
            print("Invalid input, try again!")
            continue

def card_pull_message(ace, person, pull_show, end): # Stage is show/pulled cards, person is for dealer/player
    temp = random.choice(Cards)
    if temp == 11:
        print(f"{person} {pull_show} an Ace{end}", end = "")
        ace += 1
    elif temp == 10:
        print(f"{person} {pull_show} a {random.choice(Card_tens)}{end}", end = "")
    else:
        if temp == 8:
            print(f"{person} {pull_show} an {temp}{end}", end = "")
        else:
            print(f"{person} {pull_show} a {temp}{end}", end = "")
    return temp, ace

def bust_check(hand, ace, temp, hit_stand_phase, person):
    if hand + temp > 21 and ace > 0:
        hand = hand - 10 + temp
        ace -= 1
    elif hand + temp > 21 and temp == 11:
        hand += 1
        ace -= 1
    elif hand + temp == 21:
        hand += temp
        person = "\nThe dealer" if person == "The dealer" else person # Needed for proper blackjack message because of the ", now has {hand}." message
        print(f"{person} got a blackjack! ({hand})\n")
        hit_stand_phase = False
    elif hand + temp > 21:
        hand += temp  # Adding to check later if Player_Hand < 21 so we skip dealer Hit/Stand phase if not needed
        person = " and" if person == "The dealer" else person
        print(f"{person} busted with {hand}!")
        hit_stand_phase = False
    else:
        hand += temp
    if person == "The dealer" and hand < 21:
        print(f", now has {hand}.")
    return hand, ace, hit_stand_phase

def menu(double_down, bet, timer):
    while True: # As long as you don't quit from menu
        menu_option = input("""
==== MENU ==== 
Resume play ("Play")
Options ("Options")
Check wallet balance ("Wallet")
Quit the game ("Quit")
>""").lower()
        if menu_option == "play":
            break
        elif menu_option == "quit":
            print("Thanks for playing!")
            print("Quitting game...")
            exit()
        elif menu_option == "wallet":
            print(f"Your current balance is ${Wallet}")
        elif menu_option == "options":
            double_down, bet, timer = options(double_down, bet, timer)
        else:
            print("Invalid input, try again!")
    return double_down, bet, timer

def options(double_down, bet, timer):
    while True: # As long as you don't quit from options
        option = input("""
==== OPTIONS ====
Turn on bets ("B On")
Turn off bets ("B Off")
Turn on double downs ("D On")
Turn off double downs ("D Off")
Change wait time between rounds ("Time")
Return to menu ("Menu")
>""").lower()
        if option == "b on":
            bet = True
            print("Bets are now on.")
        elif option == "b off":
            bet = False
            print("Bets are now off.")
        elif option == "d on":
            double_down = True
            print("Double downs are now on.")
        elif option == "d off":
            double_down = False
            print("Double downs are now off.")
        elif option == "time":
             timer = float(input("How many seconds would you like to wait between rounds? "))
             print(f"Wait time between rounds is now {timer} seconds.")
        elif option == "menu":
            break
        else:
            print("Invalid input, try again!")
    return double_down, bet, timer

#Important parameters for the game
Sleep_Timer = float(3.5)
GameRunning = True
Bets_On = True
Double_Down_On = True
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
Wallet = float(number_validation("What is your budget for playing blackjack? $"))
if Wallet == 0:
    Bets_On = False # Determines whether bets are on or off
    Double_Down_On = False # Determines whether double downs are on or off

while GameRunning:
    # Resetting variables for next round as well as setting them up for the first.
    Dealer_Hand = Dealer_Temp = Dealer_Ace = int(0)
    Player_Hand = Player_Temp = Player_Ace = int(0)
    Hit_Stand_Phase = Second_Dealer_Card = True
    Valid_Bet = False
    Bet = int(0)
    Double_Down = True if Double_Down_On else False

    print(f"\nWins/Losses/Ties: {wins}/{losses}/{ties}")
    print(f"Round {round_index} of blackjack")
    if Bets_On:
        Bet = float(number_validation("How much would you like to bet? $"))
        while Bet > Wallet:
            print("You can't bet more than you have!")
            Bet = float(number_validation("How much would you like to bet? $"))
    Double_Down = False if Bet == 0 else True # If no bet, pointless to double down

    print("")

    # Dealer gets his first 2 cards with 1 hidden card stored in Dealer_Temp
    Dealer_Temp, Dealer_Ace = card_pull_message(Dealer_Ace, "The dealer", "shows", " + a hidden card.\n")
    Dealer_Hand += Dealer_Temp
    print("")
    sleep(1)

    # Give player's initial 2 cards.
    for i in range (0,2):
        Player_Temp, Player_Ace = card_pull_message(Player_Ace, "You", "pulled", "!\n")
        Player_Hand += int(Player_Temp)
        sleep(1)

    print("") # Gap between Dealer's cards and Player's Hit/Stand phase

    while Hit_Stand_Phase:
        if Player_Hand == 21:
            print(f"You got a blackjack! ({Player_Hand})\n")
            break
        if Double_Down:
            print(f"You have {Player_Hand}, type \"H\" to Hit, \"S\" to Stand, \"D\" to double down. Type \"M\" for menu. >", end = "")
        else:
            print(f"You have {Player_Hand}, type \"H\" to Hit, \"S\" to Stand. Type \"M\" for menu. >", end = "")
        Hit_or_Stand = input()
        if Hit_or_Stand.lower() == "h":
            Player_Temp, Player_Ace = card_pull_message(Player_Ace,"You", "pulled", "!\n")
            Player_Hand, Player_Ace, Hit_Stand_Phase = bust_check(Player_Hand, Player_Ace, Player_Temp, Hit_Stand_Phase, "You")
            Double_Down = False
        elif Hit_or_Stand.lower() == "s":
            print("") # Gap between player's stand and dealer's hit/stand phase
            Hit_Stand_Phase = False
        elif Hit_or_Stand.lower() == "m":
            Double_Down_On, Bets_On, Sleep_Timer = menu(Double_Down_On, Bets_On, Sleep_Timer)
            Double_Down = True if Double_Down_On else False # To change the printed text
        elif Hit_or_Stand.lower() == "d" and Double_Down:
            if Bets_On:
                Bet *= 2
                print(f"You have doubled down to ${Bet}!")
                Double_Down = False
        else:
            print("Invalid input, try again!")
        if Player_Hand > 21:
            print("The dealer wins!")
            losses += 1
            Wallet -= Bet

    Hit_Stand_Phase = True # Resetting hit stand phase for dealer's hit/stand phase or next turn.

    if Player_Hand <= 21 and Dealer_Hand < 17: # Basically if player is alive AND there's something to deal for dealer, otherwise no reason to go on
        while Hit_Stand_Phase:
            if Dealer_Hand < 17:
                stage = "shows" if Second_Dealer_Card else "pulled"
                Dealer_Temp, Dealer_Ace = card_pull_message(Dealer_Ace, "The dealer", stage, "")
                Second_Dealer_Card = False  # To prevent the dealer from "showing" the hidden card again
                Dealer_Hand, Dealer_Ace, Hit_Stand_Phase = bust_check(Dealer_Hand, Dealer_Ace, Dealer_Temp, Hit_Stand_Phase, "The dealer")
                sleep (1)
            else:
                break
        if Dealer_Hand < 22:
            if Dealer_Hand > Player_Hand:
                if Dealer_Hand == 21:
                    print(f"The dealer wins with a blackjack ({Dealer_Hand})! You had {Player_Hand}!")
                else:
                    print(f"The dealer wins with a hand of {Dealer_Hand}, you had {Player_Hand}!")
                losses += 1
                Wallet -= Bet
            elif Dealer_Hand < Player_Hand:
                if Player_Hand == 21:
                    print(f"You win with a blackjack! The dealer had {Dealer_Hand}!")
                else:
                    print(f"You win with a hand of {Player_Hand}, congratulations! The dealer had {Dealer_Hand}!")
                wins += 1
                Wallet += Bet
            else:
                print(f"It's a tie! Both you and the dealer had a hand of {Dealer_Hand}!")
                ties += 1
            Hit_Stand_Phase = False
        else:
            print("You win!")
            wins += 1
            Wallet += Bet
    sleep(Sleep_Timer)
    print("\n" * 20)
    round_index += 1 # To keep track of round















