This project is a terminal-based implementation of the popular card game Blackjack, designed for single-player play against a dealer. 
The game includes features commonly found in real-world Blackjack, such as betting, double-downs, splits, and insurance options, all delivered through a text-based user interface (TUI). 
It is beginner-friendly yet offers options to customize gameplay for advanced users.

Features:

	Core Blackjack Mechanics: Players can hit, stand, and aim to get closer to 21 than the dealer without busting.
	Betting System: Add stakes to your game with adjustable bets.
	Advanced Rules: Includes insurance, splits, and double-downs to enhance gameplay strategy.
	Customization Options:
		Toggle features like splits, side bets, and double-downs.
		Adjust delay times between game rounds.
	Statistics Tracking: Tracks wins, losses, and ties during the session.
	Interactive Menu: Accessible during gameplay for pausing or modifying settings.

How to run:

	Ensure Python 3.9 or higher is installed on your system.
	Run the script using the following command:
		python blackjack.py
	Follow the on-screen instructions to set your initial wallet and begin the game.

Gameplay Instructions:

	Objective: Get a hand total closer to 21 than the dealer’s without exceeding 21.
	Starting the Game:
		Input your wallet budget.
		Place your bets.
	Player Actions:
		Hit: Draw another card.
		Stand: Hold your current hand.
		Double Down: Double your bet and draw one more card.
		Split: Split matching cards into separate hands.
	Winning Conditions:
		Beat the dealer’s hand without busting.
		Dealer busts (exceeds 21).
		Achieve a Blackjack (21 with your first two cards).

Dependencies:

	No external libraries are required. 
	The game uses Python's built-in "random" and "time" modules.

What I Learned:

	Game Logic Design: Gained experience in implementing complex game rules, including handling edge cases like Blackjack on a double-down or split.
	State Management: Mastered techniques to track and update game states dynamically (e.g., player hands, wallet balance, and settings).
	User Input Validation: Enhanced understanding of robust input validation to ensure smooth and error-free gameplay.
	Modular Code Writing: Focused on creating reusable and maintainable functions to improve scalability and future enhancements.
	Optimization: Gained a lot of experience in on-the-spot optimization to shorten or clarify the code.