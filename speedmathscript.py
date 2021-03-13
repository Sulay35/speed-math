from math import *
from random import *
from time import *

calculs=[1,2]    
  
def play():
  score=0
  t0=monotonic()
  level=1
  add_max=5
  
  while 1:        
    if score%5==0:
      print("* NIVEAU ",int(score/5),"*")
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
    
    if int(rep)==result and dt<=5:
      score+=1
      #t0=monotonic()
      print("________",score)
      continue      
    elif int(rep)!=result:
      print("MAUVAISE REPONSE")
      print("Reponse : ", result)
      print("score : ", score)
      if int(input("Rejouer ?"))==1:
        play()        
      else:
        break
      
    elif dt>5:
      print("TEMPS ECOULE  |  SCORE : ", score)
      if int(input("Rejouer ?"))==1:
        play()        
        break
      else:
        break        
play()
