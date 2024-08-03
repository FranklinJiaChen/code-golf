import sys
p=print
for a in sys.argv[1:]:
	[p('♔♕♖♗♘♙♚♛♜♝♞♟'['KQRBNPkqrbnp'.find(c)]*c.isalpha()or'\n'*(c<'0')or' '*int(c),end='')for c in a.split()[0]]
	p();p()
