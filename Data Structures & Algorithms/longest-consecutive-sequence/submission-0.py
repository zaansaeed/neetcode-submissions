class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        nums_set = set(nums)
        max_count = 0
        for num in nums:
            if num-1 not in nums_set:
                counter = 0
                temp_num = num
                while temp_num in nums_set:
                    temp_num += 1
                    counter+=1
                if counter > max_count:
                    max_count = counter
        return max_count
                