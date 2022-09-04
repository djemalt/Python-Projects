#!/usr/bin/env python
# coding: utf-8

# # Initial Setup

# In[2]:


#Card
#suit, Rankm Value
import random

suits = ("Hearts","Diamonds","Spades","Clubs")
ranks = ("Two","Three" ,"Four" , "Five", "Six", "Seven", "Eight", "Nine", "Ten" , "Jack", "Queen", "King" , "Ace")

values = { "Two" : 2,"Three": 3 ,"Four" : 4, "Five": 5, "Six":6, "Seven":7, "Eight":8,
          "Nine":9, "Ten" :10, "Jack":11, "Queen": 12, "King" : 13, "Ace":14}
#Deck

#player

#game logic


# #  Create the Card Class

# In[3]:


#Card
#suit, Rankm Value
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit


# #  Create the Deck Class

# In[4]:


class Deck:
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                #create the card object
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()


# #  Create Player Class

# In[5]:


class Player:
    
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        #list of multiple card objects
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
            #for a single card object
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


# # Game setup + logic - Run to play

# In[6]:


#Game Setup / Reset
player_one = Player("One")
player_two = Player("Two")

# shuffle deck
new_deck = Deck()
new_deck.shuffle()


#split deck to each player
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


game_on = True

#start game
round_num = 0

while game_on:
    
    round_num +=1
    print(f"Round {round_num}")
    #check if P1 has cards
    if len(player_one.all_cards) == 0:
        print('Player One has Lost!')
        game_on = False
        break
    #check if P2 has cards   
    if len(player_two.all_cards) == 0:
        print('Player Two has Lost!')
        game_on = False
        break
        
    #start new round
    #p1 plays cards
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())
    #p2 plays cards
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
        
    # comparison
    at_war = True
    while at_war:
        
        
        #check if P1 wins, gets all cards
        if player_one_cards[-1].value > player_two_cards[-1].value:
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            at_war = False
        
        #check if P2 wins, gets all cards
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            at_war = False
        #else at War!
        else:
            print("War")
            
            #makes sure each player has at least 5 cards, if not they lose and cant declare war
            if len(player_one.all_cards) < 5:
                print("Player one unable to declare war")
                print("Player two wins")
                game_on = False
                break
                
                
            elif len(player_two.all_cards) < 5:
                print("Player Two unable to declare war")
                print("Player One wins")
                game_on = False
                break
            
            #if so, draw 5 more cards at war, and go back up
            for num in range(5):
                player_one_cards.append(player_one.remove_one())
                player_two_cards.append(player_two.remove_one())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




