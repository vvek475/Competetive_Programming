class Solution:
    def isValid(self, s: str) -> bool:
        c_open=['{','[','(']
        c_close=['}',']',')']
        last=[]
        if len(s)%2!=0:return False
        for st in s:
            if st in c_open: 
                last.append(st)
                continue
            elif st in c_close and len(last)>0:
                if c_open.index(last[-1])==c_close.index(st) :
                    last.pop()
                    continue
            return False
        if len(last)==0:return True
par= Solution
print(par.isValid(par,"([}}])"))