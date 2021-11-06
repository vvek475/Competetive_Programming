class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ls=[]
        if len(s)<2 :return False
        for i in s:
            if ls not in ls:
                ls.append(i)
                con=''.join(ls)
            else:break
        
        con=''.join(ls)
        if len(con)==len(s):return False
        for i in range(len(con),len(s),len(con)):
            ok=s[i:i+len(con)]
            if ok!=con and len(con)==len(s):return False
        return True
result=Solution()
print(result.repeatedSubstringPattern('abab'))
                