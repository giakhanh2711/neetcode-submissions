class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                if numbers[mid] > tmp:
                    right -= 1
                else:
                    left += 1
                