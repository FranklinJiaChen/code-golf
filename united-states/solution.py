import sys
for arg in sys.argv[1:]:
    s = ""
    for c in arg:
        if c.isupper() or c == 'z':
            s += c
    if arg[0:2] == 'Te':
        s += arg[2]
    if arg[0] in 'CVGHP' or 'Io' < arg < 'Mas':
        s += arg[-1]
    if arg == 'Alaska':
        s += arg[-2]
    if 'Mid' < arg < 'New' and arg != 'Nebraska':
        for i in arg[4::-1]:
            if 'i' < i:
                s += i
                break
    if len(s) < 2:
        s += arg[1]
    print(s.upper())