
class TestValue:
    def __init__(self, A, expect):
        self.A = A
        self.expect = expect


class Solution:

    def __init__(self):
        self.test_values = [
            TestValue([9, 3, 9, 3, 9, 7, 9], 7),
            TestValue([1], 1)
        ]

    def solution(self, A):
        raise NotImplementedError("You must implement.")

    def test(self):
        for test_value in self.test_values:
            s = self.solution(test_value.A)
            print(test_value.__dict__, 'result', s)
            assert s == test_value.expect


class Solution1(Solution):
    """
    OddOccurrencesInArray
    100%
    O(N) or O(N*log(N))
    """

    def __init__(self):
        super().__init__()

    def solution(self, A):
        result = 0
        for a in A:
            result ^= a
        return result


if __name__ == '__main__':
    solution = Solution1()
    solution.test()
