def Print_Triangle(n):
    z=n
    for i in range(1,n+1):
        '''Each line the first element and last are printed 
        others elements are replaced by a whitespace
        and spaces are printed for decrement of n on front'''
        print(' '*z,end=' ')
        for j in range(1,i+1): 
            if i==n:
                print(j,end=' ')
            elif j==1 or j==i: 
                print(j,end=' ')
            else:
                print(' ',end=' ')
        print()            
        z-=1

if __name__=='__main__':
    while True:
        num=input('Enter the limit up to 10 that has to be printed : \n')
        if num.isdigit() and int(num)<=10:
            Print_Triangle(int(num))
            break
        print('Please enter a valid number  \n')