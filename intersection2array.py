class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
      
        duplicates = []
        for i in nums1:
            if i in nums2:
                duplicates.append(i) 
        final_res = []
        for i in duplicates:
            if i not in final_res:
                final_res.append(i)   
        return final_res
