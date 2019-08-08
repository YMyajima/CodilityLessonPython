class TestValue:
    def __init__(self, A, expect):
        self.A = A
        self.expect = expect


class Solution:

    def __init__(self):
        self.test_values = [
            TestValue([4, 1, 3, 2], 1),
            TestValue([4, 1, 3], 0),
            TestValue([3, 1], 0),
            TestValue([3, 3, 2], 0),
            TestValue([3, 4, 2], 0),
            TestValue([2], 0),
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
        A = sorted(A)
        start = 1
        for a in A:
            if start == a:
                start += 1
            else:
                return 0
        return 1


if __name__ == '__main__':
    solution = Solution1()
    solution.test()
