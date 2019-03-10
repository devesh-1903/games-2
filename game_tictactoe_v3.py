import time

def disp_board(box):

    print('\n      {box[7]}|{box[8]}|{box[9]}\n     -------\n      {box[4]}|{box[5]}|{box[6]}\n     -------\n      {box[1]}|{box[2]}|{box[3]}\n'.format(box=box))

def print_assigned():
    time.sleep(0.3)
    print('----------------------------------')
    print('Player1 assingned ',player1)
    print('Player2 assingned ',player2)
    print('----------------------------------')
    time.sleep(0.2)

def win_check(nl):
    row1 = nl[1:4]
    row2 = nl[4:7]
    row3 = nl[7:10]
    col1 = nl[1:8:3]
    col2 = nl[2:9:3]
    col3 = nl[3:10:3]
    dia1 = nl[3:8:2]
    dia2 = nl[1:10:4]
    boardlines = [row1,row2,row3,col1,col2,col3,dia1,dia2]
    #print(boardlines)
    for i in boardlines:
        #print(i)
        if ' ' not in i and len(set(i)) == 1 :
            print('\n****VICTORY****')
            return True
            break
        
        


########################################################################
# GAME ASSIGN PLAYERS
########################################################################
player1 = ''
player2 = ''

while True:  #### Replay loop
    print('\n'*3)
    while not (player1 == 'X' or player1 == 'O'):  #### PLAYER CHOOSING
        player1 = input("Pick a marker X or O: ").upper()
    if player1 == 'X': player2 = 'O'
    if player1 == 'O': player2 = 'X'
    print_assigned() ######## PRINT RESULTS

########################################################################
# GAME MODULE : INPUT CHECK
########################################################################

    victory = None   # holder for win_check()
    count = 1        # Player iteration 
    i = 1            # Move iteration
    nl = [' '] * 10  # NULL BOARD
    ul = []          # USED SPACES BOARD
    move = 0         # Holder for move input()

########################################################################
# GAME MODULE : COUNT LIST EDIT & CHECKING WINS
########################################################################
    
    disp_board(nl)  # Print NULL BOARD
    while i <= 9:
        print()
        while not (move in list(range(1,10)) and move not in ul):
            try:
                move = int(input('Pick NUM 1-9: '))
            except:continue

        if count == 1 :
            nl.pop(move)
            nl.insert(move, player1)
            ul.append(move)
            count = 2
            print('move #',i)
            i += 1
            disp_board(nl)
            victory = win_check(nl)
            if victory : break
            

        elif count == 2 :
            nl.pop(move)
            nl.insert(move, player2)
            ul.append(move)
            count = 1
            print('move #',i)
            i += 1
            disp_board(nl)
            victory = win_check(nl)
            if victory : break
            
    if not victory : print('\n****DRAW****')
            
    print('\nEND')
    


########################################################################
# REPLAY MODULE
########################################################################
    while True:
        again = ''
        while not (again.lower() == 'yes' or again.lower() == 'no'):  #### PLAYER CHOOSING
            again = input('\nPlay again? yes/no: ')
        if again == 'yes' :
            break
        else:
            print('Good bye')
            quit()

    continue
