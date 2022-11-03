#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
from operator import le
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def quicksort(start, end):
            if start >= end:
                return 
            else:
                idx = partition(start, end)
                quicksort(start, idx-1)
                quicksort(idx+1, end)
        
        def partition(start, end):
            if start == end:
                return start
            else:
                pivot = start
                left, right = start + 1, end
                while left <= right:
                    while left <= right and nums[pivot] >= nums[left]:
                        left += 1
                    while right >= left and nums[pivot] < nums[right]:
                        right -= 1
                    if left <= right:
                        nums[left], nums[right] = nums[right], nums[left]
                        left += 1
                        right -= 1

                nums[pivot], nums[right] = nums[right], nums[pivot]
                return right

        random.shuffle(nums)
        quicksort(0, len(nums)-1)
        return nums


# @lc code=end

