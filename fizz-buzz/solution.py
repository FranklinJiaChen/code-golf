i=1
exec("print('Fizz'*(i%3<1)+'Buzz'*(i%5<1)or i);i+=1;"*100)