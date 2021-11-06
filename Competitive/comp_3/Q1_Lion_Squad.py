def Print_Triangle(rows):
    for i in range(1, rows):
        #the below list comprehension prints num in ascending order

        [print(frwd,end=' ') for frwd in range(1,i-1)]
        
        #the below list comprehension prints num in descending order
        
        [print(bcwd,end=' ') for bcwd in range(i-1,0,-1)]
        
        print()

def Input_Validator():
    while True:
        num=input('Enter a valid num :')
        if num.isdigit(): 
            Print_Triangle(int(num)+2)
            break
        print('Sorry, Enter a number')

if __name__=='__main__':
    Input_Validator()
    
    

