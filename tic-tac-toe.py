# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 09:18:41 2022

@author: abaker
"""

#a tic-tac-toe game using dictionary skills
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'tmid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ',}
def printBoard(board):
    print(board ['top-L'] + '|' + board['top-M'] + '|' + board ['top-R'])
    print('-+-+-')
    print(board ['mid-L'] + '|' + board['mid-M'] + '|' + board ['mid-R'])
    print('-+-+-')
    print(board ['low-L'] + '|' + board['low-M'] + '|' + board ['low-R'])
    printBoard(theBoard) 
    
    def game():
        turn = 'X'
        count = 0
        
        for i in range(9):
            #is this supposed to be range(10) ???
            printBoard(theBoard)
            print('Turn for ' + turn +' .Move on which space?')
            
            move = input()
            
            if theBoard[move] == ' ':
                theBoard[move] = turn
                if turn == 'X':
                    turn = 'O'
                else:
                    print("That place is already filled. \n Move to which place?")
                    continue
                
                #check if player X or O has won after 5 moves
                if count >= 5:
                   if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                       printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X' 
                    
            
    