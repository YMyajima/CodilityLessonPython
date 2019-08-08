class TestValue:
    def __init__(self, A, expect):
        self.A = A
        self.expect = expect


class Solution:

    def __init__(self):
        self.test_values = [
            TestValue([3, 1, 2, 4, 3], 1),
            TestValue([3, 1], 2),
        ]

    def solution(self, A):
        raise NotImplementedError("You must implement.")

    def test(self):
        for test_value in self.test_values:
            s = self.solution(test_value.A)
            print(test_value.__dict__, 'result', s)
            assert s == test_value.expect


class Solution1(Solution):

    def __init__(self):
        super().__init__()

    def solution(self, A):
        sum_value = sum(A)
        left = 0
        min_value = None
        for p in range(0, len(A)-1):
            current_a = A[p]
            left += current_a
            right = sum_value - left
            if min_value is None:
                min_value = abs(left - right)
            else:
                min_value = min(min_value, abs(left - right))
        return min_value


if __name__ == '__main__':
    solution = Solution1()
    solution.test()
