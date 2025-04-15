from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence
from back import *
from random import *
global a1, a2, a3, b1, b2, b3, c1, c2, c3


root = Tk()

p1 = StringVar(value="")
p2 = StringVar(value="")
p = StringVar(value="")
number = IntVar(value=int(round(random(), 0)))
#print(number.get())
contra_o_galo = BooleanVar()


fundo_ficheiro = 'galo.gif'
fundo = Image.open(fundo_ficheiro)
fundotk = ImageTk.PhotoImage(fundo)


board_ficheiro = Image.open('board.jpg')
boardtk = ImageTk.PhotoImage(board_ficheiro)

galoescolha = Image.open('galo escolha.jpg')
galoescolha = galoescolha.resize((400, 300))
galoescolhatk = ImageTk.PhotoImage(galoescolha)

galovitorioso =  Image.open('galo vitorioso.jpg')
galovitoriosotk = ImageTk.PhotoImage(galovitorioso)

galoempatado = Image.open('galo empatado.jpg')
galoempatado = galoempatado.resize((500, 300))
galoempatadotk = ImageTk.PhotoImage(galoempatado)


frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(fundo)]

main_page = Frame(root, width=500, height=500)
main_page.grid()
main_page.grid_propagate(False)

label = Label(main_page, image = fundotk)
label.pack()
label.image = fundotk
label.frames = frames 

board = Board()

botao_jogar = Button(main_page,
                     text='Jogar!',
                     bg = 'red',
                     fg = 'white',
                     font=('Goudy Old Style',16, 'bold'),
                     relief='raised',
                     command=lambda: (boardescolha(),
                                      cleanboard(board)))
botao_jogar.place(x=200, y=300)

def remove_button(button):
    button.destroy()
    
def switch_windows(current_window, other_window):
    current_window.destroy()  
    other_window
    
def randompick(player1, player2):
    number = random()
    if number <= 0.5:
        player1.set('X')
        player2.set('O')
    else:
        player1.set('O')
        player2.set('X')
    return player1, player2

def updateplayersymbol(player, symbol1, symbol2, n):
    #print(n.get())
    if n.get()%2 == 0:
        player.set(symbol1.get())
    else:
        player.set(symbol2.get())
    
def updategif_galo(frame=0):
    frame %= len(frames)  # Loop the animation
    new_image = frames[frame]  # Get the current frame
    label.configure(image=new_image)  # Update label with new frame
    root.after(100, updategif_galo, frame + 1)

updategif_galo()


def boardescolha():
    boardescolha= Toplevel(root)
    boardescolha.title('')
    boardescolha.geometry('400x300')
    background = Label(boardescolha, image=galoescolhatk).place(x=0, y=0)
    Label(boardescolha, text='Escolhe', font=(40), fg='black').place(x=150, y=100)
    
    button_o = Button(boardescolha,
                      bg='white',
                      text='O',
                      font= (30),
                      command=lambda: (p1.set('O'), p2.set('X'), contra_o_galo.set(False), switch_windows(boardescolha, boardgame_())))
    button_o.place(x=100, y=150)
    
    button_x = Button(boardescolha,
                      bg='white',
                      text='X',
                      font= (30),
                      command=lambda:(p1.set('X'), p2.set('O'), contra_o_galo.set(False), switch_windows(boardescolha, boardgame_())))
    button_x.place(x=250, y=150)
    
    button_galo = Button(boardescolha,
                         bg= 'white',
                         text= 'ou queres jogar contra o GALO?',
                         font=(30),
                         command=lambda: (contra_o_galo.set(True), randompick(p1, p2), switch_windows(boardescolha, boardgame_()))                  
                         )
    button_galo.place(x=40, y=220)

def galo_jogar(player1, player2, player, board, a1, a2, a3, b1, b2, b3, c1, c2, c3, boardgame):
    to_button = {'A1': a1, 'A2': a2, 'A3': a3, 
                 'B1': b1, 'B2': b2, 'B3': b3, 
                 'C1': c1, 'C2': c2, 'C3': c3 }
    #print(player.get(), player1.get(), player2.get(), contra_o_galo.get())
    if contra_o_galo.get() and player.get() == player1.get():
        move = ai_move_minimax(player2.get(), player1.get(), board)
        if move and move in to_button:
            boardgame.after(200, to_button[move].invoke)

def winner(board, player, n, topwindow):
    if check_winner(board) == player:
        winnerpage_(topwindow)
        n.set(int(round(random(), 0)))
       # print(n.get())


def winnerpage_(topwindow):
    winnerpage = Toplevel(topwindow)
    winnerpage.geometry ('264x300')
    Label(winnerpage, image=galovitoriosotk).place(x=0, y=0)
    Label(winnerpage, text=f"Parabéns ganhaste {p.get()}", font=(20)).place(x=20, y=10)

def draw(board, n, topwindow):
    if check_draw(board):
        drawpage_(topwindow)
        n.set(int(round(random(), 0)))
        #print(n.get())
        
    
def drawpage_(topwindow):
    winnerpage = Toplevel(topwindow)
    winnerpage.geometry ('500x300')
    Label(winnerpage, image=galoempatadotk).place(x=0, y=0)
    Label(winnerpage, text='EMPATE', font=(20)).place(x=20, y=10)
    

def boardgame_():
    boardgame= Toplevel(root)
    boardgame.title('ATENÇAO Jogo do Galo!!! ATENÇAO')
    boardgame.geometry('400x300')
    labelboard=Label(boardgame, image=boardtk)
    labelboard.pack() 
    updateplayersymbol(p, p1, p2, number)
    #print(p.get(), p1.get(), p2.get())
    Label(boardgame,text=f"É a tua vez {p.get()}").place(x=0, y=0)

    
    
    a1 = Button(boardgame,
                bg='white',
                command=lambda: (remove_button(a1),
                                 Label(boardgame, 
                                       text= p.get(),
                                       font=('Arial', 20)).place(x=70, y=40),
                                 alterarboard(board, 'A1', p.get()),
                                 winner(board, p.get(), number, boardgame),
                                 draw(board, number, boardgame),
                                 number.set(number.get() + 1),
                                 updateplayersymbol(p, p1, p2, number),
                                 Label(boardgame,text=f"É a tua vez {p.get()}").place(x=0, y=0),
                                 galo_jogar(p1, p2, p, board, a1, a2, a3, b1, b2, b3, c1, c2, c3, boardgame)), 
                padx=30, 
                pady=20)
    a2 = Button(boardgame,
                bg='white',
                command=lambda: (remove_button(a2), 
                                 Label(boardgame, 
                                       text= p.get(),
                                       font=('Arial', 20)).place(x=70, y=100),
                                 alterarboard(board, 'A2', p.get()),
                                 winner(board, p.get(), number, boardgame),
                                 draw(board, number, boardgame),
                                 number.set(number.get() + 1),
                                 updateplayersymbol(p, p1, p2, number),
                                 Label(boardgame,text=f"É a tua vez {p.get()}").place(x=0, y=0),

                                 galo_jogar(p1, p2, p, board, a1, a2, a3, b1, b2, b3, c1, c2, c3, boardgame)), 
                padx=30, 
                pady=20)
    a3 = Button(boardgame,
                bg='white',
                command=lambda: (remove_button(a3), 
                                 Label(boardgame, 
                                       text= p.get(),
                                       font=('Arial', 20)).place(x=70, y=180),
                                 alterarboard(board, 'A3', p.get()),
                                 winner(board, p.get(), number, boardgame),
                                 draw(board, number, boardgame),
                                 number.set(number.get() + 1),
                                 updateplayersymbol(p, p1, p2, number),
                                 Label(boardgame,text=f"É a tua vez {p.get()}").place(x=0, y=0),

                                 galo_jogar(p1, p2, p, board, a1, a2, a3, b1, b2, b3, c1, c2, c3, boardgame)), 
                padx=30, 
                pady=20)
   
    b1 = Button(boardgame,
                bg='white',
                command=lambda: (remove_button(b1), 
                                 Label(boardgame, 
                                       text= p.get(),
                                       font=('Arial', 20)).place(x=180, y=40),
                                 alterarboard(board, 'B1', p.get()),
                                 winner(board, p.get(), number, boardgame),
                                 draw(board, number, boardgame),
                                 number.set(number.get() + 1),
                                 updateplayersymbol(p, p1, p2, number),
                                 Label(boardgame,text=f"É a tua vez {p.get()}").place(x=0, y=0),

                                 galo_jogar(p1, p2, p, board, a1, a2, a3, b1, b2, b3, c1, c2, c3, boardgame)), 
                padx=30, 
                pady=20)
    b2 = Button(boardgame,
                bg='white',
                command=lambda: (remove_button(b2), 
                                 Label(boardgame, 
                                       text= p.get(),
                                       font=('Arial', 20)).place(x=180, y=100),
                                 alterarboard(board, 'B2', p.get()),
                                 winner(board, p.get(), number, boardgame),
                                 draw(board, number, boardgame),
                                 number.set(number.get() + 1),
                                 updateplayersymbol(p, p1, p2, number),
                                 Label(boardgame,text=f"É a tua vez {p.get()}").place(x=0, y=0),

                                 galo_jogar(p1, p2, p, board, a1, a2, a3, b1, b2, b3, c1, c2, c3, boardgame)), 
                padx=30, 
                pady=20)
    b3 = Button(boardgame,
                bg='white',
                command=lambda: (remove_button(b3), 
                                 Label(boardgame, 
                                       text= p.get(),
                                       font=('Arial', 20)).place(x=180, y=180),
                                 alterarboard(board, 'B3', p.get()),
                                 winner(board, p.get(), number, boardgame),
                                 draw(board, number, boardgame),
                                 number.set(number.get() + 1),
                                 updateplayersymbol(p, p1, p2, number),
                                 Label(boardgame,text=f"É a tua vez {p.get()}").place(x=0, y=0),

                                 galo_jogar(p1, p2, p, board, a1, a2, a3, b1, b2, b3, c1, c2, c3, boardgame)), 
                padx=30, 
                pady=20)
    
    c1 = Button(boardgame,
                bg='white',
                command=lambda: (remove_button(c1), 
                                 Label(boardgame, 
                                       text= p.get(),
                                       font=('Arial', 20)).place(x=280, y=40),
                                 alterarboard(board, 'C1', p.get()),
                                 winner(board, p.get(), number, boardgame),
                                 draw(board, number, boardgame),
                                 number.set(number.get() + 1),
                                 updateplayersymbol(p, p1, p2, number),
                                 Label(boardgame,text=f"É a tua vez {p.get()}").place(x=0, y=0),

                                 galo_jogar(p1, p2, p, board, a1, a2, a3, b1, b2, b3, c1, c2, c3, boardgame)), 
                padx=30, 
                pady=20)
    c2 = Button(boardgame,
                bg='white',
                command=lambda: (remove_button(c2), 
                                 Label(boardgame, 
                                       text= p.get(),
                                       font=('Arial', 20)).place(x=280, y=100),
                                 alterarboard(board, 'C2', p.get()),
                                 winner(board, p.get(), number, boardgame),
                                 draw(board, number, boardgame),
                                 number.set(number.get() + 1),
                                 updateplayersymbol(p, p1, p2, number),
                                 Label(boardgame,text=f"É a tua vez {p.get()}").place(x=0, y=0),

                                 galo_jogar(p1, p2, p, board, a1, a2, a3, b1, b2, b3, c1, c2, c3, boardgame)), 
                padx=30, 
                pady=20)
    c3 = Button(boardgame,
                bg='white',
                command=lambda: (remove_button(c3), 
                                 Label(boardgame, 
                                       text= p.get(),
                                       font=('Arial', 20)).place(x=280, y=180),
                                 alterarboard(board, 'C3', p.get()),
                                 winner(board, p.get(), number, boardgame),
                                 draw(board, number, boardgame),
                                 number.set(number.get() + 1),
                                 updateplayersymbol(p, p1, p2, number),
                                 Label(boardgame,text=f"É a tua vez {p.get()}").place(x=0, y=0),

                                 galo_jogar(p1, p2, p, board, a1, a2, a3, b1, b2, b3, c1, c2, c3, boardgame)), 
                padx=30, 
                pady=20)
    a1.place(x=50, y=20)
    a2.place(x=50, y=100)
    a3.place(x=50, y=180)
    b1.place(x=150, y=20)
    b2.place(x=150, y=100)
    b3.place(x=150, y=180)
    c1.place(x=260, y=20)
    c2.place(x=260, y=100)
    c3.place(x=260, y=180)
    galo_jogar(p1, p2, p, board, a1, a2, a3, b1, b2, b3, c1, c2, c3, boardgame)
    
    return boardgame
root.mainloop()

