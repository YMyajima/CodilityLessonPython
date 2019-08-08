
class TestValue:
    def __init__(self, X, Y, D, expect):
        self.X = X
        self.Y = Y
        self.D = D
        self.expect = expect


class Solution:

    def __init__(self):
        self.test_values = [
            TestValue(10, 85, 30, 3),
            TestValue(10, 10, 30, 0),
            TestValue(10, 100, 45, 2),
        ]

    def solution(self, X, Y, D):
        raise NotImplementedError("You must implement.")

    def test(self):
        for test_value in self.test_values:
            s = self.solution(test_value.X, test_value.Y, test_value.D)
            print(test_value.__dict__, 'result', s)
            assert s == test_value.expect


class Solution1(Solution):
    """
    CyclicRotation
    100%
    """

    def __init__(self):
        super().__init__()

    def solution(self, X, Y, D):
        actual_y = Y - X
        if actual_y == 0:
            return 0
        jump_num = actual_y // D
        remaining_y = actual_y % D
        if remaining_y > 0:
            return jump_num + 1
        return jump_num


if __name__ == '__main__':
    solution = Solution1()
    solution.test()
