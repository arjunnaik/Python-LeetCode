class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=0
        var=None
        for i in s:
            sum+=dic[i]
            if var!=None and dic[i]>dic[var]:
                sum-=(dic[var]*2)
            var=i
        return sum
            
        
