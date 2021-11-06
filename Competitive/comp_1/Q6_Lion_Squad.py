def Print_Triangle(n:int):
    z=n
    for i in range(n+1):
        print(' '*(z*2),end='')
        if n==i:
            for j in range(n):
                print('* ',end='  ')
            return
        for j in range(1,i):
            if j==1:print('*',end=' ')
            else:print(' ',end=' ')
        for j in range(i,0,-1):
            if j==1:print('*',end=' ')
            else:print(' ',end=' ')
        print()
        z-=1
         
if __name__=='__main__':
    while True:
        n=input('Enter a valid num :')
        if n.isdigit(): 
            Print_Triangle(int(n))
            break
        print('Sorry, Enter a number')