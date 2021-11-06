n=int(input('Enter val'))
stack=[]
for i in range(n):
    print(("*"*(i+1)))
    if i!=(n-1):
        stack.insert(0,("*"*(i+1)))
print(('\n'.join(stack)))


