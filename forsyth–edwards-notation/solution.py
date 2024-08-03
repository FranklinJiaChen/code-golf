import sys
for a in sys.argv[1:]:print(''.join('♔♕♖♗♘♙♚♛♜♝♞♟'['KQRBNPkqrbnp'.find(c)]*c.isalpha()or'\n'*(c<'0')or' '*int(c)for c in a.split()[0])+'\n')