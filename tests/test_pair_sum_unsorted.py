"""
Given an array of integers unsorted and a target value.

Return:
The indexes of any pair of numbers in the array that sum to the target. 

Details:
The order of the indexes in the result doesn't matter. 
If no pair is found, return an empty array.

Example 1:
    Input: nums = [-1, -2, 0, 8, 5], target = 5
    Output: [2, 4]

    Explanation: nums [2] + nums [4] = 0 + 5 = 5
"""
import pytest
from solutions.pair_sum_unsorted import pair_sum_unsorted

@pytest.mark.parametrize("target, nums, result",[
    (5, [-1, -2, 0, 8, 5],[2, 4]), #simple solution
    (10, [-1,0,3,4],[]), #no solution
    (4,[],[]), #Empty list
])
def test_pair_sum_sorted(target: int, nums: list[int], result: list[int]):
    assert pair_sum_unsorted(target, nums) == result
    