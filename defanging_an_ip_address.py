class Solution:
    def defangIPaddr(self, address: str):
        new = ""
        for i in address:
            if i == ".":
                new += "[.]"
            else:
                new += i
        return new
        