import sys
p=print
for a in sys.argv[1:]:
	for c in a.split()[0]:
		p('♔♕♖♗♘♙♚♛♜♝♞♟'['KQRBNPkqrbnp'.find(c)]*c.isalpha()or'\n'*(c<'0')or' '*int(c),end='')
	p();p()