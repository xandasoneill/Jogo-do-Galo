from random import *


class Player:
   def  __init__(self, symbol):
       self.symbol = symbol

class Board(dict):
    def __init__(self):
        super().__init__({
            'A1': None, 'A2': None, 'A3': None,
            'B1': None, 'B2': None, 'B3': None,
            'C1': None, 'C2': None, 'C3': None
        })

        
def cellss():
    list_of_cells =["A1", "B1", "C1", 
                    "A2", "B2", "C2",
                    "A3", "B3", "C3"]
    return list_of_cells
    
def is_cell_empty(jogada,board):
    return board[jogada] is None

def list_of_emmpty(board):
    cells=cellss()
    empty_cells = []
    for cell in cells:
        if is_cell_empty(cell, board):
            empty_cells.append(cell)
    return empty_cells

def cleanboard(board):
    list_of_cells = cellss()
    for cell in list_of_cells:
        board[cell] = None

def alterarboard(board, jogada, symbol):
    board[jogada] = symbol

def jogar(symbol, board):
        while True:
            print(f"É a tua vez {symbol}")
            col = input("Escolha entre A, B e C para coluna: ").upper()
            row = input("Escolha entre 1, 2, e 3 para linha: ")
    
            jogada = col + row
    
            if col in ['A', 'B', 'C'] and row.isdigit() and 1 <= int(row) < 4:
                if is_cell_empty(jogada, board):
                    alterarboard(board, jogada, symbol)
                else:
                    print("Essa célula já está ocupada! Escolha outra.")
            else:
                print("Jogada inválida. Tente novamente.")
        

def check_draw(board):
    empty_cells = list_of_emmpty(board)
    if check_winner(board) == None and empty_cells == []:
        return True

def check_winner(board):

    
    linhas = [["A1", "B1", "C1"], 
              ["A2", "B2", "C2"], 
              ["A3", "B3", "C3"]]

    colunas = [["A1", "A2", "A3"], 
               ["B1", "B2", "B3"], 
               ["C1", "C2", "C3"]]

    diagonais = [["A1", "B2", "C3"], 
                 ["A3", "B2", "C1"]]

    for linha in linhas + colunas + diagonais:
        valores = [board[cell] for cell in linha]
        if valores[0] is not None and valores.count(valores[0]) == 3:
            return valores[0]
    return None

def minimax(ai_player, human_player, is_maximizing, depth, board):
    if check_winner(board) == ai_player:
        return 1
    elif check_winner(board) == human_player:
        return -1
    elif check_draw(board):
        return 0
  
    empty_cells = list_of_emmpty(board)
  
    if is_maximizing:
        best_score = -float('inf')
        for cell in empty_cells:
            board[cell] = ai_player
            score = minimax(ai_player, human_player, False, depth + 1, board)
            board[cell] = None
            best_score = max(score, best_score)
        return best_score - depth
    else:
        best_score = float('inf')
        for cell in empty_cells: 
            board[cell] = human_player
            score = minimax(ai_player, human_player, True, depth + 1, board)
            board[cell] = None
            best_score = min(score, best_score)
        return best_score + depth

def ai_move_minimax(ai_player, human_player, board):
    best_score = -float('inf')
    best_move = None

    empty_cells = list_of_emmpty(board)
    #print(empty_cells)
    

    for cell in empty_cells:
        board[cell] = ai_player
        score = minimax(ai_player, 
                        human_player, 
                        False, 
                        0,
                        board)
        board[cell] = None
        if score > best_score:
            best_score = score
            best_move = cell
    board[best_move] = ai_player
    return best_move
    