class Solution:
    def romanToInt(self, s: str) -> int:
        romnum={'I': 1,'V': 5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s=list(map(str,s[::-1]))
        lst=[0]
        def ToFind(i):
            now=romnum[s[i]]
            if lst[-1]<=now:lst.append(now)
            elif now<lst[-1]:lst.append(-now)
            return
        list(map(ToFind,list(range(len(s)))))
        return sum(lst)
okay=Solution              
print(okay.romanToInt(okay,"I"))
