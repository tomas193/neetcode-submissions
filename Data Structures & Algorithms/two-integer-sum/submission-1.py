class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = {}
        
        for idx in range(len(nums)):
            complement = target - nums[idx]
            
            if complement in candidates:
                return [ candidates[complement], idx ]
                
            if nums[idx] not in candidates:
                candidates[nums[idx]] = idx

        return []