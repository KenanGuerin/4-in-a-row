#This is what the board look like 

#	TOP
#F	0123456
#E	0123456
#D	0123456
#C	0123456
#B	0123456
#A	0123456
#	BOTTOM



A=['⠀','⠀','⠀','⠀','⠀','⠀','⠀']
B=['⠀','⠀','⠀','⠀','⠀','⠀','⠀']
C=['⠀','⠀','⠀','⠀','⠀','⠀','⠀']
D=['⠀','⠀','⠀','⠀','⠀','⠀','⠀']
E=['⠀','⠀','⠀','⠀','⠀','⠀','⠀']
F=['⠀','⠀','⠀','⠀','⠀','⠀','⠀']

row=[A,B,C,D,E,F]

player1='∎'
player2='∆'


def show():#print the board
	global A,B,C,D,E,F
	print(F)
	print(E)
	print(D)
	print(C)
	print(B)
	print(A)

def place(player): #ask and place the player piece (with gravity)
	global A,B,C,D,E,F
	col=int(input("Type a column 1-7 : "))-1
	if A[col]=='⠀':
		A[col]=player
	elif B[col]=='⠀':
		B[col]=player
	elif C[col]=='⠀':
		C[col]=player
	elif D[col]=='⠀':
		D[col]=player
	elif E[col]=='⠀':
		E[col]=player
	elif F[col]=='⠀':
		F[col]=player
	else:
		print("No more space in this colum")
		print("Type another one")
		place(player)
		

def debug_place(player,col): #like place but for debug
	global A,B,C,D,E,F
	col-=1
	if A[col]=='⠀':
		A[col]=player
	elif B[col]=='⠀':
		B[col]=player
	elif C[col]=='⠀':
		C[col]=player
	elif D[col]=='⠀':
		D[col]=player
	elif E[col]=='⠀':
		E[col]=player
	elif F[col]=='⠀':
		F[col]=player
	else:
		print("No more space in this colum")
		print("Type another one")
		place(player)

def iswincolumn(player):# check is there are any column win combination
	global row
	for rw in range(0,3):
		for i in range (0,7):
			if row[rw][i]==row[rw+1][i]==row[rw+2][i]==row[rw+3][i]==player:
				return True
	return False
	
def iswinrow(player):
	global row
	for rw in row:
		for i in range(0,4):
			if rw[i]==rw[i+1]==rw[i+2]==rw[i+3]==player:
				return True
	return False
	
def iswindiagonal1(player):
	global row
	for rw in range(0,3):
		for i in range(0,4):
			if row[rw][i]==row[rw+1][i+1]==row[rw+2][i+2]==row[rw+3][i+3]==player:
				return True
	return False

def iswindiagonal2(player):# erreur
	global row
	for rw in range(6,3):
		for i in range(7,4):
			print(row[rw][i])
			if row[rw][i]==row[rw-1][i-1]==row[rw-2][i-2]==row[rw-3][i-3]==player:
				return True
	return False
	
def iswindiagonal(player):
	if iswindiagonal1(player):
		return True
	elif iswindiagonal2(player):
		return True
	else:
		return False

def board_num():
	l=0
	for col in range(1,8):
		for i in range(0,6):
			l+=1
			debug_place(l,col)

board_num()
show()
#print(iswindiagonal2(player1))