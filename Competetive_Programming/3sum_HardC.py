class Solution:
    def threeSum( self,param_1):
        param_1.sort()
        ls=[]
        ls1=[]
        ls2=[]
        zero=0
        if len(param_1)<=2:return[]
        for i in param_1:
            if i==0:zero+=1
        if len(param_1)==zero:return [[0,0,0]]
        for i in range(0,len(param_1)):
            for j in range(-1,len(param_1),-1):
                if (param_1[i]-param_1[j])>0:
                    param_1.remove(param_1[j])
                elif (param_1[i]-param_1[j])<0:
                    param_1.remove(param_1[i])
        i=0
        j=1
        k=2
        while i!=len(param_1):
            j=i+1
            
            while j!=len(param_1): 
                k=j+1
                while k!=len(param_1): 
                    if param_1[i]==param_1[j]==param_1[k]==0:
                        ls.append(param_1[i])
                        ls.append(param_1[j])
                        ls.append(param_1[j])
                        ls.sort()
                        if ls not in ls2:
                            ls2.append(ls)
                        ls=[]
                
                        
                    else:
                        if 0==(param_1[i]+param_1[j]+param_1[k]):
                            ls.append(param_1[i])
                            ls.append(param_1[j])
                            ls.append(param_1[k])
                            ls1.append(ls)
                            ls.sort()
                            if ls not in ls2:
                                ls2.append(ls)
                            ls=[]
                    k+=1
                j+=1
            i+=1                        
        return ls2
        
okay=Solution                  
print(okay.threeSum(okay,[-1,0,1,2,-1,-4,123,456,234,667,-456,-321]))