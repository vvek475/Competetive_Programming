
def reverse_num(inp):
    #this line converts number to positive if negative
    num=abs(inp)
    strn=str(num)
    nums=int(strn[::-1])
    #these above lines converts num to string and is reversed
    if inp>0:
        print(nums)
    else:
    #if input was negative this converts to negative again after above process
        nums*=-1
        print(nums)
            
def Input_validator():
    while True:
        num=input('Enter string to be reversed: \n')
        if num.isdigit() or (num[0]=='-' and num[1:].isdigit()):
                reverse_num(int(num))
                break
        print('Please enter a valid number  \n')

if __name__=='__main__':
    Input_validator()
