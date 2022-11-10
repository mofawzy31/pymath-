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
