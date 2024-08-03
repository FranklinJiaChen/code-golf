p=print
import sys
for a in sys.argv[1:]:
	for row in a.split()[0].split('/'):
		for cell in row:
			try:p('♔♕♖♗♘♙♚♛♜♝♞♟'['KQRBNPkqrbnp'.index(cell)],end='')
			except:p(' '*int(cell),end='')
		p()
	p()