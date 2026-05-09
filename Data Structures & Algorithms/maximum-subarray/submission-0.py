class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            if current + n > n:
                current+=n
            else:
                current = n
            print("current",current)

            if current> max_sum:
                max_sum = current
            print("max_sm",max_sum)
        return max_sum
        
        