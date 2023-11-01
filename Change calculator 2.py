import math 
def Change2(N,C):
    k=math.log(N)/math.log(C)
    k=int(k//1)
    n=N*100
    L1=[]
    L2=[]
    for i in range(k+1):
        L1.append(C**i)
    L1.reverse()
    for i in L1:
        Rem=n%i
        L2.append(n//i)
        n=Rem
    for i in range(0,len(L1)):
        print (L1[i], "=", L2[i])
