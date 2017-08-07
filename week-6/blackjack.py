#!/usr/bin/env python
# Mini-project #6 - Blackjack
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []

    def __str__(self):
        # return a string representation of a hand
        cards = ""
        for i in range(len(self.hand)):
            cards += str(self.hand[i])
            cards += " "
        return "Hand contains " + cards

    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        count = 0
        for i in range(len(self.hand)):
            value += VALUES[self.hand[i].get_rank()]
        for j in range(len(self.hand)):
            if (self.hand[i].get_rank()) == 'A':
                count += 1
        if count == 0:
            return value
        else:
            if value + 10 <= 21:
                return value + 10
            else:
                value
        
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.hand)):
            self.hand[i].draw(canvas, pos)
            pos[0] += 92

        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        card = self.deck.pop()
        return card
    
    def __str__(self):
        # return a string representing the deck
        deck = ""
        for i in range(len(self.deck)):
            deck += str(self.deck[i])
            deck += " "
        return "Deck contains" + deck



#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, my_deck, dealer_hand, score
    outcome = ""
    if in_play:
        score -= 1
        outcome = "You lose"
    my_deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    my_deck.shuffle()
    player_hand.add_card(my_deck.deal_card())
    player_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())
    #print "player's", player_hand
    #print "dealers's", dealer_hand
    in_play = True

def hit():
    # if the hand is in play, hit the player
    global in_play, outcome, score
    if in_play == True:
        if player_hand.get_value() <= 21:
            player_hand.add_card(my_deck.deal_card())
        if player_hand.get_value() > 21:
            #print "Busted"
            outcome = "You went bust and lose"
            score -= 1
            in_play = False
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play, outcome, score
    if in_play == False:
        #print "You have been busted"
        outcome = "You have been busted"
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(my_deck.deal_card())
    # assign a message to outcome, update in_play and score
    if dealer_hand.get_value() > 21:
        #print "Dealer busted, You win"
        outcome = "Dealer busted, You win"
        if in_play:
            score += 1
            in_play = False
    else:
        #print "player hand: ", player_hand.get_value()
        #print "Dealer hand", dealer_hand.get_value()
        if dealer_hand.get_value() >= player_hand.get_value():
            outcome = "Dealer wins"
            if in_play:
                score -= 1
                in_play = False
        else:
            outcome = "You Wins"
            if in_play:
                score += 1
                in_play = False
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Blackjack', [150, 60], 60, 'Red', 'sans-serif')
    canvas.draw_text('Player', [20, 370], 30, 'Black')
    player_hand.draw(canvas, [20, 400])
    canvas.draw_text('Dealer', [20, 170], 30, 'Black')
    dealer_hand.draw(canvas, [20, 200])
    if in_play:
        canvas.draw_text('Hit or Stand?', [130, 370], 30, 'Yellow')
    else:
        canvas.draw_text('New Deal?', [130, 370], 30, 'Yellow')
        
    canvas.draw_text(outcome, [170, 170], 20, 'Black')
    canvas.draw_text("Score: " + str(score), [400, 130], 30, 'Black')
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (CARD_BACK_CENTER[0] + 20, CARD_BACK_CENTER[1]+200), CARD_SIZE)
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
