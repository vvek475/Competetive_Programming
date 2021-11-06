def print_diamond(inp):
    #input is doubled for upper and lower triangle 
    limit=inp*2-4
    increment=0
    #this prints the first line
    print(' '*(limit//2),'*')
    for i in range(limit+1):
        #the below if statement is to print upper part of diamond
        if i<limit//2:
            print((limit//2-i)*" ",end='')
            print('*',end='')
            print(' '*(i),end='')
            print('*',end='')
            print(' '*(i),end='')
            print('*')
        #the below if statement is to print umiddle part of diamond
        elif i==limit//2:
            print('* '*(limit//2+2))
        #the below if statement is to print upper part of diamond
        else:
            increment+=1
            print((i-limit//2)*" ",end='')
            print('*',end='')
            print(' '*(i-2*increment),end='')
            print('*',end='')
            print(' '*(i-2*increment),end='')
            print('*')
    #this prints the last line
    print(' '*(limit//2),'*')

def Input_validator():
    while True:
        num=input('Enter string to be reversed: \n')
        if num.isdigit():
                print_diamond(int(num))
                break
        print('Please enter a valid number  \n')

if __name__=='__main__':
    Input_validator()
