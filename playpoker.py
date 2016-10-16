#  File: playpoker.py
#  Description: Write a program that simulates a variation of Poker called "5-Card Draw"
#  Student's Name: Thu Anh Le
#  Student's UT EID: tal864
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 09/22/2015
#  Date Last Modified: 09/24/2015



# import the random number generator
# this is needed to shuffle the cards into a random order

import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank, suit):
    # each Card object consists of two attributes: a rank
    #    and a suit
    self.rank = rank
    self.suit = suit
    
  def __str__ (self):
    # print J, Q, K, A instead of 11, 12, 13, 14
    if self.rank == 14:
      rank = 'A'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 11:
      rank = 'J'
    else:
      rank = self.rank
    return str(rank) + self.suit

  # you'll find the following methods to be useful:  they 
  #    allow you to compare Card objects

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)



class Deck (object):

  def __init__ (self):
    # self.deck is the actual deck of cards
    # create it by looping through all SUITS and RANKS
    #    and appending them to a list
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  def shuffle (self):
    # the shuffle method in the random package reorders
    #    the contents of a list into random order
    random.shuffle (self.deck)

  def deal (self):
    # if the deck is empty, fail:  otherwise pop one
    #    card off and return it
    if len(self.deck) == 0:
      return None
    else:
      return self.deck.pop(0)
      
class Poker (object):
  #
  # when you create an object of class Poker, you
  #    create a deck, shuffle it, and deal cards
  #    out to the players.
  #
  def __init__ (self, numHands):
    self.deck = Deck()              # create a deck
    self.deck.shuffle()             # shuffle it
    self.hands = []
    numCards_in_Hand = 5
 


    for i in range (numHands):
      # deal out 5-card hands to numHands players
      # you'd actually get shot if you dealt this
      #    way in a real poker game (5 cards to
      #    the first player, 5 to the next, etc.)
      hand = []
      for j in range (numCards_in_Hand):
        hand.append (self.deck.deal())
      self.hands.append (hand)

  def play (self):
  # start playing the poker game and evaluate hands
    total_points = 0 # total points each hand has according to card ranking
    h = 0 # assigned value for each category
    max_list = [] # to get the highest rank card
    dict_list = []

    for i in range (len(self.hands)):
      # the method "sorted" returns a sorted list without
      #   altering the original list.  reverse = True
      #   makes it sort in decreasing order
      sortedHand = sorted (self.hands[i], reverse = True)
      hand = ''
      rank_list = [] # create an array of all the cards needed to be royal_flush
      for card in sortedHand:
        hand = hand + str(card) + ' '
      print ('Hand ' + str(i + 1) + ': ' + hand)

    dict = {} # create a dict with total points as keys and hand number as values
    print()
    for x in range (len(self.hands)): # create another loop to print out hand evaluations
      sortedHand = sorted (self.hands[x], reverse = True)
      # c1, c2, c3, c4, and c5 are the ranks of the cards in the hand, where c1 is the highest ranking card and c5 is the lowest ranking card
      #
      # This is used to calculate total points of a hand
      c1 = sortedHand[0].rank; c2 = sortedHand[1].rank; c3 = sortedHand[2].rank; c4 = sortedHand[3].rank; c5 = sortedHand[4].rank
     

      # evaluate whether a hand is royal flush, flush, straight flush, four of a kind, three of a kind, one pair, two pair and high card
      #
      #Print out the one with the highest value
      if( Poker.is_royal(self, sortedHand) == True):
        h = 10 
        print('Hand ' + str(x + 1) + ': ' + "Royal Flush")
        dict[total_points] = x + 1
   
    
      elif( Poker.is_straight_flush(self, sortedHand) == True):
        h = 9 
        print('Hand ' + str(x + 1) + ': ' + "Straight Flush")
        dict[total_points] = x + 1
    
      elif( Poker.is_four(self, sortedHand) == True):
        # c1, c2, c3, and c4 are the ranks of the four of a kind cards and c5 is the side card
        point_dict = {}
        for card in sortedHand:
          if card.rank in point_dict:
            point_dict[card.rank] += 1
          else:
            point_dict[card.rank] = 1
        for key in point_dict.keys:
          if (point_dict[key] == 4):
            c1 = c2 = c3 = c4 = key
          else:
            c5 = key
        h = 8
        print('Hand ' + str(x + 1) + ': ' + "Four Of A Kind")
        dict[total_points] = x + 1
   

      elif( Poker.is_full(self, sortedHand) == True):
        # c1, c2, and c3 are the ranks of the three cards having the same rank and c4 and c5 are the ranks of the two remaining cards having the same rank.
        point_dict = {}
        for card in sortedHand:
          if card.rank in point_dict:
            point_dict[card.rank] += 1
          else:
            point_dict[card.rank] = 1
        for key in point_dict.keys:
          if (point_dict[key] == 3):
            c1 = c2 = c3 = key
          else:
            c5 = c4 = key
        h = 7
        print('Hand ' + str(x + 1) + ': ' + "Full House")
        dict[total_points] = x + 1
       

      elif( Poker.is_flush(self, sortedHand) == True):
        h = 6
        print('Hand ' + str(x + 1) + ': ' + "Flush")
        dict[total_points] = x + 1
     

      elif( Poker.is_straight_flush(self, sortedHand) == True):
        h = 5
        print('Hand ' + str(x + 1) + ': ' + "Straight")
        dict[total_points] += x + 1
      

      elif( Poker.is_three(self, sortedHand) == True):
        # c1, c2, and c3 are the ranks of the three cards of the same rank and c4 and c5 are the ranks of the remaining cards where c4 has higher rank than c5
        point_dict = {}
        for card in sortedHand:
          if card.rank in point_dict:
            point_dict[card.rank] += 1
          else:
            point_dict[card.rank] = 1
        c4 = 0
        for key in reversed(sorted(point_dict.keys())):
          if (point_dict[key] == 3):
            c1 = c2 = c3 = key
          else:
            if (c4 == 0):
              c4 = key
            else:
              c5 = key
        h = 4
        print('Hand ' + str(x + 1) + ': ' + "Three Of A Kind")
        dict[total_points] = x + 1
       

      elif( Poker.is_two(self, sortedHand) == True):
        # c1 and c2 are the ranks of the first and higher ranking pair. c3 and c4 are the ranks of the second and lower ranking pair. c5 is the rank of the remaining side card.
        point_dict = {}
        for card in sortedHand:
          if card.rank in point_dict:
            point_dict[card.rank] += 1
          else:
            point_dict[card.rank] = 1
        c1 = 0
        for key in reversed(sorted(point_dict.keys())):
          if (point_dict[key] == 2):
            if c1 == 0:
              c1 = c2 = key
            else:
              c3 = c4 = key
          else:
            c5 = key
        h = 3
        print('Hand ' + str(x + 1) + ': ' + "Two Pairs")    
        dict[total_points] = x + 1
       
      elif( Poker.is_one(self, sortedHand) == True):
        # c1 and c2 are the ranks of the pair of cards having the same rank. c3, c4, and c5 are the ranks of the side cards from highest to lowest rank.
        point_dict = {}
        for card in sortedHand:
          if card.rank in point_dict:
            point_dict[card.rank] += 1
          else:
            point_dict[card.rank] = 1

        c3 = c4 = 0
        for key in reversed(sorted(point_dict.keys())):
          if (point_dict[key] == 2):
            c1 = c2 = key
          else:
            if ( c3 == 0):
              c3 = key
            elif ( c4 == 0):
              c4 = key
            else:
              c5 = key
        h = 2
        print('Hand ' + str(x + 1) + ': ' + "One Pair")
        dict[total_points] = x + 1
      
      else:
        h = 1
        dict[total_points] = x + 1

      # Calculates total points of the cards
      total_points = h * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5  
      max_list.append(total_points)
    max_value = max(max_list) # Determine the hand with highest total point
  
    if max_value in dict.keys():
      print()
      print('Hand', dict.get(max_value) - 1 , 'wins.')  # Print out the winning hand
    else:
      print()
      print('Hand', str(sorted(dict.values())[-1]), 'wins.') 


  def is_flush (self, hand):
    # Check if the hand has a Flush
    #
    # all five cards have the same suit. The numerical ranks do not matter
    single_suit = hand[0].suit
    for card in hand:
      if single_suit != card.suit:
        return False
    return True

  def is_royal (self, hand):
    # Check if the hand has a royal flush
    #
    # consists of a 10, Jack, Queen, King, and Ace all of the same suit
    rank_list = [14, 13, 12, 11, 10]
    if (Poker.is_flush(self, hand)):
      for card in range (len(rank_list)):
        if rank_list[card] != hand[card].rank: # if one of the rank in hand is different from rank_list
          return False
      return True
    return False 

  def is_straight (self, hand):
    # Check if the hand has a straight 
    #
    # consists of 5 cards in consecutive numerical sequence
    for card in range (len(hand)):
        if hand[card].rank - 1 != hand[card + 1].rank: 
          return False
    return True

  def is_straight_flush (self, hand):
    # Check if a card has a straight flush
    #
    # consists of 5 cards in consecutive numerical sequence, all of the same suit
    if (Poker.is_flush(self, hand)):
     if (Poker.is_straight(self, hand)):
      return True
  
  def is_one (self, hand):
    # Check if the card has a pair
    #
    # has two cards of the same rank. The other three cards can be anything
    num_set = set()
    for card in hand:
      num_set.add(card.rank)

    if len(hand) == len(num_set) + 1 :
      return True
    return False

  def is_two (self, hand):
    # Check if the card has two pairs
    #
    # there are two cards of a matching rank, another two cards of a different matching rank, and a fifth card which can be anything
    num_set=set()
    for card in hand:
      num_set.add(card.rank)

    if len(hand) == len(num_set) + 2 :
      return True
    return False


  def is_four (self, hand):
    # Check if there are four pairs
    #
    # Create a Hashtable to count the number of occurences from a distinct rank number on a card
    dict = {}
    # Set card rank as keys and the number of occurences as values
    for card in hand:
      if card.rank in dict:
        # if the rank number is in dict, then add one if occurs again
        dict [card.rank] += 1
        # if the number of occurences reaches 4, then return True
        if dict [card.rank] == 4:
          return True
      else:
        # if the rank number is not in dict yet, add it in
        dict [card.rank] = 1
    return False

  def is_three (self, hand):
    # Check if there are three pairs
    #
    # Create a Hashtable to count the number of occurences from a distinct rank number on a card
    dict = {}
    # Set card rank as keys and the number of occurences as values
    for card in hand:
      if card.rank in dict:
        # if the rank number is in dict, then add one if occurs again
        dict [card.rank] += 1
        # if the number of occurences reaches 3, then return True
        if dict [card.rank] == 3:
          return True
      else:
        # if the rank number is not in dict yet, add it in
        dict [card.rank] = 1
    return False

  def is_full (self, hand):
    # Check if the hand has a full house
    #
    # three of the cards must have the same numerical rank as each other, and the the two remaining cards must have the same numerical rank
    #
    # Create a Hashtable to count the number of occurences from a distinct rank number on a card
    dict = {}
    count = 0
    # Set card rank as keys and the number of occurences as values
    for card in hand:
      if card.rank in dict:
        dict [card.rank] += 1
      else:
        dict [card.rank] = 1
    
    for x in dict.values():
     # if found 2 occurences of a rank (1 pair) in dict, then add 1 to count
      if x == 2 :
        count += 1
     # if found 3 occurences of a rank in dict, add 2 to count to prevent the case of 2 pairs
      if x == 3 :
        count += 2

    return count == 3

  def is_high (self, hand):
    return hand[0].rank
   


def main():

  numHands = int (input ('Enter number of hands to play: '))

  # need at least 2 players but no more than 6
  while (numHands < 2 or numHands > 6):
    numHands = int (input ('Enter number of hands to play: '))

  # create a Poker object:  create a deck, shuffle it, and
  # deal out the cards
  game = Poker (numHands)

  # play the game
  game.play()


main()
