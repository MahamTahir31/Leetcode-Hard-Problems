class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

if __name__ == "__main__":
    # Test cases
    nums1 = [1, 2, 0]
    nums2 = [3, 4, -1, 1]
    nums3 = [7, 8, 9, 11, 12]

    solution = Solution()

    print("Output for nums1:", solution.firstMissingPositive(nums1))
    print("Output for nums2:", solution.firstMissingPositive(nums2))
    print("Output for nums3:", solution.firstMissingPositive(nums3))
