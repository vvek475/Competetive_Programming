def Print_Triangle(n):
    for i in range(1,n):

        #the below print statement prints space before triangle

        print(' '*(n-i)*2,end='')

        #the below print statement prints number upto middle

        [print(frwd,end='') if frwd>9 else print(frwd,end=' ') for frwd in range(1,i)]

        #the below print statement prints number frommiddle

        [print(bcwd,end='') if bcwd>9 else print(bcwd,end=' ') for bcwd in range(i-2,0,-1)]   

        print()

def Input_validator():
    while True:
        num=input('Enter the limit up to 9 that has to be printed : \n')
        if num.isdigit():
            Print_Triangle(int(num)+2)
            break
        print('Please enter a valid number  \n')

if __name__=='__main__':
    Input_validator()