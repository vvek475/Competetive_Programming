def Fib(now=1,prev=0):
    if now<=0 or now>n:return
    else:
        print(now)
        Fib(now+prev,now)   
n=int(input())    
if __name__=='__main__':
    Fib() 