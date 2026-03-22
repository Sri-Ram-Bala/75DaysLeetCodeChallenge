class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        added_index = []
        for index, element in enumerate(numbers):
            i = index + 1
            find_num = target - element
            if find_num in numbers:
                try:
                    n = numbers.index(find_num, i)
                    added_index.append(i)
                    added_index.append(n+1)
                    break
                except ValueError:
                    continue
        return added_index