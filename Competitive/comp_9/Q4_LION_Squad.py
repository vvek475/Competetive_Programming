def add_alphabets(input):      
    lst='z a b c d e f g h i j k l m n o p q r s t u v w x y z'
    asci=[]
    if input:
        [asci.append(ord(i)-96) for i in input]
        add=sum(asci)%26
        lst=lst.split()
        dictionary={}
        for i,alp in enumerate(lst):
            dictionary.update({i:alp})
        return dictionary[add]
    else : 
        return 'z'
            
def Input_validator():
    while True:
        lst=list(map(str,input('Enter the list of options to check : \n').split()))
        if True:
            print(add_alphabets(lst))
            break

if __name__=='__main__':
    Input_validator()

