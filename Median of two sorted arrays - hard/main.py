class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = sorted(nums1 + nums2)
        n = len(merged)
        
        mid = n // 2  # Index of the middle element
        med = (merged[mid] + merged[~mid]) / 2.0 if n % 2 == 0 else merged[mid]
        
        return med

if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2]
    nums2 = [3, 4]
    median = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Median of {nums1} and {nums2} is: {median}")

    nums1 = [3]
    nums2 = [-2, -1]
    median = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Median of {nums1} and {nums2} is: {median}") 
