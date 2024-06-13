print('   2 3 4 5 6 7\n','-'*13)
for i in range(16):print(f'{i:X}: '+' '.join((chr(i+j*16),'DEL')[i+j>21]for j in range(2,8)))