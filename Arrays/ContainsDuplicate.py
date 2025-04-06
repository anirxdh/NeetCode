class Solution:  #Easy
    def hasDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    

if __name__ == "__main__":
    s = Solution()
    print(s.hasDuplicate([1,py 2, 3, 1])) # True
    print(s.hasDuplicate([1, 2, 3, 4])) # False
    print(s.hasDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])) # True