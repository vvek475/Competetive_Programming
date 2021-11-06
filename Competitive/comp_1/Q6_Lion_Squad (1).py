def Print_Triangle(num):
   for i in range(num):
    for j in range(num-i):
        print(' ', end=' ') # printing space required and staying in same line
    
    for j in range(2*i+1):
        if i==num-1:
            if j%2==0:
                print('* ',end='  ')
        elif j==0 or j==2*i:
            print('*',end=' ')
        else:
            print(' ', end=' ')
    print() # printing new line
         
def input_val(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break 

if __name__=="__main__":

    num = input_val("Enter Number: ")
    Print_Triangle(num)