
list1=[]
list2=[]
list3=[]
z=4
number=6
    
for i in range (0,number): 
        
    list1.append(bin(i+1))
    list2.append(hex(i+1))
    list3.append(oct(i+1))
cb=str(list1[number-1])
cb=cb[2:]
z=len(cb)
print(cb)
print(z)
for i in range(0,number):
    ab=str(list1[i])
    ab=ab[2:]
    ba=str(list2[i])
    ba=ba[2:]
    ba=ba.upper()
    cb=str(list3[i])
    cb=cb[2:]
        

    
    print(str(i+1).rjust(2," ")+(cb).rjust(z," ")+(ba).rjust(z," ")+(ab).rjust(z+1," "))

