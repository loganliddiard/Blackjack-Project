class OptimalPlayer:
    def __init__(self):
        self.hit = 1  # Represent "Hit"
        self.stay = 0  # Represent "Stay"
        self.player = "optimal"

        # Modified basic strategy table to exclude doubling and splitting
        self.basic_strategy = {
            (8, 1): 'H',  (8, 2): 'H',  (8, 3): 'H',  (8, 4): 'H',  (8, 5): 'H',  (8, 6): 'H',  (8, 7): 'H',  (8, 8): 'H',  (8, 9): 'H',  (8, 10): 'H',  (8, 11): 'H',
            (9, 1): 'H',  (9, 2): 'H',  (9, 3): 'H',  (9, 4): 'H',  (9, 5): 'H',  (9, 6): 'H',  (9, 7): 'H',  (9, 8): 'H',  (9, 9): 'H',  (9, 10): 'H',  (9, 11): 'H',
            (10, 1): 'H', (10, 2): 'H', (10, 3): 'H', (10, 4): 'H', (10, 5): 'H', (10, 6): 'H', (10, 7): 'H', (10, 8): 'H', (10, 9): 'H', (10, 10): 'H', (10, 11): 'H',
            (11, 1): 'H', (11, 2): 'H', (11, 3): 'H', (11, 4): 'H', (11, 5): 'H', (11, 6): 'H', (11, 7): 'H', (11, 8): 'H', (11, 9): 'H', (11, 10): 'H', (11, 11): 'H',
            (12, 1): 'H', (12, 2): 'H', (12, 3): 'S', (12, 4): 'S', (12, 5): 'S', (12, 6): 'S', (12, 7): 'H', (12, 8): 'H', (12, 9): 'H', (12, 10): 'H', (12, 11): 'H',
            (13, 1): 'H', (13, 2): 'S', (13, 3): 'S', (13, 4): 'S', (13, 5): 'S', (13, 6): 'S', (13, 7): 'H', (13, 8): 'H', (13, 9): 'H', (13, 10): 'H', (13, 11): 'H',
            (14, 1): 'H', (14, 2): 'S', (14, 3): 'S', (14, 4): 'S', (14, 5): 'S', (14, 6): 'S', (14, 7): 'H', (14, 8): 'H', (14, 9): 'H', (14, 10): 'H', (14, 11): 'H',
            (15, 1): 'H', (15, 2): 'S', (15, 3): 'S', (15, 4): 'S', (15, 5): 'S', (15, 6): 'S', (15, 7): 'H', (15, 8): 'H', (15, 9): 'H', (15, 10): 'H', (15, 11): 'H',
            (16, 1): 'H', (16, 2): 'S', (16, 3): 'S', (16, 4): 'S', (16, 5): 'S', (16, 6): 'S', (16, 7): 'H', (16, 8): 'H', (16, 9): 'H', (16, 10): 'H', (16, 11): 'H',
        }

    def get_action(self, player_hand, dealer_upcard, bet):
        """
        Determine the optimal strategy for the given player hand and dealer's upcard,
        without doubling or splitting.

        :param player_hand: The total value of the player's hand.
        :param dealer_upcard: The value of the dealer's upcard.
        :param bet: Current bet amount (unused, but could affect risk-based strategies in extensions).
        :return: 1 for Hit, 0 for Stay.
        """
        if player_hand < 8:  # Always hit if the hand is less than 8
            return self.hit
        
        if (player_hand, dealer_upcard) in self.basic_strategy:
            action = self.basic_strategy[(player_hand, dealer_upcard)]
            if action == 'H':
                return self.hit
            elif action == 'S':
                return self.stay
        
        # Default to hitting as a fallback
        return self.stay