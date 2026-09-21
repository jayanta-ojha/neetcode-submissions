class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        # for loop (nums1)
        for num in nums1:
            # index of num in nums2
            index = nums2.index(num)
            next_greater = -1

            # find next_greater in nums2
            for j in range(index+1, len(nums2)):
                if nums2[j] > num:
                    next_greater = nums2[j]
                    break

            result.append(next_greater)
        
        return result