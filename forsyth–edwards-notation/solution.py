p=print
import sys
for a in sys.argv[1:]:
	for c in a.split()[0]:
		try:p('♔♕♖♗♘♙♚♛♜♝♞♟'['KQRBNPkqrbnp'.index(c)],end='')
		except:
			try:p(' '*int(c),end='')
			except:p()
	p();p()