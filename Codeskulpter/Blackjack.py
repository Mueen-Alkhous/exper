# Mini-project #6 - Blackjack

import simplegui
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
player_score = 0
dealer_score = 0
player_value = 0
dealer_value = 0

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
        self.hand = []

    def __str__(self):
        string = "Hand contains "
        for i in self.hand:
            string += str(i) + " "
        return string
        
    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        global player_value, dealer_value
        if self == player_hand:
            player_value = 0
            for i in self.hand:
                player_value += VALUES[str(i)[1]]
            for i in self.hand:
                if str(i)[1] == "A":
                    if player_value + 10 <= 21:
                        return player_value + 10
            return player_value
        if self == dealer_hand:
            dealer_value = 0
            for i in self.hand:
                dealer_value += VALUES[str(i)[1]]
            for i in self.hand:
                if str(i)[1] == "A":
                    if daeler_value + 10 <= 21:
                        return dealer_value + 10
            return dealer_value
            
   
    def draw(self, canvas, pos):
            for i in self.hand:
                i.draw(canvas, pos)
                pos[0] += CARD_SIZE[0]

# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for i in SUITS:
            for r in RANKS:
                self.deck.append(Card(i, r))

    def shuffle(self):
        random.shuffle(self.deck)
        

    def deal_card(self):
        return random.choice(self.deck)
    
    
    def __str__(self):
        deck_repr = ""
        for i in self.deck:
            deck_repr += (str(i)) + " "
        return "Deck contains " + str(deck_repr)

#define event handler for the deal button
def deal():
    #defining global variables
    global outcome, in_play, player_hand, dealer_hand, shuffled_deck,dealer_score
    
    # create a shuffled deck to choose a hand from it
    shuffled_deck = Deck()
    shuffled_deck.shuffle()
    
    # craete the player and dealer hands
    dealer_hand = Hand()
    player_hand = Hand()
    
    # add two cards to the daeler's hand
    dealer_hand.add_card(Deck.deal_card(shuffled_deck))
    dealer_hand.add_card(Deck.deal_card(shuffled_deck))
    
    # add two cards to the player's hand
    player_hand.add_card(Deck.deal_card(shuffled_deck))
    player_hand.add_card(Deck.deal_card(shuffled_deck))
    
    # get the value of a hand
    player_hand.get_value()
    dealer_hand.get_value()
    
    # add a point to the dealer if the player click deal in the middle of a match
    if in_play:
        dealer_score += 1
    in_play = True

#define event handler for the hit button
def hit():
    global player_hand, in_play, dealer_score
    if in_play:
        if player_hand.get_value() <=  21:
            player_hand.add_card(Deck.deal_card(shuffled_deck))
            if player_hand.get_value() > 21:
                in_play = False
                dealer_score += 1

#define event handler for the stand button
def stand():
    global in_play, player_score, dealer_score
    if in_play == True:
        # implementing the dealer's rules
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(Deck.deal_card(shuffled_deck))
            
        player_score += 1
        in_play = False

# draw handler
def draw(canvas):
    # drawing the player part on the canvas
    player_hand.draw(canvas, [110, 600-CARD_SIZE[1]-10])
    canvas.draw_text("Player", [0, 600-CARD_SIZE[1]+10], 25, "Black")
    canvas.draw_line([0, 600 - 110], [600, 600 - 110], 5, "Red")
    canvas.draw_line([0, 600 - 5], [600, 600 - 5], 5, "Red")
    canvas.draw_text("Score:" + str(player_score), [0, 600 - 10], 25, "Black")
    canvas.draw_text("Value:" + str(player_value), [0, 600 - 48], 25, "Black")
    
    # drawing the dealer parn on the canvas
    dealer_hand.draw(canvas, [110, 10])
    canvas.draw_text("Dealer", [0, 30], 25, "Black")
    canvas.draw_line([0, 5], [600, 5], 5, "Red")
    canvas.draw_line([0, CARD_SIZE[1] + 15], [600, CARD_SIZE[1] + 15], 5, "Red")
    canvas.draw_text("Score:" + str(dealer_score), [0, 100], 25, "Black")
    
    
    # drawing the title of the game and draw some decoration
    canvas.draw_text("Blackjack", [180, 300], 50, "Black")
    canvas.draw_line([0, 281], [180, 281], 5, "Red")
    canvas.draw_line([390, 281], [600, 281], 5, "Red")
    
    # hiding the dealer (hole) card and draw the actions for the player
    if in_play:
        canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE, [110 + CARD_CENTER[0], CARD_CENTER[1] + 10], CARD_SIZE)
        canvas.draw_text("Hit or Stand ?", [0, 482], 25, "Black")
    else:
        canvas.draw_text("New Deal ?", [0, 480], 25, "Black")
        
# drawing the result of a match
    if not in_play:
        canvas.draw_text("Value:" + str(dealer_value), [0, 65], 25, "Black")
        
        # if the dealer busted
        if dealer_hand.get_value() > 21:
            canvas.draw_text("You Lose", [240, 200], 25, "Black")
            canvas.draw_text("(Busted)", [245, 230], 25, "Black")
            canvas.draw_text("You Win", [240, 400], 25, "Black")
        
        # if the player busted
        elif player_hand.get_value() > 21:
            canvas.draw_text("You Win", [240, 200], 25, "Black")
            canvas.draw_text("You Lose", [240, 400], 25, "Black")
            canvas.draw_text("(Busted)", [245, 430], 25, "Black")
        
        # if the dealer beat the player
        elif dealer_hand.get_value() > player_hand.get_value():
            canvas.draw_text("You Win", [240, 200], 25, "Black")
            canvas.draw_text("You Lose", [240, 400], 25, "Black")
        
        # if the player beat the dealer
        elif dealer_hand.get_value() < player_hand.get_value():
            canvas.draw_text("You Lose", [240, 200], 25, "Black")
            canvas.draw_text("You Win", [240, 400], 25, "Black")
            
        # if the player and dealer tie    
        elif dealer_hand.get_value() == player_hand.get_value():
            canvas.draw_text("You Win", [240, 200], 25, "Black")
            canvas.draw_text("You Lose", [240, 400], 25, "Black")
        

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()
deal()

# remember to review the gradic rubric