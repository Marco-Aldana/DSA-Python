"""
Given an array of integers sorted in ascending order and a target value.

Return:
The indexes of any pair of numbers in the array that sum to the target. 

Details:
The order of the indexes in the result doesn't matter. 
If no pair is found, return an empty array.

Example 1:
    Input: nums = [-2, -1, 0, 5, 8], target = 5
    Output: [2, 3]

    Explanation: nums [2] + nums [3] = 0 + 5 = 7
"""
import pytest
from solutions.pair_sum_sorted import pair_sum_sorted

@pytest.mark.parametrize("target, nums, result",[
    (5, [-2, -1, 0, 5, 8],[2, 3]), #simple solution
    (10, [-1,0,3,4],[]), #no solution
    (4,[],[]), #Empty list
])
def test_pair_sum_sorted(target: int, nums: list[int], result: list[int]):
    assert pair_sum_sorted(target, nums) == result
    