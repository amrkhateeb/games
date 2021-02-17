#____________________________ {Classes}_______________________________________

#this class is for player's total balance ,and bets he wants to pay each turn
class Money():
    def __init__(self,player_money=0,table_money=0):
        self.player_money = player_money
        self.table_money = table_money
    #this method asks for total balance
    def player_money_ask(self):
            true_player_money=True
            while true_player_money:
                try:
                    self.player_money = int(input('Please enter Your bets Balance value as number:'))
                except:
                    print('This is not a number please provid a number: ')
                    continue
                else:
                    print('Thank You')
                    true_player_money = False
            return self.player_money

    #this method asks the player for the bets to paid each turn
    def table_money_ask(self):
        bets=0
        true_table_money=True
        while true_table_money:
            try:
                self.table_money=int(input('Please Enter the bets for this round: '))
            except:
                print('This is not a number please provid a number: ')
                continue
            else:
                print('Thank You')
                true_table_money = False
                self.player_money=self.player_money - self.table_money
        return self.table_money

    #this method will modify the balance of the player based on the result
    def results(self,BJ='won'):
        if BJ=='won':
            self.player_money = self.player_money + (2 * self.table_money)
        elif BJ =='BJ':
            self.player_money = self.player_money + self.table_money + ((3/2) * self.table_money)
        elif BJ=='draw':
            self.player_money = self.player_money + self.table_money
        elif BJ=='lost':
            pass
        return  self.player_money

#------------------------------------------------------------------------------
#this Class usning [random] class to choose a random card from the Game cards
#in each turn for player and dealer,the random choice will be deleted from Game cards to avoid duplicate cards. 
#player's and deale's cards will be stored in lists to be printed in a Card form

from IPython.display import clear_output
class Table():
    def __init__(self,cards,player_list=[],dealer_list=[]):
        self.cards = cards
        self.player_list = player_list
        self.dealer_list = dealer_list
    def open_round(self):
        
        cardpart1='._____.  '
        cardpart2='|     |  '
        cardpart3=f'| {"  "}♦ |  '
        cardpart4='|_____|  '
        from random import choice
        random_choice = choice(self.cards)
        self.player_list.append(random_choice)
        self.cards.remove(random_choice)

        random_choice = choice(self.cards)
        self.dealer_list.append(random_choice)
        self.cards.remove(random_choice)

        random_choice = choice(self.cards)
        self.player_list.append(random_choice)
        self.cards.remove(random_choice)
        p=''
        d=''
        for index,number in enumerate(self.player_list):
            if number in ['10♥','10♠','10♦','10♣']:
                p = p + f'| {self.player_list[index]} |  ' 
            else:
                p = p + f'|  {self.player_list[index]} |  '     
        
        c=p
        for index,number in enumerate(self.dealer_list):
            if number in ['10♥','10♠','10♦','10♣']:
                d = d + f'| {self.dealer_list[index]} |  ' 
            else:
                d = d + f'|  {self.dealer_list[index]} |  '
        cc=d

        a=cardpart1*len(self.player_list)
        b=cardpart2*len(self.player_list)
        d=cardpart4*len(self.player_list)
        aa=cardpart1*len(self.dealer_list)
        bb=cardpart2*len(self.dealer_list)
        dd=cardpart4*len(self.dealer_list)
        clear_output()
        print(" Dealer's Cards ")
        print(aa)
        print(bb)
        print(cc)
        print(dd)
        print('\n ')
        print(" Pleaer's Cards ")
        print(a)
        print(b)
        print(c)
        print(d)
        return (self.player_list,self.dealer_list)

    def player_round(self):
        cardpart1='._____.  '
        cardpart2='|     |  '
        cardpart3=f'| {"  "}♦ |  '
        cardpart4='|_____|  '
        from random import choice
        
        random_choice = choice(self.cards)
        self.player_list.append(random_choice)
        self.cards.remove(random_choice)

        
        p=''
        d=''
        for index,number in enumerate(self.player_list):
            if number in ['10♥','10♠','10♦','10♣']:
                p = p + f'| {self.player_list[index]} |  ' 
            else:
                p = p + f'|  {self.player_list[index]} |  '     
        
        c=p
        for index,number in enumerate(self.dealer_list):
            if number in ['10♥','10♠','10♦','10♣']:
                d = d + f'| {self.dealer_list[index]} |  ' 
            else:
                d = d + f'|  {self.dealer_list[index]} |  '
        cc=d

        a=cardpart1*len(self.player_list)
        b=cardpart2*len(self.player_list)
        d=cardpart4*len(self.player_list)
        aa=cardpart1*len(self.dealer_list)
        bb=cardpart2*len(self.dealer_list)
        dd=cardpart4*len(self.dealer_list)
        clear_output()
        print(" Dealer's Cards ")
        print(aa)
        print(bb)
        print(cc)
        print(dd)
        print('\n ')
        print(" Player's Cards ")
        print(a)
        print(b)
        print(c)
        print(d)
        return (self.player_list,self.dealer_list)

    def dealer_round(self):
        cardpart1='._____.  '
        cardpart2='|     |  '
        cardpart3=f'| {"  "}♦ |  '
        cardpart4='|_____|  '
        from random import choice       
        random_choice = choice(self.cards)
        self.dealer_list.append(random_choice)
        self.cards.remove(random_choice)

        
        p=''
        d=''
        for index,number in enumerate(self.player_list):
            if number in ['10♥','10♠','10♦','10♣']:
                p = p + f'| {self.player_list[index]} |  ' 
            else:
                p = p + f'|  {self.player_list[index]} |  '     
        
        c=p
        for i,n in enumerate(self.dealer_list):
            if i in ['10♥','10♠','10♦','10♣']:
                d = d + f'| {self.dealer_list[i]} |  ' 
            else:
                d = d + f'|  {self.dealer_list[i]} |  '
        cc=d

        a=cardpart1*len(self.player_list)
        b=cardpart2*len(self.player_list)
        d=cardpart4*len(self.player_list)
        aa=cardpart1*len(self.dealer_list)
        bb=cardpart2*len(self.dealer_list)
        dd=cardpart4*len(self.dealer_list)
        clear_output()
        print(" Dealer's Cards ")
        print(aa)
        print(bb)
        print(cc)
        print(dd)
        print('\n ')
        print(" Player's Cards ")
        print(a)
        print(b)
        print(c)
        print(d)
        return (self.player_list,self.dealer_list)

#-----------------------------------------------------------------------------
#the Sum() class will sum vlaues of player's card and dealer's cards :
class Sum():
    def __init__(self,player_list,dealer_list):
        self.player_list=player_list
        self.dealer_list=dealer_list

    #player_sum() will sum the values of player's cards, 
    # taking into account the rules for "A" card (1 or 11):
    def player_sum(self):
        p_sum=0   
        eleven=False
        for n,zft in enumerate(self.player_list):
            # dealing with the first appearance of the "A" card (1 or 11):
            if self.player_list[n][0]=='A'and (not eleven):
                if (p_sum + 11)<=21:
                    p_sum=p_sum+11
                    eleven=True
                else:
                     p_sum=p_sum+1
            # dealing with the second appearance of the "A" card (1 always):
            elif self.player_list[n][0]=='A':
                p_sum = p_sum + 1

            elif (self.player_list[n][0].isalpha()) or (self.player_list[n][0]=='1'):
                p_sum=p_sum+10

            else:
                p_sum=p_sum+int(self.player_list[n][0])

        if eleven==True and p_sum>21 :
            p_sum=p_sum - 10
        return p_sum

    #dealer_sum() will sum the values of dealer's cards, 
    # taking into account the rules for "A" card (1 or 11):
    def dealer_sum(self):
        d_sum=0   
        eleven1=False
        for n,zft in enumerate(self.dealer_list):
            # dealing with the first appearance of the "A" card:
            if self.dealer_list[n][0]=='A'and (not eleven1):
                if (d_sum + 11)<=21:
                    d_sum=d_sum+11
                    eleven1=True
                else:
                     d_sum=d_sum+1
            # dealing with the second appearance of the "A" card:
            elif self.dealer_list[n][0]=='A':
                d_sum = d_sum + 1

            elif (self.dealer_list[n][0].isalpha()) or (self.dealer_list[n][0]=='1'):
                d_sum=d_sum+10

            else:
                d_sum=d_sum+int(self.dealer_list[n][0])

        if eleven1==True and d_sum>21 :
            d_sum=d_sum - 10
        return d_sum


#__________________________________{Functions}______________________________

#This function asks the player to hit or stay:
def hit_stay():
    hit=''
    while hit!='hit' and hit!='stay':
        hit=input('hit or stay?: ')
    if hit=='hit':
        return 'hit'
    else:
        return 'stay'

#------------------------------------------------------------------------------
#this function will ask the player for a replay:
def replay():
    user=''
    while user!='y' and user!='n':
        user=input('replay? if yes please enter: y  if No please enter: n ')
    if user=='y':
        return True
    else:
        return False

#___________________________{Main program}______________________________________
import time
#creating an instance from the Money Class:
#asking for the players total balance 
BJ_money = Money()
player_money=BJ_money.player_money_ask()
# some initialization
rep=True
black_jack=0 

#{Main loop}
while rep:
    #game cards
    cards=['A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦','A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣','A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠']

    #creating an instance from Table() Class:
    BJ_table=Table(cards,player_list=[],dealer_list=[])
    
    #asking the player for the amount of bets he wants to pay in this turn:
    table_money=BJ_money.table_money_ask()
    
    
    # {Player's Turn}:
    #starting the game by one up face card for the dealer, 
    # and 2 up face cards for the player (the opening round):
    
    #printing the opening table:
    (player_list,dealer_list)=BJ_table.open_round()
    
    #creating an instance of the Sum() class, and add the value of player' card:
    BJ_sum=Sum(player_list,dealer_list)
    p_sum = BJ_sum.player_sum()
    
    #check for black jack case:
    if p_sum==21:
        black_jack=1
        print("stay by defult black jack case")

    #if there is no black Jack,the game continue by asking the player to hit or stay:
    #hit means new card for the player, stay means end of player's turn
    while not black_jack:
        #using hit_stay() function to ask for Hit Or Stay
        hit=hit_stay()
        if hit=='stay':
            break
        else:
            #after each hit, the value of player's cards will be added    
            (player_list,dealer_list)=BJ_table.player_round()
            p_sum = BJ_sum.player_sum()

    #{Dealer's Turn} :
    #The player will continue to obtain a card until,
    # his card total reaches 17 or more:
    cont=True
    while cont:
        #the delay is just for show:
        time.sleep(2)
        (player_list,dealer_list)=BJ_table.dealer_round()
        d_sum=BJ_sum.dealer_sum()
        if d_sum>= 17:
            cont=False

   # printing the results based on the blackJack rules:
   # using results() method from Money() class to modify the player's balance:
    print(f'Player score: {p_sum}')
    print(f'Dealer score: {d_sum}')           
    if(p_sum)>21:
        print('You lost')
        print('Going Bust')
        BJ_money.results('lost')
        print(f'Your Balance: {BJ_money.player_money}')
    elif (d_sum)>21:
        print('You Won')
        BJ_money.results('won')
        print(f'Your Balance: {BJ_money.player_money}')
    elif(p_sum==d_sum):
        print('Draw')
        print('Stand OFF')
        BJ_money.results('draw')
        print(f'Your Balance: {BJ_money.player_money}')
    elif black_jack==1:
        print('You Won Directly black Jack!')
        print("B")
        BJ_money.results('BJ')
        print(f'Your Balance: {BJ_money.player_money}')
    elif (p_sum>d_sum):
        print('You Won')
        BJ_money.results('won')
        print(f'Your Balance: {BJ_money.player_money}')
    elif p_sum<d_sum:
        print('You lost')
        BJ_money.results('lost')
        print(f'Your Balance: {BJ_money.player_money}')

#asking the player for replay using replay() function:
    if replay()==False:
        rep= False
    #reset
    black_jack=0