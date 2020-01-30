class Solution:
    def reverseBits(self, n: int) -> int:
        s, l = self.tobits(n)
        return self.tonum(s, l)
    
    def tobits(self, n: int):
        s = [0] * 32
        l = len(s)
        
        while n > 0:
            s[l-1] = (n % 2)
            n //= 2
            l -= 1
        
        return s, 32-l
        
    def tonum(self, s: list, l: int):
        num = 0
        s = s[::-1]
        
        for i in range(l):
            num += s[i] * pow(2, 32-i-1)
        
        return num
