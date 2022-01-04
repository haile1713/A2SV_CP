class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        occur= Counter(arr1)
        
        for i in arr2:
            ans += [i] * occur[i]
            del occur[i]
        remaining_elt = occur.elements()
        remaining_elt  = sorted(remaining_elt)
        
        for i in range(len(remaining_elt)):
            ans.append(remaining_elt[i])
        return ans
