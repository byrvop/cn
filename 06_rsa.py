import math
def gcd(a,z):
    temp=0
    while(1):
        temp=a%z
        if(temp==0):
            return z
        a=z
        z=temp
if _name=="main_":
    msg=int(input("enter the msg:"))
    p=int(input("enter the value of P"))
    q=int(input("enter the value of Q"))
    n=p*q
    z=(p-1)*(q-1)
    print("value of z is:"+str(z))
    for x in range (2,z):
        if(gcd(x,z)==1):
            break
        print("value of e is "+str(x))
        i=2
        while(((i*x)%z)!=1):
            i+=1
        d=i
        c=poq(msg,x)%n
        print("value of cipher text:"+str(c))
        p1=pow(c,d)%n
        print("value of plaintext :" +str(p1))
