class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                sum = (nums[i] + nums[l] + nums[r])
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                    r -= 1
        
        return [list(inner_set) for inner_set in res]

            

            
        