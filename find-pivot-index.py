class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum_left_to_right = []
        sum_right_to_left = []

        for i in range(0, len(nums)):
            if i == 0:
                sum_left_to_right.append(nums[i])
                continue
            sum_left_to_right.append(sum_left_to_right[-1] + nums[i])

        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                sum_right_to_left.append(nums[i])
                continue
            sum_right_to_left.append(sum_right_to_left[-1] + nums[i])

        sum_right_to_left.reverse()

        for ix, i in enumerate(zip(sum_left_to_right, sum_right_to_left)):
            if i[0] == i[1]:
                return ix

        return -1

print(Solution().pivotIndex([1,7,3,6,5,6]))