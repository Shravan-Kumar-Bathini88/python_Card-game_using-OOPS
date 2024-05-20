# In this game there are two players. Player 1 and Player 2. 
#The target is to get total rank close to 21 without crossing 21
# After shuffling the deck, two cards are distributed 1 each to the players.
#The players can choose to stop or proceed with the next round.
#If they decide to stop, whoever is having higher rank card wins!!
#If they decide to hit next round, again 1 card is distributed to each player.
#Again they have to decide whether to hit or stop.
#At any point in the game, if any player total rank crosses 21, he looses.
# If both players cross 21, player1 looses, game needs to be restarted
#Encoding
#Ranks of cards
#Spades => 3
#Hearts => 2
#Clubs => 0
#Ace => 1
#Jack => 11
#Queen => 12
#King => 13
import random

#define class cards and create objects for printing, comparing cards
class Card:
    suit_list = ["Clubs ♣", "Diamonds ♦", "Hearts ♥", "Spades ♠"]
    rank_list = ["None", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    def __init__(self, suit = 0, rank =2):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank_list[self.rank] + " of " + self.suit_list[self.suit]
    def __eq__(self, other):
        return (self.rank == other.rank and self.suit == other.suit)
    def __gt__(self, other):
        if self.suit > other.suit:
            return True
        elif self.suit == other.suit:
            if self.rank > other.rank:
                return True
        return False

# create class Deck for the deck, shuffling, pop, for deal
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
         s += i* " " + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        n_cards = len(self.cards)
        for i in range(n_cards):
            j = random.randrange(0, n_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def pop_card(self):
        return self.cards.pop()
    
    def is_empty(self):
        return len(self.cards) == 0
    def deal(self, hands, n_cards = 52):
        n_players = len(hands)
        for i in range(n_cards):
            if self.is_empty():
                break
            card = self.pop_card()
            current_player = i% n_players
            hands[current_player].add_card(card)

    
#class Hand(Deck):
 #   pass

#create class Hand for adding cards to the hand
class Hand(Deck):
    def __init__(self, name = ""):
        self.cards = []
        self.name = name
    def add_card(self, card):
        self.cards.append(card)
    def __str__(self):
        s = "Hand of " + self.name 
        if self.is_empty():
            return s + " is empty"
        s += " contains \n " + Deck.__str__(self)
        return s
    

#shuffle the cards and deal 1 cards to each player
d = Deck()
d.shuffle()
player1_hand = Hand("Player 1")
player2_hand = Hand("Player 2")
hands = [player1_hand, player2_hand]
d.deal(hands, 2)

#for calculating the value in a hand 
def calculate_hand_value(hand):
    value = 0
    has_ace = False

    card = d.pop_card
    for card in hand.cards:
        rank = card.rank

        if isinstance(rank, int):
            value += rank
    return value 

#calculate hand value for each of the players
while True:
    print(f'Player 1 hand: {player1_hand} ({calculate_hand_value(player1_hand)})')
    print(f'Player 2 hand: {player2_hand} ({calculate_hand_value(player2_hand)})')

    if calculate_hand_value(player1_hand) == 21 and calculate_hand_value(player2_hand) == 21:
        print('Tie!! Restart the game!')
        break
    elif calculate_hand_value(player1_hand) == 21:
        print('Player 1 wins!')
        break
    elif calculate_hand_value(player2_hand) == 21:
        print('Player 2 wins!')
        break
    elif (calculate_hand_value(player1_hand) > 21 and calculate_hand_value(player2_hand) > 21):
        print('Restart the game!')
        break
    elif calculate_hand_value(player1_hand) > 21:
        print('Player 1 lost!')
        break
    elif calculate_hand_value(player2_hand) > 21:
        print('Player 2 lost!')
        break

#asking input from the user whether to hit or stand
    action = input('Do you want to hit or stand? ')

    if action.lower() == 'hit':
        d.deal(hands, 2)
    else:
        break

print(f'Player 1 hand: {player1_hand} ({calculate_hand_value(player1_hand)})')
print(f'Player 2 hand: {player2_hand} ({calculate_hand_value(player2_hand)})')

#determining the winner
if calculate_hand_value(player1_hand) == 21:
        print('Player 1 wins!')
elif calculate_hand_value(player2_hand) == 21:
        print('Player 2 wins!')
elif (calculate_hand_value(player1_hand) > 21 and calculate_hand_value(player2_hand) > 21):
        print('Restart the game!')
elif calculate_hand_value(player1_hand) > 21:
        print('Player 1 lost!')
elif calculate_hand_value(player2_hand) > 21:
        print('Player 2 lost! Player1 wins!')
elif calculate_hand_value(player1_hand) > calculate_hand_value(player2_hand):
        print('Player 1 wins!')
elif calculate_hand_value(player1_hand) < calculate_hand_value(player2_hand):
        print('Player 2 wins!')
else:
        print('Tie!')