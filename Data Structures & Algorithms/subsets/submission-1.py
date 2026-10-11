class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            # decision to not include nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res

        # Time complexity O(n*2^n) where n is the size of the input and 2^n since we have at most 2^n options to go through from each node 
        # Space complexity O(n) extra space since we our subset is at most the size of the input 
        # O(2^n) for hte output list