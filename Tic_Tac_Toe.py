# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:26:13 2020

@author: Suraj Pandey
"""
import numpy as np

board = np.array([('','',''),('','','',),('','','')])

Play = True

#def display_board():
    #print(board)
     
#display_board()

def player_input():
    marker = ''
    while marker != 'X' or marker != 'O':
        input('Player1 choose your marker X or O: ').upper()
        if marker == 'X':
            return ('X', 'O')
            break 
        
        elif marker == 'O': 
            return('O','X')
            break
        else:
            print('Invalid Input!, Try Again')

#player_input()
       
def place_marker():
    board[i][j] = 15
    print(board)
#place_marker()
    
def win_check(board,mark):
    return( (board[0][0] == board[0][1]==board[0][2] == mark) or 
    (board[1][0] == board[1][1]==board[1][2] == mark) or
    (board[2][0] == board[2][1]==board[2][2] == mark) or
    (board[0][0] == board[1][0]==board[2][0] == mark) or
    (board[0][1] == board[1][1]==board[2][1] == mark) or
    (board[0][2] == board[1][2]==board[2][2] == mark) or
    (board[0][0] == board[1][1]==board[2][2] == mark) or
    (board[0][2] == board[1][1]==board[2][0] == mark))
    
  
#print(win_check(board,5))
    
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
    
def space_check(i,j):
    if board[i][j] == '':
        return True
    else:
        return False
    
#print(space_check(0,2))  
        
def full_board_check():
    for i in range(3):
        for j in range(3):
            if space_check(i,j):
                return False
            else:
                return True
#print(full_board_check())         
                
def player_choice():
    #marker1 = 'X'
    #marker2 = 'O'

        
    while Play:
        
        print('Enter your next move')
        i = int(input('Enter row: '))
        j= int(input('Enter column: '))
        if  i  in [0,1,2] and j in [0,1,2] and space_check(i,j):
            
            return i,j
            break
        else:
            print('Invalid Input, Please Try Again')
            
        
#player_choice()   
def replay():
    
    while True:
        rplay=input('Play again? Y/N  ')
        if rplay == 'Y':
            return True
            break
        elif rplay == 'N':
            return False
            break
        else:
            print("Invalid Input, Try Again")
        
#print(replay())   
def main():
    print('Welcome to Tic Tac Toe')

#Resetting the board
    while True:
        board = np.array([('','',''),('','',''),('','','')])
    
    #Player and their Marker
        Player1_marker,Player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first')
    
        play_game= input("Are you ready? Y/N ")
        if play_game == 'Y':
            game_on = True
        else:
            game_on = False
            
        while game_on:
        #Player1's Turn
            if turn == 'Player 1':
                print (board)
                row,column=player_choice()
                board[row][column] = Player1_marker
            
                if win_check(board,Player1_marker):
                    print (board)
                    print("Player 1 won the game")
                    game_on = False
                else :
                    if full_board_check():
                        print('Game ends at Tie')
                        print(board)
                        break
                    else:
                        turn = 'Player 2'
                
            elif turn == 'Player 2':
            #Player2's Turn
                print (board)
                row,column=player_choice()
                board[row][column] = Player2_marker
            
                if win_check(board,Player2_marker):
                    print (board)
                    print("Player 2 won the game")
                    game_on = False
                else:
                    if full_board_check():
                        print('Game ends at Tie')
                        print(board)
                        break
                    else:
                        turn = 'Player 1'
        if not replay():
            break
main()           

    

    
        
    

        

        
        

    
         
        
    
    
    
     