num=list(map(int,input().split()))[:10]
num.sort()
lst=[[num[i],num[j],num[k]]  for i in range(len(num)) for j in range(i+1,len(num)) for k in range(j+1,len(num)) if num[i]+num[j]+num[k]==0]
ls=[]
for i in range(len(lst)):
    lst[i].sort()
    if lst[i] not in ls:
        ls.append(lst[i])
print(ls)