p=print
import sys
for a in sys.argv[1:]:
	for c in a.split()[0]:
		if c<'0':p();continue
		try:p('♔♕♖♗♘♙♚♛♜♝♞♟'['KQRBNPkqrbnp'.index(c)],end='')
		except:p(' '*int(c),end='')
	p();p()