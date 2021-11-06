def Print_Triangle(num):
# I will print the rows  
    for i in range(1, num+1):  
    # J will print number the column  
        for j in range(1, i +1):  
            if j==1 or j==i:
                print(j,end=' ')
            elif i==num:
                print(j,end=' ')
            else: 
                if j>9:print(' ',end='')
                print(" ",end=' ')  
        print()
    
if __name__=='__main__':
    while True:
        num=input('Enter the limit within 10 that has to be printed : \n')
        if num.isdigit() and int(num)<=10:
            Print_Triangle(int(num))
            break
        print('Please enter a valid number  \n')