class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        """suit和value的值均为整型数"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return False
            else:
                return True
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return False
            else:
                return True
        return False

#    def __repr__(self):
#        v = self.values[self.value] + " of " + self.suits[self.suit]
#        return v


a = Card(3, 2)
b = Card(3, 1)
print(a < b)
