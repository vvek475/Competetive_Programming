def reverse_num(limit):
    logo='.|.'
    hypen='-'
    decrement=-1
    increment=limit//2+3
    for i in range(1,limit//2+1):
    #this loop prints upper half
        decrement+=1
        increment-=1
        print((2*(limit//2-i)+increment)*hypen,end="")
        print((i+decrement)*logo,end="")
        print((2*(limit//2-i)+increment)*hypen)
    #this line prints welcome line
    print(hypen*(limit-6+limit//2+4),'WELCOME',hypen*(limit-6+limit//2))
    increment=0
    decrement=limit//2
    for i in range(0,limit//2):
    #this loop prints lower half
        increment+=1
        decrement-=1
        print(((i+2*increment)+1)*hypen,end="")
        print(((limit//2-i)+decrement)*logo,end="")
        print(((i+2*increment)+1)*hypen)
                
def Input_validator():
    while True:
        num=input('Enter the number upto which it has  to be printd: \n')
        if num.isdigit():
                reverse_num(int(num))
                break
        print('Please enter a valid number  \n')

if __name__=='__main__':
    Input_validator()
