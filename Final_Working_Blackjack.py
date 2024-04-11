#!/usr/bin/env python
# coding: utf-8

# In[21]:


def balance_():
    """Asks the user his total balance"""
    total_amount = 0
    while int(total_amount) < 100:
        try:
            total_amount = int(input("What's your total balance?💰 "))
            if total_amount < 100:
                print ("Minimum amount is 100")
                total_amount = int(input("What's your total balance?💰 "))
        except ValueError:
            print ("You have to give a number")
    return total_amount
    print (f"Your total balance is {total_amount}")


# In[22]:


def rules ():
    """Tells the rules to the user"""
    print (f"In this game of blackjack you must draw cards to get closer to 21 but without going past it, and you will play against the\
    dealer, whoever gets the sum closest to 21 wins. \
    \nNote: Every game must begin with a bet of 100 dollars.\
    \nNote: The House must stand on a hard 17 or more")


# In[23]:


def cards_value (cards): 
    """Describing the value of the cards"""
    if cards[0] in ['K','J', 'Q' ,'A']:
        return (10)
    elif cards[0] == 'A': 
        return (11)
    else:
        return int(cards[0])
    
    


# In[31]:


def shuffle_card(deck):
    """Shuffles the cards and stores them with the return"""
    random.shuffle(deck)
    
    user_card = [deck.pop(), deck.pop()]
    house_card = [deck.pop(), deck.pop()]
    return user_card, house_card
    


# In[32]:


def cards_of_user(user,user_card, user_hand):
    """Shows user cards and score"""
    print (user,"has",user_card)
    print(user, "score: ", user_hand)
    print("\n")


# In[41]:


def total_balance (total_amount,amount):
    """Counts the total balance"""
    total = total_amount + amount
    print ("Final amount:", total)
    if total >= 100:
        print ("💵")
    return total


# In[42]:


def owe_to_house (total_amount):
    """Checks if total balance is less than 0"""
    if total_amount < 0:
        print (f"you owe the house {total_amount}💸")


# In[43]:


def bold(type):
    import sys
    sys.stdout.write("\033[1m" + type + "\033[0m")


# In[ ]:


print ("Welcome to Blackjack")
rules ()
total_amount = balance_()


while True:
    play_game = input("\nDo you want to play Blackjack? yes or no: ")

 
    if play_game.lower().startswith("y"):
        game_on = True
    elif play_game.lower().startswith("n"):
        game_on = False
        break
    else:
        print ("Please answer yes or no")
        play_game = input("\nDo you want to play Blackjack? yes or no: ")
        
        

    while game_on:
        
        bold("\n\nNEW ROUND\n")
        
        import random 
        
        card_cat = ["💎", "♠️", "❤️", "♣️"]
        card_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q","K"]
        deck = [(cards, cat) for cat in card_cat for cards in card_list ]
        
        user_card, house_card = shuffle_card(deck)
        user = "user"
        dealer = "house"

        user_hand = sum(cards_value(cards) for cards in user_card)
        house_hand = sum(cards_value(cards) for cards in house_card)
        cards_of_user(user,user_card, user_hand) 
        cards_of_user(dealer,house_card, house_hand)
        print ("-------------------------------------------")
        
        while user_hand < 21:
            user_input = str(input("Would you like another card? yes or no\n"))
            if user_input.lower().startswith("y"):
                new_card = deck.pop()
                user_card.append(new_card)
                user_hand += cards_value(new_card)
                cards_of_user(user,user_card,user_hand)
                cards_of_user(dealer,house_card,house_hand)
                print ("-------------------------------------------")
            elif user_input.lower().startswith("n"):
                break
            else:
                print("Wrong answer. Please reply with yes or no.")
                continue
            
        if user_hand > 21:
            if house_hand > 21:
                cards_of_user(dealer,house_card,house_hand)
                bold ("Everybody loses\n")
                total_amount = total_balance(total_amount,0)
                owe_to_house (total_amount)
            elif house_hand < 17:
                print ("*Turn for the house to draw cards:")
                new_card = deck.pop()
                house_card.append(new_card)
                house_hand += cards_value(new_card)
                if house_hand > 21:
                    cards_of_user(dealer,house_card,house_hand)
                    bold ("Everybody loses\n")
                    total_amount = total_balance(total_amount,0)
                    owe_to_house (total_amount)
                else:
                    cards_of_user(dealer,house_card,house_hand)
                    bold ("Bummer, you have lost\n")
                    total_amount = total_balance(total_amount,-100)
                    owe_to_house (total_amount)
            else:
                cards_of_user(user,user_card,user_hand)
                cards_of_user(dealer,house_card,house_hand)
                bold ("House wins, bummer\n")
                total_amount = total_balance(total_amount,-100)
                owe_to_house (total_amount)
    
            break
        
        while house_hand < 17:
            print ("*Turn for the house to draw cards*")
            new_card = deck.pop()
            house_card.append(new_card)
            house_hand += cards_value(new_card)
            
        print ("-------------------------------------------")    
        cards_of_user(user,user_card, user_hand) 
        cards_of_user(dealer,house_card, house_hand)
        print ("-------------------------------------------")
    
        if house_hand > 21:
            #cards_of_user(dealer,house_card, house_hand)
            bold ("House has lost. Congratulations to the winner👑\n")
            total_amount = total_balance(total_amount,+100)
            owe_to_house (total_amount)
            break
        elif user_hand > house_hand:
            #cards_of_user(user,user_card, user_hand) 
            #cards_of_user(dealer,house_card, house_hand)
            total_amount = total_balance(total_amount,+100)
            owe_to_house (total_amount)
            bold ("Congratulations, you won🎉")
            break
        elif house_hand > user_hand:
            #cards_of_user(user,user_card, user_hand) 
            #cards_of_user(dealer,house_card, house_hand)
            total_amount = total_balance(total_amount,-100)
            owe_to_house (total_amount)
            bold ("Oh no, you have lost")
            break
        else: 
            #cards_of_user(user,user_card, user_hand) 
            #cards_of_user(dealer,house_card, house_hand)
            bold ("It´s a tie.")
            total_amount = total_balance(total_amount,0)
            owe_to_house (total_amount)
            break
     
            
        
        

    
        
        
        

    

        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




