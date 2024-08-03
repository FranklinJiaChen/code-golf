import sys
for a in sys.argv[1:]:
	for row in a.split()[0].split('/'):
		for cell in row:
			if cell.isdigit():print(' '*int(cell),end='')
			else:print('♔♕♖♗♘♙♚♛♜♝♞♟'['KQRBNPkqrbnp'.index(cell)],end='')
		print()
	print()