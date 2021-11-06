class Solution:
    def reverse(self, m: int) -> int:
        n=list(str(m)[::-1])  
        if m<0:
            n.pop()
            z=-int("".join(n))
        else:z=int(("".join(n)))
        if -2**31 >= z or z >= 2**31 - 1:return 0
        return z


okay=Solution
print(okay.reverse(okay,-101100))