from math import *
from random import *
from time import *

def S(t):
  T=0.6
  A=14*exp(1/T)
  return A*exp(-t/T)+1  
  
def play():
  score=0
  t0=monotonic()
  level=1
  add_max=5
  calculs=0
  
  while 1:        
    if calculs%5==0:
      print("* NIVEAU ",int(calculs/5),"*")
      print("________")
      add_max+=1
      t0=monotonic()
    else:
      t0=monotonic()
    a=randint(2,add_max)
    b=randint(2,add_max)
    calcul=randint(1,2)
    
    if calcul==1:
      #addition
      result=a+b
      print(a,"+",b)
    elif calcul==2:
      #multiplication
      result=a*b
      print(a,"x",b)

    rep=input()    
    while rep=="":
      rep=input()
    
    dt=monotonic()-t0
    
    if int(rep)==result:
      score+=S(dt)
      calculs+=1
      print("________                  +", round(S(dt)))
      continue
            
    elif int(rep)!=result:
      print("MAUVAISE REPONSE")
      print("Reponse : ", result)
      print("score : ", round(score))
      if int(input("Rejouer ?"))==1:
        play()        
      else:
        break
            
play()
