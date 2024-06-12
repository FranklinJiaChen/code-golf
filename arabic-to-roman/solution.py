import sys
for z in sys.argv[1:]:
	y=''
	for e,f in zip([1000,900,500,400,100,90,50,40,10,9,5,4,1],"M CM D CD C XC L XL X IX V IV I".split()):n,z=divmod(int(z),e);y+=f*n
	print(y)