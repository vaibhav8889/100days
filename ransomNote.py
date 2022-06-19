class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = 0
        for i in ransomNote:
            a = ransomNote.count(i)
            b = magazine.count(i)
            if b >= a:
                count += 1
        if count == len(ransomNote):
            return True
        else:
            return False
        
        