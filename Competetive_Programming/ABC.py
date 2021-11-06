def ABS(inp):
    a=inp%1
    if a==0:res=int(125)
    elif a*10<5:res= int(125)
    elif a*10>4:res =int(inp)+1
    return res
print(ABS(125.4))