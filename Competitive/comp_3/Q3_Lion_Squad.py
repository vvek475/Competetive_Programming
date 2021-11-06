def Print_Triangle(limit):

    for i in range(1,limit):
        print('*'*(limit-i-1),end='')
        #the above print statement prints stars before the digits
        print(f'*{i}'*i,end='')
        #the above print statement prints the integers 
        print('*'*(limit-i),end='')
        #the above print statement prints stars after the digits
        print()

def Input_validator():
    while True:
        num=input('Enter the limit up to 9 that has to be printed : \n')
        if num.isdigit() and int(num)<=9:
            Print_Triangle(int(num)+1)
            break
        print('Please enter a valid number  \n')

if __name__=='__main__':
    Input_validator()