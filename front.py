from back import *
board = Board()

p1 = None

while p1 != 'O'and p1 != 'X':
    p1 = input('Escolhe o teu símbolo (O ou X)? ')
    p1 = p1.capitalize()
if p1 == 'O':
    p2 = 'X'
else:
    p2 = 'O'
player1 = Player(p1)
player2 = Player(p2)
for i in range(9):
        if i%2 == 0:        
            jogar(player1.symbol, board)
            if check_winner(board, True) == player1.symbol:
                print(f"Parabéns {player1.symbol} ganhaste!!")
                break
                
            
        else:
            ai_move_minimax(player2.symbol, player1.symbol, board)
            print(board)
            if check_winner(board, True) == player2.symbol:
                print(f"Parabéns {player2.symbol} ganhaste!!") 
                break



