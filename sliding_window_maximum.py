def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0 or k > len(nums):
        return []
    candidates = []  # indices, values decreasing front to back
    output = []
    for i, num in enumerate(nums):
        # front: drop anything that's aged out of the window
        if candidates and candidates[0] <= i - k:
            candidates.pop(0)
        # back: drop anything smaller than the new number
        while candidates and nums[candidates[-1]] < num:
            candidates.pop()
        candidates.append(i)
        # window is only complete once i has reached k-1
        if i >= k - 1:
            output.append(nums[candidates[0]])
    return output


def sliding_window_maximum2(nums: list[int], k: int) -> list[int]:
    result = []
    nums_l = len(nums)
    if nums_l < k:
        return result
    pos = k
    while pos <= nums_l:
        result.append(max(nums[:pos]))
        pos += 1
    return result
