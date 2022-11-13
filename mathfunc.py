#factorial
def multi(z):
     y=z-1
     while z:
          x=z*y
          z=x
          if y>1:
               y-=1
          else:
               break
     return x
#fibonacci
def fib(x):
    f1=1
    f2=1
    f3=2
    v = []
    while x >= f1 :
        v= v + [f1]
        f1 = f2
        f2 = f3
        f3 = f1 + f2
    return v 
