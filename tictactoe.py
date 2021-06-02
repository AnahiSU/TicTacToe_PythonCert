import time as t #Para el contador (tiempo de mostrar el tablero en la consola)
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

def EnterMove(board):
    try:
      movi =int(input("\nWhat is your next move?: "))
      for i in range(0,3): #Revisar en que fila se encuentra la variable
        if movi in board[i]:
          aux = True #Mouskerramienta misteriosa que servirá para más adelante
          fil = i   
      if aux == True: #Aquí mero se ve en que columna está
        tab = board[fil] #Dandole una variable pa que me deje trabajar
        col = tab.index(movi) #Viendo donde se encuentra el bendito numero 
        board[fil][col] = "O" #Super nice, aqui el numero ya estará reemplazado por O
    except:
      print("\nInvalid move, you lost your turn :)") 
      t.sleep(2) 
    def clear(): #Limpiar consola en Linux y Windows
      if os.name == "nt":
        os.system("cls")
      else:
        os.system("clear")

    clear()  

def checklist(board):
  free = []
  for fil in range(0,3):
    for col in range (0,3):
      if board[fil][col] not in ["O","X"]:
        free.append((fil,col))
  return free 

def MachineMove(board):
  free = checklist(board)
  count = len(free)
  if count > 0:
    num = r.randrange(count)
    fil, col = free[num]
    board[fil][col] = 'X'
    print("\nComputer is thinking...")
    t.sleep(2)
  def clear(): #Limpiar consola en Linux y Windows
      if os.name == "nt":
        os.system("cls")
      else:
        os.system("clear")
  clear()  
     
  
# checkBoard en proceso :,)
def checkBoard(board, sgn):
	if sgn == "X":	#Buscar X
		who = "computer"	#X es de la maquina
	elif sgn == "O": #Buscar O
		who = "user"	#O es del usuario
	else:
		who = None 
	cross1 = cross2 = True  #para las diagonales
	for rc in range(3):
    #Filas
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
			return who
    #Columnas
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
			return who
    #Diagonales  
		if board[rc][rc] != sgn:
			cross1 = False
		if board[2 - rc][2 - rc] != sgn:
			cross2 = False
	if cross1 or cross2:
		return who
	return None


#Hora de la verdad :)    
free = checklist(board)
human = True
while len(free):
  DisplayBoard(board)
  if human:
    EnterMove(board)
    winner = checkBoard(board, "O")
    checklist(board)
    free = checklist(board)
  else:
    MachineMove(board)
    winner = checkBoard(board, "X")
    checklist(board)
    free = checklist(board)
  if winner == None and len(free) == 0:
    break
  elif winner != None:
    break
  human = not human 

DisplayBoard(board)
if checkBoard(board, "X") == "computer":
  print("\nI win!")
elif checkBoard(board, "O") == "user":
  print("\nYou win!")
else:
  print("\nIt's a draw. You're amazing! (guiño, guiño ;)")    






