def Print_Triangle(n:int):
    z=n
    for i in range(0,n):
        print(i*' ','*'+(z*2*' ')+'*')
        #i is used in increment order to print spaces in front of actual triangle
        #z is decremented and multipled with '*' and printedas it is a inverse triangle   
        z-=1   
        
if __name__=='__main__':
    while True:
        n=input('Enter a valid num :')
        if n.isdigit(): 
            Print_Triangle(int(n))
            break
        print('Sorry, Enter a number')