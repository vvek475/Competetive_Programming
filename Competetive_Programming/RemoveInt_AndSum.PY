"""""
In a given text you need to sum the numbers while excluding any digits that form part of a word.
The text consists of numbers, spaces and letters from the English alphabet.
Input: A string.
Output: An int.

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
                        'painting by Danish artist Anna '
                        'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
 """
def sum_numbers(text: str) -> int:
    if len(text)==0:return 0
    new=""
    lst=[]
    z1=["s","n","r","t"]
    for i in text:
        if  i.isdigit():new+=i
        elif new!="":
            if i ==" ":            
                lst.append(int(new))
                new=''
            elif i in z1:new=''
    if text[len(text)-1].isdigit():lst.append(int(text[len(text)-1]))
    print(lst)       
    from functools import reduce
    lst1=reduce(lambda x,y:x+y,lst)
    return lst1

if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('my 5 numbers 50 50s is 2'))
