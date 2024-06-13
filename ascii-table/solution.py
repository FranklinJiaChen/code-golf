print('   2 3 4 5 6 7\n',"-"*13)
for i in range(16):
    print('0123456789ABCDEF'[i]+':',chr(32+i),chr(48+i),chr(64+i),chr(80+i),chr(96+i),[chr(112+i),'DEL'][i>14])