# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 54

# The file, poker.txt, contains one-thousand random hands dealt to two players. 
# Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. 
# You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
# How many hands does Player 1 win?
    

from enum import Enum

class Suit(Enum):
    SPADES = 0
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3

    @staticmethod
    def get_suit_from_letter(letter):
        if letter == 'S':
            return Suit.SPADES
        if letter == 'C':
            return Suit.CLUBS
        if letter == 'D':
            return Suit.DIAMONDS
        if letter == 'H':
            return Suit.HEARTS

class Value(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8 
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    @staticmethod
    def get_value_from_letter(letter):
        if letter == 'A':
            return Value.ACE
        if letter == 'T':
            return Value.TEN
        if letter == 'J':
            return Value.JACK
        if letter == 'Q':
            return Value.QUEEN
        if letter == 'K':
            return Value.KING
        
    def __gt__(self,other):
        return self.value > other.value
        
    def __lt__(self,other):
        return self.value < other.value

class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    @staticmethod
    def new_card(card):
        value = Value(int(card[0])) if card[0].isdigit() else Value.get_value_from_letter(card[0])
        suit = Suit.get_suit_from_letter(card[1])
        return Card(value,suit)

    def is_suit(self,suit):
        return self.suit == suit

    def same_value(self,other):
        return self.value == other.value

    def __str__(self):
        return self.value.name + ' of ' + self.suit.name
    
    def __eq__(self,other):
        return self.value == other.value and self.suit == other.suit

    def __lt__(self,other):
        return self.value.value < other.value.value

    def __gt__(self,other):
        return self.value.value > other.value.value

class Hand:
    def __init__(self,cards):
        self.cards = [Card.new_card(c) for c in cards]
        
    def __str__(self):
        return str([str(card) for card in self.cards])
        
    @staticmethod
    def decide(p1,p2):
        if p1 is not None:
            if p2 is not None:
                if p1 == p2 or (isinstance(p1,Card) and isinstance(p2,Card) and p1.value == p2.value):
                    return False, None
                return True, p1 > p2
            return True, True
        elif p2 is not None:
            return True, False
        return False, None

    def high_card(self):
        return sorted(self.cards)[-1]

    def has_value(self,value):
        for card in self.cards:
            if card.value == value:
                return True
        return False

    def has_values(self,values):
        for value in values:
            if not self.has_value(value):
                return False
        return True

    def flush(self):
        suit = self.cards[0].suit
        for card in self.cards:
            if not card.is_suit(suit):
                return None
        return self.high_card()

    def royal_flush(self):
        if not self.flush():
            return False
        return self.has_values([Value.TEN, Value.JACK, Value.QUEEN, Value.KING, Value.ACE])
    
    def straight_flush(self):
        if not self.flush():
            return None
        return self.straight()

    def full_house(self):
        if len(self.pairs()) < 2:
            return None
        return self.three_of_a_kind()

    def straight(self):
        sort = sorted(self.cards)
        if sort[0].value.value == sort[1].value.value-1 == sort[2].value.value-2 == sort[3].value.value-3 == sort[4].value.value-4:
            return self.high_card()
        return None

    def four_of_a_kind(self):
        cards = sorted(self.cards)
        if cards[0].same_value(cards[3]) or cards[-4].same_value(cards[-1]):
            return cards[2].value
        return None
    
    def three_of_a_kind(self):
        cards = sorted(self.cards)
        if cards[0].same_value(cards[2]) or cards[-3].same_value(cards[-1]) or cards[1].same_value(cards[3]):
            return cards[2].value
        return None

    def pairs(self):
        cards = sorted(self.cards)
        pairs = set()
        for i in range(len(cards)-1):
            if cards[i].same_value(cards[i+1]):
                pairs.add(cards[i].value)
        return pairs

    def two_pair(self):
        pairs = self.pairs()
        if len(pairs) == 2:
            return max(pairs)
        return None
        
    def one_pair(self):
        pairs = self.pairs()
        if len(pairs) >= 1:
            return max(pairs)
        return None

    def beats(self,other):
        if self.royal_flush():
            return True,"Royal flush"
        if other.royal_flush():
            return False,"Royal flush"

        decided,winner = Hand.decide(self.straight_flush(),other.straight_flush())
        if decided:
            return winner,"Straight flush"
        decided,winner = Hand.decide(self.four_of_a_kind(),other.four_of_a_kind())
        if decided:
            return winner,"4 of a kind"
        decided,winner = Hand.decide(self.full_house(),other.full_house())
        if decided:
            return winner,"Full house"
        decided,winner = Hand.decide(self.flush(),other.flush())
        if decided:
            return winner,"Flush"
        decided,winner = Hand.decide(self.straight(),other.straight())
        if decided:
            return winner,"Straight"
        decided,winner = Hand.decide(self.three_of_a_kind(),other.three_of_a_kind())
        if decided:
            return winner,"Three of a kind"
        decided,winner = Hand.decide(self.two_pair(),other.two_pair())
        if decided:
            return winner,"Two pair"
        decided,winner = Hand.decide(self.one_pair(),other.one_pair())
        if decided:
            return winner,"One pair"
        return self.high_card() > other.high_card(),"High card"

def play_poker(file):
    with open(file) as poker_file:
        count = 0
        for line in poker_file:
            cards = line.strip().split(" ")
            p1 = Hand(cards[:5])
            p2 = Hand(cards[5:])
            winner,_ = p1.beats(p2)
            if winner:
                count += 1
        return count

print(play_poker("Problem54/poker.txt"))