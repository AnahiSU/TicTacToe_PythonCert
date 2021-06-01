import time #Para el contador (tiempo de mostrar el tablero en la consola)
import os
import random as r
board = [[1,2,3],[4,"X",6],[7,8,9]]
def DisplayBoard(board): #Creación del tablero y el arreglo
    print((("+"+"-"*7))*3+"+") 
    for a in range(3): 
      print(("|"+" "*7)*3+"|") 
      for i in range(3): 
        tab=board[a][i] 
        print(("|"+" "*3)+str(tab)+" "*3,end="") 
      print("|")  
      print(("|"+" "*7)*3+"|")  
      print((("+"+"-"*7))*3+"+") 

DisplayBoard(board) 
def EnterMove(board):
    movi =int(input("¿Dónde deseas poner la O?: "))
    for i in range(0,3): #Revisar en que fila se encuentra la variable
      if movi in board[i]:
        aux = True #Mouskerramienta misteriosa que servirá para más adelante
        fil = i   
    if aux == True: #Aquí mero se ve en que columna está
      tab = board[fil] #Dandole una variable pa que me deje trabajar
      col = tab.index(movi) #Viendo donde se encuentra el bendito numero 
      board[fil][col] = "O" #Super nice, aqui el numero ya estará reemplazado por O
    else:
      print("No manches, eso no es válido") #Revisar wtf 

    def clear(): #Limpiar consola en Linux y Windows
      if os.name == "nt":
        os.system("cls")
      else:
        os.system("clear")

    clear()  
    DisplayBoard(board)

def MachineMove(board):
  aux = False
  EnterMove(board)
  numeroR = r.randint(1,9)
  while aux == False:
    for b in range(3):
      if numeroR in board[b]:
        aux = True
        fil = b
  if aux == True:
    tab = board[fil]
    col = tab.index(numeroR)
    board[fil][col] = "X"
  def clear(): #Limpiar consola en Linux y Windows
      if os.name == "nt":
        os.system("cls")
      else:
        os.system("clear")
  clear()  
  DisplayBoard(board)
  EnterMove(board)

# checkBoard en proceso :,)
def checkBoard(board):
  aux = False
  while aux == False:
    for i in range(3):
      a = board[i][0]
      b = board[i][1]
      c = board[i][2]
      if a == "X":
        if a == b == c:
          print("Computer Wins!")
          aux = True
      elif a == "O":
        if a == b == c:
          print("You win!")
          aux = True  
    for c in range(3):
      a = board[0][c]
      b = board[1][c]
      c = board[2][c]
      if a == "X":
        print("Computer Wins!")
        aux = True
      elif a == "O":
        print("You win!")
        aux = True
        



#Invocar pruebas
MachineMove(board)
