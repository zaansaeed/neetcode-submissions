class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {num: i for i, num in enumerate(nums)}
        num_set = set(nums)
        for i,num in enumerate(nums):
            if target-num in num_set:
                _min = min(i, num_to_idx[target-num])
                _max = max(i, num_to_idx[target-num])
                if _min != _max:
                    return [_min,_max]
        