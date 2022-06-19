class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=0
        b=0
        s =[]
        c = 0
        d = False
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 0:
                c = c+1
            else:
                d = True
                break
        while(digits):
            a = a * 10 + digits.pop()
        while(a):
            b = b * 10 + a% 10
            a = a//10
        if d == True:
            for i in range(c):
                b = b * 10
        b = b + 1
        while(b):
            s.append(b % 10)
            b = b // 10
        return reversed(s)