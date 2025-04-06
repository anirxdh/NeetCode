class Solution:  #Easy
   def getConcatenation(self, nums: list[int]) -> list[int]:
       ans = []
       for i in range(2):
           for num in nums:
               ans.append(num)
       return ans


if __name__ == "__main__":
    s = Solution()
    print(s.getConcatenation([1, 2, 1])) # [1, 2, 1, 1, 2, 1]
    print(s.getConcatenation([1, 3, 2, 1])) # [1, 3, 2, 1, 1, 3, 2, 1]
    print(s.getConcatenation([0])) # [0, 0]