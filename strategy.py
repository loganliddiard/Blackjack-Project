## custom player object


class CustomPlaystyle:

    def __init__(self,minVal=17,dealerVal=0,bet_range=0):
        self.hit = 1
        self.stay = 0
        self

        self.hitWhenBelow = minVal

    ##Plays based on classic dealer playstyle
    def get_action(self,hand,dealer_hand,bet):

        if hand < self.hitWhenBelow:
            return self.hit

        else: return self.stay