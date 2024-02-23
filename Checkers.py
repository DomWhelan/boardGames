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
WHITE = (210, 210, 220)
GREY = (180, 180, 200)
RED = (200, 0, 0)
PINK = (255, 180, 180)
GREEN = (10, 100, 10)
YELLOW = (255, 255, 204)

BLANK_SQUARE = 0
PLAYER_1_TURN = 0
PLAYER_1 = 1
PLAYER_1_SELECTION = 3
PLAYER_1_KING = 5
PLAYER_1_KING_SELECTION = 7
PLAYER_2_TURN = 1
PLAYER_2 = 2
PLAYER_2_SELECTION = 4
PLAYER_2_KING = 6
PLAYER_2_KING_SELECTION = 8


RED_PIECE_SETUP = [(0, 0), (0, 2), (0, 4), (0, 6),
                   (1, 1), (1, 3), (1, 5), (1, 7),
                   (2, 0), (2, 2), (2, 4), (2, 6)]

WHITE_PIECE_SETUP = [(5, 1), (5, 3), (5, 5), (5, 7),
                     (6, 0), (6, 2), (6, 4), (6, 6),
                     (7, 1), (7, 3), (7, 5), (7, 7)]


# Functions
def create_board():
    new_board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    for position in RED_PIECE_SETUP:
        new_board[position[0]][position[1]] = PLAYER_1
    for position in WHITE_PIECE_SETUP:
        new_board[position[0]][position[1]] = PLAYER_2
    return new_board


def is_opposing_player(player_1, player_2):
    if player_1 == PLAYER_1 or player_1 == PLAYER_1_KING:
        if player_2 == PLAYER_2 or player_2 == PLAYER_2_KING:
            return True
        else:
            return False
    else:
        if player_2 == PLAYER_1 or player_2 == PLAYER_1_KING:
            return True
        else:
            return False


def valid_move(current_board, player, row_to_move, col_to_move, row_init, col_init):
    if player == PLAYER_1 or player == PLAYER_1_KING or player == PLAYER_2_KING:
        if current_board[row_to_move][col_to_move] == BLANK_SQUARE:
            if row_init == row_to_move - 1:
                if col_init == col_to_move + 1 or col_init == col_to_move - 1:
                    return True
            elif row_init == row_to_move - 2:
                if col_init == col_to_move + 2:
                    if is_opposing_player(player, board[row_to_move - 1][col_to_move + 1]):
                        # if board[row_to_move - 1][col_to_move + 1] == PLAYER_2:       *** DELETE IF NO ISSUES ***
                        return True
                if col_init == col_to_move - 2:
                    if is_opposing_player(player, board[row_to_move - 1][col_to_move - 1]):
                        # if board[row_to_move - 1][col_to_move - 1] == PLAYER_2:       *** DELETE IF NO ISSUES ***
                        return True
            elif row_init == row_to_move - 4:
                if col_init == col_to_move + 4:
                    # if (board[row_to_move - 1][col_to_move + 1] == PLAYER_2 and
                    if (is_opposing_player(player, board[row_to_move - 1][col_to_move + 1]) and
                            valid_move(current_board, player, row_to_move, col_to_move, (row_to_move - 2),
                                       (col_to_move + 2))):
                        return True
                if col_init == col_to_move - 4:
                    # if (board[row_to_move - 1][col_to_move - 1] == PLAYER_2 and
                    if (is_opposing_player(player, board[row_to_move - 1][col_to_move - 1]) and
                            valid_move(current_board, player, row_to_move, col_to_move, (row_to_move - 2),
                                       (col_to_move - 2))):
                        return True
                if col_init == col_to_move:
                    # if (board[row_to_move - 1][col_to_move + 1] == PLAYER_2 and
                    if (is_opposing_player(player, board[row_to_move - 1][col_to_move + 1]) and
                            valid_move(current_board, player, (row_to_move - 2), (col_to_move + 2),
                                       row_init, col_init)):
                        return True
                    # if (board[row_to_move - 1][col_to_move - 1] == PLAYER_2 and
                    if (is_opposing_player(player, board[row_to_move - 1][col_to_move - 1]) and
                            valid_move(current_board, player, (row_to_move - 2), (col_to_move - 2),
                                       row_init, col_init)):
                        return True

    if player == PLAYER_2 or player == PLAYER_1_KING or player == PLAYER_2_KING:
        if current_board[row_to_move][col_to_move] == BLANK_SQUARE:
            if row_init == row_to_move + 1:
                if col_init == col_to_move + 1 or col_init == col_to_move - 1:
                    return True
            elif row_init == row_to_move + 2:
                if col_init == col_to_move + 2:
                    # if board[row_to_move + 1][col_to_move + 1] == PLAYER_1:
                    if is_opposing_player(player, board[row_to_move + 1][col_to_move + 1]):
                        return True
                if col_init == col_to_move - 2:
                    # if board[row_to_move + 1][col_to_move - 1] == PLAYER_1:
                    if is_opposing_player(player, board[row_to_move + 1][col_to_move - 1]):
                        return True
            elif row_init == row_to_move + 4:
                if col_init == col_to_move + 4:
                    if (is_opposing_player(player, board[row_to_move + 1][col_to_move + 1]) and
                            valid_move(current_board, player, row_to_move, col_to_move, (row_to_move + 2),
                                       (col_to_move + 2))):
                        return True
                if col_init == col_to_move - 4:
                    if (is_opposing_player(player, board[row_to_move + 1][col_to_move - 1]) and
                            valid_move(current_board, player, row_to_move, col_to_move, (row_to_move + 2),
                                       (col_to_move - 2))):
                        return True
                if col_init == col_to_move:
                    if col_init <= 5:
                        if (is_opposing_player(player, board[row_to_move + 1][col_to_move + 1]) and
                            valid_move(current_board, player, (row_to_move + 2), (col_to_move + 2),
                                       row_init, col_init)):
                            return True
                    if col_init >= 2:
                        if (is_opposing_player(player, board[row_to_move + 1][col_to_move - 1]) and
                                valid_move(current_board, player, (row_to_move + 2), (col_to_move - 2),
                                           row_init, col_init) and col_init >= 2):
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
########################################################################################################################
pygame.init()

# display Constants
SQUARE_SIZE = 80
WIDTH = COLUMN_COUNT * SQUARE_SIZE
HEIGHT = ROW_COUNT * SQUARE_SIZE
SCREEN_MARGIN = 160
SIZE = ((WIDTH + SCREEN_MARGIN*2), (HEIGHT + SCREEN_MARGIN))
RADIUS = int(SQUARE_SIZE / 2 - 8)
message_1 = "PLAYER 1 GO"
message_2 = "PLAYER 2 GO"
message_3 = "PLAYER 1 WINS"
message_4 = "PLAYER 2 WINS"


def draw_board(current_board, message):
    my_font = pygame.font.SysFont("monospace", 75)
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if r % 2 == 0 and c % 2 == 0 or r % 2 == 1 and c % 2 == 1:
                pygame.draw.rect(screen, BLACK,
                                 (c * SQUARE_SIZE + SCREEN_MARGIN, r * SQUARE_SIZE + SCREEN_MARGIN / 2,
                                  SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen, WHITE,
                                 (c * SQUARE_SIZE + SCREEN_MARGIN, r * SQUARE_SIZE + SCREEN_MARGIN / 2,
                                  SQUARE_SIZE, SQUARE_SIZE))

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            x_center = int(c * SQUARE_SIZE + SCREEN_MARGIN + SQUARE_SIZE / 2)
            y_center = int(r * SQUARE_SIZE + SCREEN_MARGIN / 2 + SQUARE_SIZE / 2)
            king_points = [(x_center - 10, y_center - 10),
                           (x_center - 5, y_center - 3),
                           (x_center, y_center - 10),
                           (x_center + 5, y_center - 3),
                           (x_center + 10, y_center - 10),
                           (x_center + 10, y_center + 10),
                           (x_center - 10, y_center + 10)]
            if current_board[r][c] == PLAYER_1 or current_board[r][c] == PLAYER_1_KING:
                pygame.draw.circle(screen, RED, (x_center, y_center), RADIUS)
                if current_board[r][c] == PLAYER_1_KING:
                    pygame.draw.polygon(screen, YELLOW, king_points)
            elif current_board[r][c] == PLAYER_2 or current_board[r][c] == PLAYER_2_KING:
                pygame.draw.circle(screen, WHITE, (x_center, y_center), RADIUS)
                if current_board[r][c] == PLAYER_2_KING:
                    pygame.draw.polygon(screen, YELLOW, king_points)
            elif current_board[r][c] == PLAYER_1_SELECTION or current_board[r][c] == PLAYER_1_KING_SELECTION:
                pygame.draw.circle(screen, PINK, (x_center, y_center), RADIUS)
                if current_board[r][c] == PLAYER_1_KING_SELECTION:
                    pygame.draw.polygon(screen, YELLOW, king_points)
            elif current_board[r][c] == PLAYER_2_SELECTION or current_board[r][c] == PLAYER_2_KING_SELECTION:
                pygame.draw.circle(screen, GREY, (x_center, y_center), RADIUS)
                if current_board[r][c] == PLAYER_2_KING_SELECTION:
                    pygame.draw.polygon(screen, YELLOW, king_points)

        pygame.display.update()

    pygame.draw.rect(screen, GREEN, (0, 0, WIDTH + SCREEN_MARGIN, SCREEN_MARGIN / 2))
    pygame.draw.rect(screen, GREEN, (0, HEIGHT + SCREEN_MARGIN/2, WIDTH + SCREEN_MARGIN, SCREEN_MARGIN / 2))
    if message == message_1 or message == message_3:
        label = my_font.render(message, 1, RED)
        screen.blit(label, (200, 0))
    else:
        label = my_font.render(message, 1, WHITE)
        screen.blit(label, (160, HEIGHT + SCREEN_MARGIN/2))


# def display_message(message, color):
#     label = my_font.render(message, 1, color)
#     screen.blit(label, (40, 10))


screen = pygame.display.set_mode(SIZE)
screen.fill(GREEN)
draw_board(board, message_1)
pygame.display.update()
# my_font = pygame.font.SysFont("monospace", 75)


while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x_position = event.pos[0]
            y_position = event.pos[1]
            column = int(math.floor((x_position - SCREEN_MARGIN) / SQUARE_SIZE))
            row = int(math.floor((y_position - SCREEN_MARGIN / 2) / SQUARE_SIZE))
            if turn == PLAYER_1_TURN:
                if not selection_made:
                    if board[row][column] == PLAYER_1 or board[row][column] == PLAYER_1_KING:
                        if board[row][column] == PLAYER_1:
                            board[row][column] = PLAYER_1_SELECTION
                        else:
                            board[row][column] = PLAYER_1_KING_SELECTION
                        selected_square = (row, column)
                        selection_made = True
                        print(np.flip(board, 0))
                        pygame.display.update()
                        draw_board(board, message_1)
                else:
                    if board[row][column] == PLAYER_1 or board[row][column] == PLAYER_1_KING:
                        if board[row][column] == PLAYER_1:
                            if board[selected_square[0], selected_square[1]] == PLAYER_1_KING_SELECTION:
                                board[selected_square[0], selected_square[1]] = PLAYER_1_KING
                            else:
                                board[selected_square[0], selected_square[1]] = PLAYER_1
                            board[row][column] = PLAYER_1_SELECTION
                        else:
                            if board[selected_square[0], selected_square[1]] == PLAYER_1_KING_SELECTION:
                                board[selected_square[0], selected_square[1]] = PLAYER_1_KING
                            else:
                                board[selected_square[0], selected_square[1]] = PLAYER_1
                            board[row][column] = PLAYER_1_KING_SELECTION
                        selected_square = (row, column)
                        selection_made = True
                        print(np.flip(board, 0))
                        pygame.display.update()
                        draw_board(board, message_1)
                    elif valid_move(board, PLAYER_1, row, column, selected_square[0], selected_square[1]):
                        if selected_square[1] == column + 2 or selected_square[1] == column + 4:
                            board[selected_square[0] + 1][selected_square[1] - 1] = BLANK_SQUARE
                            if selected_square[1] == column + 4:
                                board[selected_square[0] + 3][selected_square[1] - 3] = BLANK_SQUARE
                        elif selected_square[1] == column - 2 or selected_square[1] == column - 4:
                            board[selected_square[0] + 1][selected_square[1] + 1] = BLANK_SQUARE
                            if selected_square[1] == column - 4:
                                board[selected_square[0] + 3][selected_square[1] + 3] = BLANK_SQUARE
                        elif selected_square[1] == column:
                            if (is_opposing_player(PLAYER_1, board[selected_square[0] + 1][selected_square[1] + 1]) and
                                    board[selected_square[0] + 2][selected_square[1] + 2] == BLANK_SQUARE and
                                    is_opposing_player(PLAYER_1,
                                                       board[selected_square[0] + 3][selected_square[1] + 1])):
                                board[selected_square[0] + 1][selected_square[1] + 1] = BLANK_SQUARE
                                board[selected_square[0] + 3][selected_square[1] + 1] = BLANK_SQUARE
                            elif (is_opposing_player(PLAYER_1,
                                                     board[selected_square[0] + 1][selected_square[1] - 1]) and
                                  board[selected_square[0] + 2][selected_square[1] - 2] == BLANK_SQUARE and
                                  is_opposing_player(PLAYER_1, board[selected_square[0] + 3][selected_square[1] - 1])):
                                board[selected_square[0] + 1][selected_square[1] - 1] = BLANK_SQUARE
                                board[selected_square[0] + 3][selected_square[1] - 1] = BLANK_SQUARE
                        if board[selected_square[0]][selected_square[1]] == PLAYER_1_SELECTION:
                            if row == 7:
                                board[row][column] = PLAYER_1_KING
                            else:
                                board[row][column] = PLAYER_1
                        else:
                            board[row][column] = PLAYER_1_KING
                        board[selected_square[0]][selected_square[1]] = BLANK_SQUARE
                        selection_made = False
                        print(np.flip(board, 0))
                        draw_board(board, message_2)
                        pygame.display.update()
                        turn += 1
                        turn = turn % 2
                    elif (board[selected_square[0]][selected_square[1]] == PLAYER_1_KING_SELECTION and
                          valid_move(board, PLAYER_1_KING, row, column, selected_square[0], selected_square[1])):
                        if selected_square[1] == column + 2 or selected_square[1] == column + 4:
                            board[selected_square[0] - 1][selected_square[1] - 1] = BLANK_SQUARE
                            if selected_square[1] == column + 4:
                                board[selected_square[0] - 3][selected_square[1] - 3] = BLANK_SQUARE
                        elif selected_square[1] == column - 2 or selected_square[1] == column - 4:
                            board[selected_square[0] - 1][selected_square[1] + 1] = BLANK_SQUARE
                            if selected_square[1] == column - 4:
                                board[selected_square[0] - 3][selected_square[1] + 3] = BLANK_SQUARE
                        elif selected_square[1] == column:
                            if (is_opposing_player(PLAYER_1, board[selected_square[0] - 1][selected_square[1] + 1]) and
                                    board[selected_square[0] - 2][selected_square[1] + 2] == BLANK_SQUARE and
                                    is_opposing_player(PLAYER_1,
                                                       board[selected_square[0] - 3][selected_square[1] + 1])):
                                board[selected_square[0] - 1][selected_square[1] + 1] = BLANK_SQUARE
                                board[selected_square[0] - 3][selected_square[1] + 1] = BLANK_SQUARE
                            elif (is_opposing_player(PLAYER_1,
                                                     board[selected_square[0] - 1][selected_square[1] - 1]) and
                                  board[selected_square[0] - 2][selected_square[1] - 2] == BLANK_SQUARE and
                                  is_opposing_player(PLAYER_1, board[selected_square[0] - 3][selected_square[1] - 1])):
                                board[selected_square[0] - 1][selected_square[1] - 1] = BLANK_SQUARE
                                board[selected_square[0] - 3][selected_square[1] - 1] = BLANK_SQUARE
                        board[row][column] = PLAYER_1_KING
                        board[selected_square[0]][selected_square[1]] = BLANK_SQUARE
                        selection_made = False
                        print(np.flip(board, 0))
                        draw_board(board, message_2)
                        pygame.display.update()
                        turn += 1
                        turn = turn % 2

            else:
                if not selection_made:
                    if board[row][column] == PLAYER_2 or board[row][column] == PLAYER_2_KING:
                        if board[row][column] == PLAYER_2:
                            board[row][column] = PLAYER_2_SELECTION
                        else:
                            board[row][column] = PLAYER_2_KING_SELECTION
                        selected_square = (row, column)
                        selection_made = True
                        print(np.flip(board, 0))
                        draw_board(board, message_2)
                        pygame.display.update()
                else:
                    if board[row][column] == PLAYER_2 or board[row][column] == PLAYER_2_KING:
                        if board[row][column] == PLAYER_2:
                            if board[selected_square[0], selected_square[1]] == PLAYER_2_KING_SELECTION:
                                board[selected_square[0], selected_square[1]] = PLAYER_2_KING
                            else:
                                board[selected_square[0], selected_square[1]] = PLAYER_2
                            board[row][column] = PLAYER_2_SELECTION
                        else:
                            if board[selected_square[0], selected_square[1]] == PLAYER_2_KING_SELECTION:
                                board[selected_square[0], selected_square[1]] = PLAYER_2_KING
                            else:
                                board[selected_square[0], selected_square[1]] = PLAYER_2
                            board[row][column] = PLAYER_2_KING_SELECTION
                        selected_square = (row, column)
                        selection_made = True
                        print(np.flip(board, 0))
                        draw_board(board, message_2)
                        pygame.display.update()
                    elif valid_move(board, PLAYER_2, row, column, selected_square[0], selected_square[1]):
                        if selected_square[1] == column + 2 or selected_square[1] == column + 4:
                            board[selected_square[0] - 1][selected_square[1] - 1] = BLANK_SQUARE
                            if selected_square[1] == column + 4:
                                board[selected_square[0] - 3][selected_square[1] - 3] = BLANK_SQUARE
                        elif selected_square[1] == column - 2 or selected_square[1] == column - 4:
                            board[selected_square[0] - 1][selected_square[1] + 1] = BLANK_SQUARE
                            if selected_square[1] == column - 4:
                                board[selected_square[0] - 3][selected_square[1] + 3] = BLANK_SQUARE
                        elif selected_square[1] == column:
                            if (is_opposing_player(PLAYER_2, board[selected_square[0] - 1][selected_square[1] + 1]) and
                                    board[selected_square[0] - 2][selected_square[1] + 2] == BLANK_SQUARE and
                                    is_opposing_player(PLAYER_2,
                                                       board[selected_square[0] - 3][selected_square[1] + 1])):
                                board[selected_square[0] - 1][selected_square[1] + 1] = BLANK_SQUARE
                                board[selected_square[0] - 3][selected_square[1] + 1] = BLANK_SQUARE
                            elif (is_opposing_player(PLAYER_2,
                                                     board[selected_square[0] - 1][selected_square[1] - 1]) and
                                  board[selected_square[0] - 2][selected_square[1] - 2] == BLANK_SQUARE and
                                  is_opposing_player(PLAYER_2, board[selected_square[0] - 3][selected_square[1] - 1])):
                                board[selected_square[0] - 1][selected_square[1] - 1] = BLANK_SQUARE
                                board[selected_square[0] - 3][selected_square[1] - 1] = BLANK_SQUARE
                        if board[selected_square[0]][selected_square[1]] == PLAYER_2_SELECTION:
                            if row == 0:
                                board[row][column] = PLAYER_2_KING
                            else:
                                board[row][column] = PLAYER_2
                        else:
                            board[row][column] = PLAYER_2_KING
                        board[selected_square[0]][selected_square[1]] = BLANK_SQUARE
                        selection_made = False
                        print(np.flip(board, 0))
                        draw_board(board, message_1)
                        pygame.display.update()
                        turn += 1
                        turn = turn % 2
                    elif (board[selected_square[0]][selected_square[1]] == PLAYER_2_KING_SELECTION and
                          valid_move(board, PLAYER_2_KING, row, column, selected_square[0], selected_square[1])):
                        if selected_square[1] == column + 2 or selected_square[1] == column + 4:
                            board[selected_square[0] + 1][selected_square[1] - 1] = BLANK_SQUARE
                            if selected_square[1] == column + 4:
                                board[selected_square[0] + 3][selected_square[1] - 3] = BLANK_SQUARE
                        elif selected_square[1] == column - 2 or selected_square[1] == column - 4:
                            board[selected_square[0] + 1][selected_square[1] + 1] = BLANK_SQUARE
                            if selected_square[1] == column - 4:
                                board[selected_square[0] + 3][selected_square[1] + 3] = BLANK_SQUARE
                        elif selected_square[1] == column:
                            if (is_opposing_player(PLAYER_2, board[selected_square[0] + 1][selected_square[1] + 1]) and
                                    board[selected_square[0] + 2][selected_square[1] + 2] == BLANK_SQUARE and
                                    is_opposing_player(PLAYER_2,
                                                       board[selected_square[0] + 3][selected_square[1] + 1])):
                                board[selected_square[0] + 1][selected_square[1] + 1] = BLANK_SQUARE
                                board[selected_square[0] + 3][selected_square[1] + 1] = BLANK_SQUARE
                            elif (is_opposing_player(PLAYER_2,
                                                     board[selected_square[0] + 1][selected_square[1] - 1]) and
                                  board[selected_square[0] + 2][selected_square[1] - 2] == BLANK_SQUARE and
                                  is_opposing_player(PLAYER_2, board[selected_square[0] + 3][selected_square[1] - 1])):
                                board[selected_square[0] + 1][selected_square[1] - 1] = BLANK_SQUARE
                                board[selected_square[0] + 3][selected_square[1] - 1] = BLANK_SQUARE
                        board[row][column] = PLAYER_2_KING
                        board[selected_square[0]][selected_square[1]] = BLANK_SQUARE
                        selection_made = False
                        print(np.flip(board, 0))
                        draw_board(board, message_1)
                        pygame.display.update()
                        turn += 1
                        turn = turn % 2

    if (PLAYER_1 not in board and PLAYER_1_KING not in board and PLAYER_1_SELECTION not in board and
            PLAYER_1_KING_SELECTION not in board):
        draw_board(board, message_4)
        pygame.display.update()
        pygame.time.wait(3000)
        game_over = True
    elif (PLAYER_2 not in board and PLAYER_2_KING not in board and PLAYER_2_SELECTION not in board and
          PLAYER_2_KING_SELECTION not in board):
        draw_board(board, message_3)
        pygame.display.update()
        pygame.time.wait(3000)
        game_over = True
# game_board = create_board()
# print(game_board)
