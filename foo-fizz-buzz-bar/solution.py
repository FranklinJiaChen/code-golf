i=0
exec("print(i%2*'Foo'+i%3//2*'Fizz'+i%5//4*'Buzz'+i%7//6*'Bar'or i+1);i+=1;"*1000)