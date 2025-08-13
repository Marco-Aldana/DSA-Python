

def pair_sum_sorted(target: int, nums: list[int]) -> list[int]:
    left: int = 0
    right: int = len(nums)-1
    
    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            return [left, right]
    
    return []
    