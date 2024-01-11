# Board Games - Checkers
# Dominic Whelan
# Jan.05, 2024
import none
import numpy as np
import pygame
import sys
import math


# Constants
ROW_COUNT = 8
COLUMN_COUNT = 8

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
RED = (255, 0, 0)
PINK = (255, 180, 180)
GREEN = (0, 255, 0)

PLAYER_1 = 1
PLAYER_2 = 2
SELECTED = 3

RED_PIECE_SETUP = [(0, 0), (0, 2), (0, 4), (0, 6),
                    (1, 1), (1, 3), (1, 5), (1, 7),
                    (2, 0), (2, 2), (2, 4), (2, 6)]

WHITE_PIECE_SETUP = [(5, 1), (5, 3), (5, 5), (5, 7),
                    (6, 0), (6, 2), (6, 4), (6, 6),
                    (7, 1), (7, 3), (7, 5), (7, 7)]


# Functions
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    for position in RED_PIECE_SETUP:
        board[position[0]][position[1]] = PLAYER_1
    for position in WHITE_PIECE_SETUP:
        board[position[0]][position[1]] = PLAYER_2
    return board


def selected_piece(board):
    pass


def valid_move(current_board, player, row_to_move, col_to_move, row_init, col_init):
    if player == PLAYER_1:
        if current_board[row_to_move][col_to_move] == 0:
            if row_init == row_to_move - 1:
                if col_init == col_to_move + 1 or col_init == col_to_move - 1:
                    return True
            elif row_init == row_to_move - 2:
                if col_init == col_to_move + 2:
                    if board[row_to_move - 1][col_to_move + 1] == PLAYER_2:
                        return True
                if col_init == col_to_move - 2:
                    if board[row_to_move - 1][col_to_move - 1] == PLAYER_2:
                        return True
    elif player == PLAYER_2:
        if current_board[row_to_move][col_to_move] == 0:
            if row_init == row_to_move + 1:
                if col_init == col_to_move + 1 or col_init == col_to_move - 1:
                    return True
            elif row_init == row_to_move + 2:
                if col_init == col_to_move + 2:
                    if board[row_to_move + 1][col_to_move + 1] == PLAYER_1:
                        return True
                if col_init == col_to_move - 2:
                    if board[row_to_move + 1][col_to_move - 1] == PLAYER_1:
                        return True
    else:
        return False


board = create_board()
print(np.flip(board, 0))
game_over = False
turn = 0
selection_made = False
selected_square = none

# GUI

pygame.init()
SQUARE_SIZE = 100
WIDTH = COLUMN_COUNT * SQUARE_SIZE
HEIGHT = ROW_COUNT * SQUARE_SIZE
SIZE = (WIDTH, HEIGHT)
RADIUS = int(SQUARE_SIZE / 2 - 8)


def draw_board(board):

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if r % 2 == 0 and c % 2 == 0 or r % 2 == 1 and c % 2 == 1:
                pygame.draw.rect(screen, BLACK,
                                 (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen, WHITE,
                                 (c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQUARE_SIZE + SQUARE_SIZE/2), int(r * SQUARE_SIZE + SQUARE_SIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, WHITE, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[r][c] == 3:
                pygame.draw.circle(screen, PINK, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[r][c] == 4:
                pygame.draw.circle(screen, GREY, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
        pygame.display.update()


screen = pygame.display.set_mode(SIZE)
draw_board(board)
pygame.display.update()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x_position = event.pos[0]
            y_position = event.pos[1]
            column = int(math.floor(x_position/SQUARE_SIZE))
            row = int(math.floor(y_position/SQUARE_SIZE))
            if turn == 0:
                if not selection_made:
                    if board[row][column] == PLAYER_1:
                        board[row][column] = 3
                        selected_square = (row, column)
                        selection_made = True
                        print(np.flip(board, 0))
                        pygame.display.update()
                        draw_board(board)
                else:
                    if valid_move(board, PLAYER_1, row, column, selected_square[0], selected_square[1]):
                        if selected_square[1] == column + 2:
                            board[selected_square[0] + 1][column + 1] = 0
                        elif selected_square[1] == column - 2:
                            board[selected_square[0] + 1][column - 1] = 0
                        board[row][column] = PLAYER_1
                        board[selected_square[0]][selected_square[1]] = 0
                        selection_made = False
                        print(np.flip(board, 0))
                        pygame.display.update()
                        draw_board(board)
                        turn += 1
                        turn = turn % 2

            else:
                if not selection_made:
                    if board[row][column] == PLAYER_2:
                        board[row][column] = 4
                        selected_square = (row, column)
                        selection_made = True
                        print(np.flip(board, 0))
                        pygame.display.update()
                        draw_board(board)
                else:
                    if valid_move(board, PLAYER_2, row, column, selected_square[0], selected_square[1]):
                        if selected_square[1] == column + 2:
                            board[selected_square[0] - 1][column + 1] = 0
                        elif selected_square[1] == column - 2:
                            board[selected_square[0] - 1][column - 1] = 0
                        board[row][column] = PLAYER_2
                        board[selected_square[0]][selected_square[1]] = 0
                        selection_made = False
                        print(np.flip(board, 0))
                        pygame.display.update()
                        draw_board(board)
                        turn += 1
                        turn = turn % 2

    if not 1 in board and not 3 in board:
        game_over = True
    elif not 2 in board and not 4 in board:
        game_over = True
# game_board = create_board()
# print(game_board)
