class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 1
        if s == "":
            return 0
        for i in range(len(s)):
            stringArr = s[i]
            for j in range(i+1,len(s)):
                if s[j] not in stringArr:
                    stringArr = stringArr + s[j]
                    length = max(length, len(stringArr))
                else:
                    break
        return length
          