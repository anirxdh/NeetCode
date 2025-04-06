class Solution:  #Easy
   def removeDuplicates(self, nums: list[int]) -> int:
       if len(nums) == 0:
           return 0
       j=1


       for i in range (1,len(nums)):
           if nums[i]!=nums[i-1]:
               nums[j]=nums[i]
               j+=1
       return j
   

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 1, 2])) # 2
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5
    print(s.removeDuplicates([1, 1, 1, 3, 3, 3, 4, 4, 5])) # 4