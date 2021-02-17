#__________________________________{Functions}_____________________________________
#asking the players if they want to play,ask agian for invalied:
def Play():
    answer=''
    while answer !='Yes' and answer !='No':
        answer = input('Do you want to play? Taype Yes or No : ')
        if answer !='Yes' and answer !='No':
            answer = input('Invalied input please type Yes or No: ')
    return(answer)

#------------------------------------------------------------------------
#this function takes a list of strings and print its content in X,O gameboard form:
#note that clear_output() works with .ipynb only. 
from IPython.display import clear_output
def print_function(s=[' ',' ',' ',' ',' ',' ',' ',' ',' ']):
    clear_output()
    print('._____________________________.')
    print('|         |         |         |')
    print(f'|    {s[(6)]}    |    {s[7]}    |    {s[8]}    |')
    print('|_________|_________|_________|')
    print('|         |         |         |')
    print(f'|    {s[(3)]}    |    {s[4]}    |    {s[5]}    |')
    print('|_________|_________|_________|')
    print('|         |         |         |')
    print(f'|    {s[(0)]}    |    {s[1]}    |    {s[2]}    |')
    print('|_________|_________|_________|')

#------------------------------------------------------------------------
#asking player1 X or O ? keep asking until receiving a valid entry: 
def choose_XO():
    player1=''
    while player1 !='X' and player1 !='O': 
        player1 = input('Player 1 ,choose X or O: ')
        while not (player1 in 'XO'):
            player1 = input('Invalied input please choose X or O: ')
    if player1=='X':
        player2 ='O'
    else:
        player2 = 'X'
    return(player1,player2)

#------------------------------------------------------------------------
#this function takes the player's choice,and prepare the input list to be printed: 
def choose_possition_convert(turn,player1,player2,input_list):
    possition=''
    lis=''
    input_nums=['1','2','3','4','5','6','7','8','9']
    #creating a list of the valid empty places, to compare it with the player's entry:
    for n,item in enumerate(input_list):
        if item==' ':
            lis=lis+str(n+1)+' '
    lis=lis.split()
    #asking the player to type a valid empty number:
    while (possition not in input_nums) or (possition not in lis) :
        possition = input('Please choose a number (1-9) with free space on the board: ')
    #put the valid input number in the correct place in the input list:
    possition=int(possition)
    index_posstion=possition-1
    for index,num in enumerate(input_list):
        if index == index_posstion:
            input_list[index]=possition
    #convert the input number in the input list to X or O based on the turn: 
    for i,number in enumerate(input_list):
        if type(number)==int and (turn%2==0):
            input_list[i]=player1
        elif type(number)==int and (turn%2 !=0):
            input_list[i]=player2
    return input_list

#------------------------------------------------------------------------
#this function checks for all the possible winning patterns for X and O 
def win_check(input_list):
    if input_list[0:3]==['X','X','X']:
        return True
    elif input_list[3:6]==['X','X','X']:
        return True
    elif input_list[6:9] ==['X','X','X']:
        return True
    elif input_list[0:7:3]==['X','X','X']:
        return True
    elif input_list[1:8:3]==['X','X','X']:
        return True
    elif input_list[2:9:3]==['X','X','X']:
        return True
    elif list(input_list[0]+input_list[4]+input_list[8])==['X','X','X']:
        return True
    elif list(input_list[2]+input_list[4]+input_list[6])==['X','X','X']:
        return True
    #-------------------------------------------------------------------------
    elif input_list[0:3]==['O','O','O']:
        return True
    elif input_list[3:6]==['O','O','O']:
        return True
    elif input_list[6:9] ==['O','O','O']:
        return True
    elif input_list[0:7:3]==['O','O','O']:
        return True
    elif input_list[1:8:3]==['O','O','O']:
        return True
    elif input_list[2:9:3]==['O','O','O']:
        return True
    elif list(input_list[0]+input_list[4]+input_list[8])==['O','O','O']:
        return True
    elif list(input_list[2]+input_list[4]+input_list[6])==['O','O','O']:
        return True
    else:
        return False

#------------------------------------------------------------------------

#__________________________________Main Program_____________________________________
play=True
while play:
    #initializing variables:
    turn=0
    win=False
    input_list=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    #asking the two players if they want to play, using Play() function:
    answer = Play()
    #depending on the Answer we continue..: 
    if answer =='No':
        print('Feel free to play again.')
        break
    #if the answer was 'Yes' the program continue:
    elif answer =='Yes':
        #printing an empty XO game Board usning print_function():
        print_function()
        #asking player1 one to choose X or O, the other choice will be saved to player2,
        #and this using choose_XO() function: 
        player1,player2=choose_XO()
        print(f"player1 {player1}")
        print(f'player2 {player2}')
        print("It's a new game")

        #----------------start playing ----------------------------------
        # (win) or (full board) will end the loop: 
        while(turn<=9 or not win):
            #choose_possition_convert() function will ask the player for a valid number,
            #convert it to X or O and place it in the right posstion of the input list:
            input_list=choose_possition_convert(turn,player1,player2,input_list)
            
            #print the updated input list using print_function(): 
            print_function(input_list)
        #------------------------------------------------------------------
            # check for a win pattern using win_check() function:
            win = win_check(input_list)
            
            #if win print the results, if no continue : 
            if (win==True) and (turn%2==0):
                print('congratulations player1 you won')
                turn=0
                break
            elif (win==True) and (turn%2!=0):
                print('congratulations player2 you won')
                turn=0
                break
            else:
                turn +=1
            #full board with no win means Tie:     
            if(turn==9):
                turn=0
                print('The result is Tie!')
                break