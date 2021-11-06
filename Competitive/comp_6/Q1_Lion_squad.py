def Print_Triangle(limit):
    ls2=[1]

    for i in range(1,limit+1):       
        ls=ls2
        out=[str(s) for s in ls2]
        out=(' ').join(out)
        print(out)
        if i==limit:
            return
        ls2=[1]#adds 1 on index 0 as first element is passed without adding
        for j in range(0,len(ls)-1):
            ls2.append(ls[j]+ls[j+1])#adds a element with next and replace it with that element
        ls2.append(1)#append 1 to list as last element is passed directly without summing
        
        
def Input_validator():
    while True:
        num=input('Enter the limit up which it has to be printed : \n')
        if num.isdigit():
            Print_Triangle(int(num))
            break
        print('Please enter a valid number  \n')

if __name__=='__main__':
    Input_validator()
