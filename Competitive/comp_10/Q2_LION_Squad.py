def backspace(auto,autoOption):      
    matches=[]
    for item in autoOption:
        if len(item)>=len(auto):
            ignoreNonAlphabets=[]
            for i in item:
                    if i.isalpha():
                        ignoreNonAlphabets.append(i)
            filteredItem=('').join(ignoreNonAlphabets)
            trim=filteredItem[:len(auto)]
            trim=trim.lower()
            if auto == trim:
                matches.append(item)
        else:
            continue
    return matches
            
def Input_validator():
    while True:
        auto=input('Enter the letters to autocomplete : \n')
        autoOption=list(map(str,input('Enter the list of options to check : \n').split()))
        if True:
            print(backspace(auto,autoOption))
            break
        print('Please enter a valid number  \n')

if __name__=='__main__':
    Input_validator()