import random


class BlackJackGame:
    def __init__(self,mute):

        # Deck of cards
        self.mute = mute
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    # Create a deck
    def create_deck(self):
        deck = [(rank, suit) for suit in self.suits for rank in self.ranks]
        random.shuffle(deck)
        return deck

    # Calculate hand value, handle aces as 1 or 11
    def calculate_hand(self,hand):
        value = sum(self.values[card[0]] for card in hand)
        aces = sum(1 for card in hand if card[0] == 'A')
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    # Display cards
    def display_hand(self,hand, player):
        if not self.mute:
            print(f"{player} hand: ", end="")
            print(", ".join(f"{rank} of {suit}" for rank, suit in hand))
            print(f"{player} hand value: {self.calculate_hand(hand)}")

    # Play a round of blackjack
    def play_blackjack(self,player):
        deck = self.create_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        #TODO: PLACE AI BETS HERE
        bet = 0

        # Player turn
        while True:
            if not self.mute: self.display_hand(player_hand, "Player")
            if self.calculate_hand(player_hand) > 21:
                if not self.mute: print("Player busts! Dealer wins.")
                return -1
            
            ##action = input("Would you like to (h)it or (s)tand? ").lower()
            
            action = player.get_action(self.calculate_hand(player_hand),self.calculate_hand(dealer_hand),bet)
            if action == 1:
                player_hand.append(deck.pop())
            elif action == 0:
                break

        # Dealer turn
        while self.calculate_hand(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
        
        # Show hands
        self.display_hand(dealer_hand, "Dealer")
        player_value = self.calculate_hand(player_hand)
        dealer_value = self.calculate_hand(dealer_hand)

        # Determine outcome
        if dealer_value > 21:
            if not self.mute: print("Dealer busts! Player wins.")
            return 1
        elif player_value > dealer_value:
            if not self.mute: print("Player wins!")
            return 1
        elif player_value < dealer_value:
            if not self.mute: print("Dealer wins!")
            return -1
        else:
            if not self.mute: print("It's a tie!")
            return 0


