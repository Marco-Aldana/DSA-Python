

def pair_sum_unsorted(target: int, nums: list[int]) -> list[int]:
    visited: dict[int, int] = {}
    
    for idx, num in enumerate(nums):
        new_target: int = target - num
        if new_target in visited:
            return [visited[new_target], idx]
        else:
            visited[num] = idx
    return []
    