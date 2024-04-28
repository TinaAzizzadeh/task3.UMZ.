A=[True,True,True]
B=[True,True,True]
C=[True,True,True]
D=[True,True,True]
for i in [A,B,C,D]:
 for x in i:
  print(x)
 if A[0]==True :
   C[0]=False
 else:
   A[0]==False
   C[0]=True
  
 if A[1]==True :
  C[1]=False
  B[2]=False
 else:
  A[1]==False
  C[1]=True
  B[2]=True
   
 if B[0]==True:
    D[0]=False
 else:
   B[0]==False
   D[0]=True
 if C[2]==True :
   D[1]=False
 else:
   C[2]==False
   D[1]=True
  
 if B[1]==True:
  D[2]=False
 else:
   B[1]==False
   D[2]=True
print("-----------")
if A[1]==True or B[2]==False or C[1]==False:
     print("B is thief")
elif D[2]==True:
     print("A is thief")
elif B[0]==False:
     print("D is thief")
else:
     print(" C is thief")