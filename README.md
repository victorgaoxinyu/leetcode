### 169 Majority Element
- The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
- Use Boyer-Moore Voting Algorithm.
```
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1

        for i in nums:
            if i == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = i
                count = 1
        return candidate        
```# leetcode
