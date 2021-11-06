def Print_Triangle(n):
    z=n
    for i in range(n):
        '''Two loops are made one in increment and other
        in decrement each print values in their order 
        next to next'''
        print((z*2)*'  ',end='')
        for j in range(i+1,2*i+2):
            
            print(' ',j,end='')
            if j<10:print(' ',end='')
            
        for j in range(2*i,i,-1):
            
            print(' ',j,end='')
            if j<10:print(' ',end='')
            
        print()
        z-=1
    
if __name__=='__main__':
    while True:
        num=input('Enter the limit up to which it has to be printed : \n')
        if num.isdigit():
            Print_Triangle(int(num))
            break
        print('Please enter a valid number  \n')