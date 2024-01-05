# Board Games
# Dominic Whelan
# Jan.05, 2024

import numpy as np
import pygame
import sys
import math


# Constants
ROW_COUNT = 8
COLUMN_COUNT = 8

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

PLAYER_1 = 1
PLAYER_2 = 2

RED_PIECE_SETUP = [(0, 0), (0, 2), (0, 4), (0, 6),
                    (1, 1), (1, 3), (1, 5), (1, 7),
                    (2, 0), (2, 2), (2, 4), (2, 6)]

BLACK_PIECE_SETUP = [(5, 1), (5, 3), (5, 5), (5, 7),
                    (6, 0), (6, 2), (6, 4), (6, 6),
                    (7, 1), (7, 3), (7, 5), (7, 7)]


# Functions
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    for position in RED_PIECE_SETUP:
        board[position[0]][position[1]] = PLAYER_1
    for position in BLACK_PIECE_SETUP:
        board[position[0]][position[1]] = PLAYER_2
    return board


def selected_peice(board):
    pass


def valid_move(board, player, selected_piece, position):
    pass



game_board = create_board()
print(game_board)
