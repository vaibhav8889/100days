class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.list1=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target==nums[j]+nums[i]:
                    self.list1.append(i) 
                    self.list1.append(j)
                    return self.list1
    
nums=[2,7,11,15]
target=9
p1=Solution()
list=p1.twoSum(nums,target)
print(list)

                
                