import sys
for a in sys.argv[1:]:
	for row in a.split()[0].split('/'):
		for cell in row:
			try:print('♔♕♖♗♘♙♚♛♜♝♞♟'['KQRBNPkqrbnp'.index(cell)],end='')
			except:print(' '*int(cell),end='')
		print()
	print()