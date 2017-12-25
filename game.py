DEBUG = False



import numpy as np
import os
import sys
import pygame

class GameBoard():
    r1 = "278146593"
    r2 = "531982647"
    r3 = "496735182"
    r4 = "653429718"
    r5 = "142678359"
    r6 = "987513264"
    r7 = "324851976"
    r8 = "819267435"
    r9 = "76539482 "
    '''
    r1 = "278   59 "
    r2 = "5  98   7"
    r3 = "  67     "
    r4 = "  34 97  "
    r5 = "14     59"
    r6 = "  75 32  "
    r7 = "     19  "
    r8 = "8   67  5"
    r9 = " 65   821"
    '''
    gameString = r1+r2+r3+r4+r5+r6+r7+r8+r9



    # These functions are sesponisble for initalizing a gameboard from a string

    def EmptyBoard(self):
        self.board = [[" "]*9]*9
        self.board = np.array(self.board)

    def Fill(self, string):
        if len(string) != (9*9):
            exit("Incorrect input string")
        else:
            for _ in range(len(string)):
                self.board[_/9][_%9] = string[_]

    def __init__(self):
        self.EmptyBoard()
        self.Fill(self.gameString)


    # These functions will be responsible for inserting a value and testing it

    def val_in_row(self, row, val):
        for _ in range(9):
            if self.board[row][_] == val:
                if DEBUG: print ( " row - col - val ", row, _, val)
                return True
        return False

    def val_in_col(self, col, val):
        for _ in range(9):
            if self.board[_][col] == val:
                if DEBUG: print ( " row - col - val ", _, col, val)
                return True
        return False

    def val_in_box(self, row, col, val):
        for i in range((row/3)*3, (row/3)*3 + 3):
            for j in range((col/3)*3, (col/3)*3 + 3):
                if self.board[i][j] == val:
                    if DEBUG: print ( " row - col - val ", row, col, val)
                    return True
        return False


    # Manage user input

    def InsertVal(self, val, row, col):
        # check row
        if self.val_in_row(row, val):
            print( "Invalid, value exists in this row already" )
            return False
        # check col
        if self.val_in_col(col, val):
            print( "Invalid, value exists in this col already" )
            return False
        # check box
        if self.val_in_box(row, col, val):
            print ( "Invali, value exists in this box already" )
            return False
        # acceptable entry
        self.board[row][col] = val
        return True

    def get_entry(self):
        # get row form user
        row = raw_input("Row: ")
        col = raw_input("Column: ")
        val = raw_input("Value : ")
        # check validity on board and enter
        self.InsertVal(val, int(row), int(col))



    def PrintBoard(self):
        string = ""
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                if (j+1)%3 == 0:
                    if (j+1) == 3 or (j+1) == 6: string += " " + str(self.board[i][j]) + " |"
                    elif (j+1) == 9: string += " " + str(self.board[i][j]) + "\n"
                else: string += " " + str(self.board[i][j])
            if i == 2 or i == 5: string += "-"*24 + "\n"
        print string


    # check if the game has been won
    def Check_For_Win(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == " ":
                    return False
        print("\n\n\n !!!!  YOU WIN  !!!! \n\n\n")
        exit()


    # Game play loop
    def Game_Loop(self):
        while(1):
            self.PrintBoard()
            self.get_entry()
            self.Check_For_Win()


# MAIN #

#G = GameBoard("123456789123456789123456789123456789123456789123456789123456789123456789123456789")

TheGame = GameBoard()
TheGame.Game_Loop()
