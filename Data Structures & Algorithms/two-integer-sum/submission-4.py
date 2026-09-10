class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = defaultdict()
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in num_to_idx:
                return [min(i, num_to_idx[diff]), max(i, num_to_idx[diff])]
            else:
                num_to_idx[nums[i]] = i 
        
        
        