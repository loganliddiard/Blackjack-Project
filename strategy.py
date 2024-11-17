



class Classic_Playstyle:

    def __init__(self,minVal):
        self.hit = 1
        self.stay = 0

        self.hitWhenBelow = minVal

    ##Plays based on classic dealer playstyle
    def get_action(self,hand,dealer_hand,bet):

        if hand < self.hitWhenBelow:
            return self.hit

        else: return self.stay