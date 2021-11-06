def Print_Triangle(n):
    for i in range(1,n+1):
        for j in range(i,n+1):
            '''Each line the first element and last are printed 
            others elements are replaced by a whitespace'''
            if i==1:
                print(j,end='  ')
            elif j==i or j==n:
                print(j,end='  ')
            else:
                print('  ',end=' ')
        print('\n')
if __name__=='__main__':
    while True:
        num=input('Enter the limit up to 10 that has to be printed : \n')
        if num.isdigit() and int(num)<=10:
            Print_Triangle(int(num))
            break
        print('Please enter a valid number  \n')