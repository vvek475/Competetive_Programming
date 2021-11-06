def Print_Triangle(n:int):
    z=n
    for l in range(n,-1,-1):
        # '*' is multiplied with i in decrement order 
        if l==n:print(n*'*')
        elif l==0:print('*')
        else:print('*'+(l-1)*' '+'*')
         
if __name__=='__main__':
    while True:
        n=input('Enter a valid num :')
        if n.isdigit(): 
            Print_Triangle(int(n))
            break
        print('Sorry, Enter a number')