from time import sleep
import random

#TODO - Add splits. (put splits as like a +=1, then for i in range (0, splits) do all of them and
# all standing ones are added into a list, then print final results with the same range using i as the hand number)
#TODO - Add side bets like insurance, 21+3, etc.
#TODO - Mayhaps a GUI? not a very graphic interface, but there technically is one?
#TODO - Add a way to change the amount of decks used in the game like most online casinos. Honestly probably pointless to do?
#TODO - Add a way to change the amount of players/bets in the game (After splits). This only depends on whether I decide to launch this game somewhere.

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
        temp_face = random.choice(Card_tens)
        print(f"{person} {pull_show} a {temp_face}{end}", end = "")
        return temp_face, temp, ace
    else:
        if temp == 8:
            print(f"{person} {pull_show} an {temp}{end}", end = "")
        else:
            print(f"{person} {pull_show} a {temp}{end}", end = "")
    return "noface", temp, ace

def bust_check(hand, ace, temp, hit_stand_phase, person):
    if hand + temp > 21 and ace > 0:
        hand = hand - 10 + temp
        ace -= 1
    elif hand + temp > 21 and temp == 11:
        hand += 1
        ace -= 1
        if hand == 21: # In the off chance you get a blackjack with an ace hitting at 20
            person = "\nThe dealer" if person == "The dealer" else person
            print(f"{person} got a blackjack! ({hand})")
            hit_stand_phase = False
    elif hand + temp == 21:
        hand += temp
        person = "\nThe dealer" if person == "The dealer" else person
        print(f"{person} got a blackjack! ({hand})")
        hit_stand_phase = False
    elif hand + temp > 21:
        hand += temp  # Adding to check later if Player_Hand < 21 so we skip dealer Hit/Stand phase if not needed
        person = "\nThe dealer" if person == "The dealer" else person
        print(f"{person} busted with {hand}!")
        hit_stand_phase = False
    else:
        hand += temp
    if person == "The dealer" and hand != 21:
        print(f", now has {hand}.")
    return hand, ace, hit_stand_phase

def menu(splits, double_down, bet, timer):
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
            splits, double_down, bet, timer = options(splits, double_down, bet, timer)
        else:
            print("Invalid input, try again!")
    return splits, double_down, bet, timer

def options(splits, double_down, bet, timer):
    while True: # As long as you don't quit from options
        option = input("""
==== OPTIONS ====
Turn on bets ("B On")
Turn off bets ("B Off")
Turn on double downs ("D On")
Turn off double downs ("D Off")
Turn on splits ("S On")
Turn off splits ("S Off")
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
        elif option == "s on":
            splits = True
            print("Splits are now on.")
        elif option == "s off":
            splits = False
            print("Splits are now off")
        elif option == "time":
             timer = float(input("How many seconds would you like to wait between rounds? "))
             print(f"Wait time between rounds is now {timer} seconds.")
        elif option == "menu":
            break
        else:
            print("Invalid input, try again!")
    return splits, double_down, bet, timer

#Important parameters for the game
Sleep_Timer = float(3.5)
GameRunning = True
Bets_On = True
Double_Down_On = True
Splits_On = True
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
while Wallet < 0:
    print("You can't have a negative budget!")
    Wallet = float(number_validation("What is your budget for playing blackjack? $"))
if Wallet == 0:
    Bets_On = False # Determines whether bets are on or off
    Double_Down_On = False # Determines whether double downs are on or off
Original_Wallet = Wallet

while GameRunning:
    # Resetting variables for next round as well as setting them up for the first.
    Dealer_Hand = Dealer_Temp = Dealer_Ace = int(0)
    Player_Hand = Player_Temp = Player_Ace = int(0)
    Bet = Split_Card = iteration = Split_Ace = int(0)
    split_number = int(0)
    Temp_Wallet = float(Wallet)
    Results = []
    Bets = []
    Hit_Stand_Phase = Second_Dealer_Card = True
    Valid_Bet = Split_Check = False
    Double_Down = True if Double_Down_On else False
    turn_one_option_text = text_if_bet = Card_Face = Previous_Face = Hit_or_Stand = ""
    print(f"\nWins/Losses/Ties: {wins}/{losses}/{ties}")
    if Bets_On:
        print(f"Current balance: ${Wallet}")
        minus_plus_sign = "-" if Wallet < Original_Wallet else "+"
        print(f"Current winnings: {minus_plus_sign}${Wallet - Original_Wallet}")
    print(f"Round {round_index} of blackjack")
    if Bets_On:

        Bet = float(number_validation("How much would you like to bet? $"))
        while Bet > Wallet or Bet < 0:
            if Bet > Wallet:
                print("You can't bet more than you have!")
                Bet = float(number_validation("How much would you like to bet? $"))
            else:
                print("You can't bet a negative amount!")
                Bet = float(number_validation("How much would you like to bet? $"))
    Bets.append(Bet)
    Wallet -= Bet
    Double_Down = False if Bet == 0 else True # If no bet, pointless to double down

    print("")

    # Dealer gets his first 2 cards with 1 hidden card stored in Dealer_Temp
    Card_Face, Dealer_Temp, Dealer_Ace = card_pull_message(Dealer_Ace, "The dealer", "shows", " + a hidden card.\n") # Card_Face does nothing for the dealer
    Dealer_Hand += Dealer_Temp
    print("")
    sleep(1)

    # Give player's initial 2 cards.
    for i in range (0,2):
        Card_Face, Player_Temp, Player_Ace = card_pull_message(Player_Ace, "You", "pulled", "!\n")
        Player_Hand, Player_Ace, Hit_Stand_Phase = bust_check(Player_Hand, Player_Ace, Player_Temp, Hit_Stand_Phase, "You")
        sleep(1)
        if Splits_On:
            Split_Check = True if Previous_Face == Card_Face and Player_Temp * 2 == Player_Hand else False # Check if eligible for split
            Split_Check = True if Previous_Face == Card_Face and Player_Temp == 11 and Player_Hand == 12 else Split_Check # Separate check for 2 aces
        Previous_Face = Card_Face

    print("") # Gap between Dealer's cards and Player's Hit/Stand phase

    while iteration <= split_number: # Nested loops exist solely for ability to handle infinite number of splits
        while Hit_Stand_Phase:
            if Split_Check and Double_Down and Bets_On and Wallet >= Bet:
                turn_one_option_text = ", \"/S\" to Split or \"D\" to Double Down"
            elif Split_Check:
                turn_one_option_text = ", \"/S\" to  Split"
            elif Double_Down and Bets_On and Wallet >= Bet:
                turn_one_option_text = ", \"D\" to Double Down"
            print(f"You have {Player_Hand}, type \"H\" to Hit, \"S\" to Stand{turn_one_option_text}. Type \"M\" for menu. >", end = "")
            Hit_or_Stand = input()
            if Hit_or_Stand.lower() == "h":
                Double_Down = False
                Card_Face, Player_Temp, Player_Ace = card_pull_message(Player_Ace,"You", "pulled", "!\n")
                Player_Hand, Player_Ace, Hit_Stand_Phase = bust_check(Player_Hand, Player_Ace, Player_Temp, Hit_Stand_Phase, "You")
            elif Hit_or_Stand.lower() == "s":
                print("") # Gap between player's stand and dealer's hit/stand phase
                Hit_Stand_Phase = False
            elif Hit_or_Stand.lower() == "/s" and Split_Check:
                split_number += 1
                if Player_Temp != 11:
                    Player_Hand -= Player_Temp # Removing the second card
                else:
                    Player_Hand -= 1 # Removing the second ace
                    Split_Ace = 1
                Split_Card = Player_Temp # Storing the second card for the split
                Bets.append(Bet) # Adding the same bet to the split hand
                Wallet -= Bet
                Card_Face, Player_Temp, Player_Ace = card_pull_message(Player_Ace, "You", "pulled", "!\n")
                Player_Hand, Player_Ace, Hit_Stand_Phase = bust_check(Player_Hand, Player_Ace, Player_Temp, Hit_Stand_Phase, "You")
                Double_Down = True if Double_Down_On and Bet != 0 else False
                if Splits_On:
                    Split_Check = True if Previous_Face == Card_Face and (Split_Card * 2 == Player_Hand or (Split_Card == 11 and Player_Hand == 12))else False  # Check if eligible for split
                else:
                    Split_Check = False
            elif Hit_or_Stand.lower() == "m":
                Splits_On, Double_Down_On, Bets_On, Sleep_Timer = menu(Splits_On, Double_Down_On, Bets_On, Sleep_Timer)
                Double_Down = True if Double_Down_On else False # To change the printed text
            elif Hit_or_Stand.lower() == "d" and Double_Down:
                Bets[-(iteration+1)] += Bet # Goes backwards through the list to add the bet to the correct hand
                print(f"You have doubled down to ${Bet * 2}!")
                Wallet -= Bet
                Double_Down = False
                Split_Check = False
            else:
                print("Invalid input, try again!")
            turn_one_option_text = ""
        iteration += 1
        Results.append(Player_Hand)
        if split_number > 0:
            if Hit_or_Stand.lower() == "h" and Player_Hand <= 21 and iteration >= split_number:
                Card_Face, Player_Temp, Player_Ace = card_pull_message(Player_Ace, "You", "pulled", "!\n")
                Split_Card, Player_Ace, Hit_Stand_Phase = bust_check(Split_Card, Player_Ace, Player_Temp, Hit_Stand_Phase, "You")
            Player_Hand = Split_Card
            Player_Temp = int(0)
            if Split_Card == 11:
                Player_Ace = Split_Ace
            Hit_Stand_Phase = True
            Split_Check = False
            Double_Down = True if Double_Down_On and Bet != 0 else False
            if Hit_or_Stand.lower() == "s" and iteration <= split_number:
                Card_Face, Player_Temp, Player_Ace = card_pull_message(Player_Ace, "You", "pulled", "!\n")
                Player_Hand, Player_Ace, Hit_Stand_Phase = bust_check(Player_Hand, Player_Ace, Player_Temp, Hit_Stand_Phase, "You")

    Hit_Stand_Phase = True # Resetting hit stand phase for dealer's hit/stand phase or next turn.
    index = int(0)
    if any(hand <= 21 for hand in Results): # Basically if player is alive, dealer plays
        while Hit_Stand_Phase:
            if Dealer_Hand < 17:
                stage = "shows" if Second_Dealer_Card else "pulled"
                Card_Face, Dealer_Temp, Dealer_Ace = card_pull_message(Dealer_Ace, "The dealer", stage, "") # Card_Face does nothing for the dealer
                Second_Dealer_Card = False  # To prevent the dealer from "showing" the hidden card again
                Dealer_Hand, Dealer_Ace, Hit_Stand_Phase = bust_check(Dealer_Hand, Dealer_Ace, Dealer_Temp, Hit_Stand_Phase, "The dealer")
                sleep (1)
            else:
                break
        for hand in Results:
            sleep(0.5)
            if hand > 21: # You busted but dealer didn't (if I busted I lose anyway so I don't think this check is necessary
                losses += 1
                text_if_bet = f". You lost ${Bets[-(index+1)]}" if Bets_On else text_if_bet
                print(f"You busted with {hand} and you lost hand #{index + 1}{text_if_bet}!")
            elif Dealer_Hand > 21: # Dealer busted but you didn't
                wins += 1
                Wallet += (Bets[-(index+1)] * 2)
                text_if_bet = f". You won ${Bets[-(index+1)]}" if Bets_On else text_if_bet
                print(f"The dealer busted with {Dealer_Hand} and you won hand #{index+1}{text_if_bet}!")
            elif Dealer_Hand > hand: # Dealer has higher hand and wins
                losses += 1
                text_if_bet = f". You lost ${Bets[-(index+1)]}" if Bets_On else text_if_bet
                if Dealer_Hand != 21:
                    print(f"The dealer won with {Dealer_Hand}, you had {hand} and lost hand #{index+1}{text_if_bet}!")
                else:
                    print(f"The dealer won with a blackjack ({Dealer_Hand}), you had {hand} and lost hand #{index+1}{text_if_bet}!")
            elif hand > Dealer_Hand: # You have higher hand and win
                wins += 1
                Wallet += (Bets[-(index+1)] * 2)
                text_if_bet = f". You won ${Bets[-(index+1)]}" if Bets_On else text_if_bet
                if hand != 21:
                    print(f"You won with {hand}, the dealer had {Dealer_Hand} and lost hand #{index+1}{text_if_bet}!")
                else:
                    print(f"You won with a blackjack, the dealer had {Dealer_Hand} and lost hand #{index+1}{text_if_bet}!")
            else: # Tie
                ties += 1
                text_if_bet = f", keeping ${Bets[-(index+1)]}" if Bets_On else text_if_bet
                Wallet += Bets[-(index+1)]
                print(f"It's a tie! Both you and the dealer had a hand of {hand} in hand #{index+1}{text_if_bet}!")
            index += 1
    else:
        for hand in Results:
            losses += 1
            index += 1
        text_if_bet = f". You lost {Temp_Wallet - Wallet}" if Bets_On else text_if_bet
        print(f"You busted on all hands and lost, the dealer wins{text_if_bet}!")
    sleep(Sleep_Timer)
    print("\n" * 25)
    round_index += 1 # To keep track of round















