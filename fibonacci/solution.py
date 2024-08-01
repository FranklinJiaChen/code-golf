a=b=1;p=print;p("0\n1\n1")
exec("p(a:=a+b);p(b:=a+b);"*14)