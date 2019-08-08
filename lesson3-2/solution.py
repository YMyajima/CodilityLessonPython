class TestValue:
    def __init__(self, A, expect):
        self.A = A
        self.expect = expect


class Solution:

    def __init__(self):
        self.test_values = [
            TestValue([2, 3, 1, 5], 4),
            TestValue([1, 2, 3], 4),
            TestValue([], 1),
            TestValue([10, 8, 1, 2, 3, 5, 9, 4, 6], 7),
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
        index = 1
        for a in A:
            if a == index:
                index += 1
                continue
            else:
                return index
        return index


if __name__ == '__main__':
    solution = Solution1()
    solution.test()
