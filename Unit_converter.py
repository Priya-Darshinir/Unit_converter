u1=input("give unit of length to be converted")
length=float(input("enter length"))


if(u1=="km"):
    
   print(length*1000,"m")

elif(u1=="m"):
   
   print(length,"m")

elif(u1=="cm"):
   
   print(length/100,"m")

else:
    
   print("invalid")
