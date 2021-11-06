def backspace(string):      
        str_list=[i for i in string]
        for i,s1 in enumerate(str_list):
            if s1=="#":
                z=1
                while True:
                    #this loop executes until a char is found before a #
                    if str_list[i-z]=='#' and z<i:z+=1
                    else:break
                #from above loop char to backspaced is found and converted to #
                str_list[i-z]="#"
        final_string=("").join(str_list)
        #this list comprehension prints every char except #
        [print(i,end="") for i in final_string if i!="#"]
        
        
def Input_validator():
    while True:
        num=input('Enter the limit up which it has to be printed : \n')
        if True:
            backspace((num))
            break
        print('Please enter a valid number  \n')

if __name__=='__main__':
    Input_validator()
