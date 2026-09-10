class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(0, len(nums)-1):
            prefix.append(prefix[-1]*nums[i])
        
        suffix = deque([1])
        for i in range(len(nums)-1, 0, -1):
            num = nums[i]*suffix[0]
            suffix.appendleft(num)
        
        res = []
        for idx in range(len(nums)):
            res.append(prefix[idx]*suffix[idx])

        return res