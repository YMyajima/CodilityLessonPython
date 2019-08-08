
class TestValue:
    def __init__(self, A, K, expect):
        self.A = A
        self.K = K
        self.expect = expect


class Solution:

    def __init__(self):
        self.test_values = [
            TestValue([3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8]),
            TestValue([0, 0, 0], 1, [0, 0, 0]),
            TestValue([1, 2, 3, 4], 4, [1, 2, 3, 4]),
            TestValue([], 0, []),
            TestValue([1, 2, 3], 0, [1, 2, 3]),
            TestValue([1, 1, 2, 3, 5], 42, [3, 5, 1, 1, 2])
        ]

    def solution(self, A, K):
        raise NotImplementedError("You must implement.")

    def test(self):
        for test_value in self.test_values:
            s = self.solution(test_value.A, test_value.K)
            print(test_value.__dict__, 'result', s)
            assert s == test_value.expect


class Solution1(Solution):
    """
    CyclicRotation
    100%
    """

    def __init__(self):
        super().__init__()

    def solution(self, A, K):
        length = len(A)
        if length == 0:
            return A
        rotate_count = K % length
        if rotate_count == 0:
            return A
        result = [None] * len(A)
        for i in range(length):
            tmp = i + rotate_count
            next_index = tmp % len(A)
            result[next_index] = A[i]
        return result


if __name__ == '__main__':
    solution = Solution1()
    solution.test()
