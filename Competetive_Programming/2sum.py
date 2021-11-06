class Solution:    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
            dictionary = {}

            for i in range(len(nums)):
                secondNumber = target-nums[i]
                if(secondNumber in dictionary.keys()):
                    secondIndex = nums.index(secondNumber)
                    return sorted([i, secondIndex])

                dictionary.update({nums[i]: i})

okay=Solution                  
print(okay.twoSum(okay,[2,11,15,7],9))