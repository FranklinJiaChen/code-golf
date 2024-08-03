p=print
import sys
for a in sys.argv[1:]:
	for r in a.split()[0].split('/'):
		for c in r:
			try:p('♔♕♖♗♘♙♚♛♜♝♞♟'['KQRBNPkqrbnp'.index(c)],end='')
			except:p(' '*int(c),end='')
		p()
	p()