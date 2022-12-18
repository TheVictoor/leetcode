class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_as_hash = {}
        twice = {}
        for i, n in enumerate(nums):
            if num_as_hash.get(n) is not None:
                twice[n] = i
            else:
                num_as_hash[n] = i

        for number in nums:
            r = target - number
            if num_as_hash.get(r) and num_as_hash[r] != num_as_hash[number]:
                return [num_as_hash[number], num_as_hash[r]]

            if r == number and twice.get(number):
                return [num_as_hash[number], twice[number]]
