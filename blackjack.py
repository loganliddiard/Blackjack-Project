import random
import gymnasium as gym
from gymnasium import spaces
import numpy as np


class BlackJackGame(gym.Env):
    def __init__(self, mute, num_decks=1):

        # Deck of cards
        self.num_decks = num_decks
        self.mute = mute
        self.verbose = not mute
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        self.action_space = spaces.Discrete(2)  # 0: Stand, 1: Hit
        # TODO: add deck seen cards for card counting
        # my hand: card ranks and their count
        # dealer hand: card ranks and their count
        self.observation_space = spaces.MultiDiscrete(np.full(2 * len(self.ranks), len(self.suits) * num_decks + 1))
        self.reset()

    def reset(self, **kargs):
        self.deck = self.create_deck()
        self.player_hand = [self.deck.pop(), self.deck.pop()]
        self.dealer_hand = [self.deck.pop()]
        self.last_action = "s"
        return self._get_obs(), {}

    def _get_obs(self):
        obs = self._hand_to_count(self.player_hand)
        obs.extend(self._hand_to_count(self.dealer_hand))
        return np.array(obs, dtype=int)

    def _hand_to_count(self, hand):
        _hand = {rank: 0 for rank in self.ranks}
        for rank, suit in hand:
            _hand[rank] += 1
        return [v for v in _hand.values()]

    def _deck_pop(self):
        if len(self.deck) == 0:  # reshuffle when there are no cards left in deck
            self.create_deck()
        return self.deck.pop()

    def step(self, action):
        reward, done = 0, False
        if action == 1:
            self.player_hand.append(self._deck_pop())
            if self.calculate_hand(self.player_hand) > 21:
                done = True
                reward = -1
        else:
            done = True
            while self.calculate_hand(self.dealer_hand) < 17:
                self.dealer_hand.append(self._deck_pop())

            player_value = self.calculate_hand(self.player_hand)
            dealer_value = self.calculate_hand(self.dealer_hand)

            if dealer_value > 21 or player_value > dealer_value:
                reward = 1
            elif player_value < dealer_value:
                reward = -1
            else:
                reward = 0
        obs = self._get_obs()
        self.last_action = action
        return obs, reward, done, False, {}

    def render(self):
        print(f"{self.last_action} | "
              f"dealer hand: {self.dealer_hand} | "
              f"player hand: {self.player_hand}")

    # Create a deck
    def create_deck(self):
        deck = [(rank, suit) for suit in self.suits for rank in self.ranks] * self.num_decks
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


            action = player.get_action(self.calculate_hand(player_hand),self.values[dealer_hand[1][0]],bet)
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


