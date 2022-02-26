class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            nums1, nums2 = nums2, nums1
        count = collections.Counter()

        for num in nums1:
            count[num] += 1

        ans = []
        for num in nums2:
            if count.get(num, 0) > 0:
                ans.append(num)
                count[num] -= 1

        return ans

