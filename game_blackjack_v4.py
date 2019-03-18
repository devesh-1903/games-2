import time
import random
from random import shuffle

#test

def ranks(): return ["2", "3", "4", "5", "6", "7","8", "9", "10", "J", "Q", "K", "A"]
def suits(): return ['♠', '♦', '♥', '♣']
def again():
    again = input('\n    Press anykey to continue/ Print "quit" elsewise: ')
    if again == 'quit' :
        print('    Good bye')
        quit()
    else: return True

class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + '' + self.suit

    def emptyhands():
        global used
        global flop_PC
        global flop_USER
        used=[]
        flop_PC=[]
        flop_USER=[]

    def pickrandom(player):
        x = 'start'
        while str(x) not in used or str(x) == 'start' :
            x = card_deck.randomcard()
            used.append(str(x))
            if player == 'PC':
                flop_PC.append(str(x))
            if player == 'USER' :
                flop_USER.append(str(x))
            break
        return str(x)

    def pointcheck(player):
        if player == 'PC': checklist = flop_PC
        if player == 'USER': checklist = flop_USER
        total = 0
        for i in checklist:
            if i[0] in ["2", "3", "4", "5", "6", "7","8", "9", "10"]:
                total += int(i[0])
            elif i[0] in ["J", "Q", "K"] or i[0:2] == "10":
                total += 10
            elif i[0] == "A":
                if total > 10: total += 1
                else : total += 11
        return total

    def image(rank_suit):
        cardlines = [[] for i in range(11)]
        if len(rank_suit) == 2:
            cardlines[0].append('  ╔══════════════╗')
            cardlines[1].append('  ║ {}           ║'.format(rank_suit))
            cardlines[2].append('  ║              ║')
            cardlines[3].append('  ║              ║')
            cardlines[4].append('  ║              ║')
            cardlines[5].append('  ║      {}      ║'.format(rank_suit))
            cardlines[6].append('  ║              ║')
            cardlines[7].append('  ║              ║')
            cardlines[8].append('  ║              ║')
            cardlines[9].append('  ║           {} ║'.format(rank_suit))
            cardlines[10].append('  ╚══════════════╝')
        elif len(rank_suit) == 3:
            cardlines[0].append('  ╔══════════════╗')
            cardlines[1].append('  ║ {}          ║'.format(rank_suit))
            cardlines[2].append('  ║              ║')
            cardlines[3].append('  ║              ║')
            cardlines[4].append('  ║              ║')
            cardlines[5].append('  ║      {}     ║'.format(rank_suit))
            cardlines[6].append('  ║              ║')
            cardlines[7].append('  ║              ║')
            cardlines[8].append('  ║              ║')
            cardlines[9].append('  ║           {}║'.format(rank_suit))
            cardlines[10].append('  ╚══════════════╝')
        return cardlines

    def mainscreen():
        top = [ [[''] for i in range(11)] for i in range(7) ]          ### made to hol MAX seven cards
        bottom = [ [[''] for i in range(11)] for i in range(7) ]

        count = 0
        for i in flop_PC:
            top[count]=Card.image(i)
            count+=1
        count = 0
        for i in flop_USER:
            bottom[count]=Card.image(i)
            count+=1

        time.sleep(0.5)
        print('\n'*100)

        i = 0
        print('\n   ~~~~~ PC ~~~~~')
        while i < 11:
            print(top[0][i][0],top[1][i][0],top[2][i][0],top[3][i][0],top[4][i][0],top[5][i][0],top[6][i][0])
            i += 1
        print('\n   >>>>> Total', Card.pointcheck('PC'),'points')
        print('\n')
        print('\n   ***** YOU *****')
        i = 0
        while i < 11:
            print(bottom[0][i][0],bottom[1][i][0],bottom[2][i][0],bottom[3][i][0],bottom[4][i][0],bottom[5][i][0],bottom[6][i][0])
            i += 1
        print('\n   >>>>> Total', Card.pointcheck('USER'),'points')

class Deck:
    def __init__(self):
        self.contents = []
        self.contents = [Card(rank,suit) for rank in ranks() for suit in suits()]

    def __str__(self):
        return 'deck of cards'

    def randomcard(self):
        random.shuffle(self.contents)
        return self.contents[0]

class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def __str__(self):
        return '{} Balance: {}$'.format(self.name, self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def pay2winner():
        while True:
            while uservictory == 'draw':
                time.sleep(0.8)
                print('   ~~~~~~~~~~~~~~~~~~~~~~~~~~~\n          NO ONE WINS')
                break
            while not uservictory:
                time.sleep(0.8)
                print('   ~~~~~~~~~~~~~~~~~~~~~~~~~~~\n          PC WINS')
                PC_account.deposit(bet)
                USER_account.withdraw(bet)
                break
            while uservictory and uservictory != 'draw':
                time.sleep(0.8)
                print('   ===========================\n          USER WINS')
                USER_account.deposit(bet)
                PC_account.withdraw(bet)
                break
            break
        time.sleep(0.3)
        return True

    def checkbalance():
        print()
        print('   ',USER_account)
        print('   ',PC_account)

        if PC_account.balance == 0 :
            print('   PC has 0 $\nThank you for playing')
            quit()
        if USER_account.balance == 0:
            print('    You have 0 $\n\n    Thank you for playing')
            quit()

    def takebet():
        global bet
        while True:

            try:
                bet = int(input('\n   Make your Bet $'))
            except:
                print('   Enter a number')
                continue

            if bet > USER_account.balance:
                print('   Not enough Credit\n   Your balance is: $',USER_account.balance)
                continue
            elif bet > PC_account.balance :
                print('   Sorry, not enough Credit for PC\n   PC balance is: $',PC_account.balance)
                continue
            elif bet <= USER_account.balance :
                print('   Bet',bet,'$ accepted')
                break

#*****************************************************************************************
#*****************************************************************************************
#*****************************************************************************************

while True:
    balance = input('\n   Please provide Deposit amount $: ')     # Deposit loop
    try:
        balance = int(balance)
        break
    except: print('   Enter a number')

print('   PC Deposits same amount : $',balance)
PC_account = Bank('PC', balance)
USER_account = Bank('USER', balance)

card_deck = Deck()

while True:
    while True:
        uservictory = True
        Bank.takebet()
        Card.emptyhands()

        Card.pickrandom('PC')              ## 4 card flop
        Card.pickrandom('PC')
        Card.pickrandom('USER')
        Card.pickrandom('USER')

        input('\n   Press any key to deal\n')
        time.sleep(0.2)
        Card.mainscreen()

        ###################################### PLAYER TURN

        while True:
            hit_or_stand = input('\n   press ENTER to hit, type S to STAND : ')
            print('   ===========================\n')
            if hit_or_stand.upper() == 'S':
                if Card.pointcheck('PC') > Card.pointcheck('USER'):   # if you stand while loosing in point
                    uservictory = False
                break

            if len(hit_or_stand) >= 0 :
                Card.pickrandom('USER')
                Card.mainscreen()
                if Card.pointcheck('USER') > 21:                      # if >21 BUST
                    print('\n     *** You are BUSTED ***')
                    uservictory = False
                    break
                if Card.pointcheck('USER') == 21:                     # if =21 do not ask to hit
                    print('\n     *** Wow, you are LUCKY ***')
                    break


        ###################################### COMPUTER TURN

        while uservictory:

            while Card.pointcheck('PC') <= Card.pointcheck('USER') :

                if Card.pointcheck('PC') == Card.pointcheck('USER') and Card.pointcheck('PC') > 17:
                    print('\n      ~~~ It is a DRAW ~~~')
                    uservictory = 'draw'
                    break

                print('   >>>>>>PC requests to Hit')
                Card.pickrandom('PC')

                if Card.pointcheck('PC') > 21:
                    Card.mainscreen()
                    print('\n      ~~~ PC is BUSTED ~~~')                   # if >21 PC BUST
                    uservictory = True
                    break
                if Card.pointcheck('PC') > Card.pointcheck('USER'):
                    Card.mainscreen()
                    print('\n      ~~~ PC got LUCKY ~~~')                   # if PC>USER
                    uservictory = False
                    break
            break
        ###################################### WIN / LOSE

        if Bank.pay2winner() : break        # adjusts balance according to Bet
    Bank.checkbalance()                     # prints new balance, quits if == 0
    if again() : continue                   # asks to play again
