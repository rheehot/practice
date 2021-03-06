#   https://leetcode.com/problems/maximum-subarray


class Solution:
    #   runtime; 48ms, 97.13%
    def maxSubArray0(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        curSum, maxSum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if curSum + nums[i] < nums[i]:
                curSum = nums[i]
            else:
                curSum += nums[i]
            maxSum = max(maxSum, curSum)
        return maxSum

    #   runtime; 44ms, 91.63%
    #   memory; 13.6MB, 5.50%
    def maxSubArray(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        curSum, maxSum = 0, -float('inf')
        for n in nums:
            curSum += n
            maxSum = max(maxSum, curSum)
            if curSum <= 0:
                curSum = 0
        return maxSum


s = Solution()
data = [([1, 2], 3),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1, 3, 2, -1, 4, 5], 14),
        ([1, 3, 2, -8, 2, 2], 6),
        ]
for nums, expected in data:
    real = s.maxSubArray(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
