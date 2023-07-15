from easy.easy_solutions.two_sum import Solution
import pytest


data = (
    ([1, 2, 3, 4, 5], 7, [1, 4]),
    ([1, -2, 3, -1, 5], -3, [1, 3]),
    ([1, 0, 3, 4, 5], 9, [3, 4])
)


@pytest.mark.parametrize('nums, target, result', data)
def test_solutions(nums, target, result):
    assert Solution().twoSum(nums, target) == result
