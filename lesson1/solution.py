import re


class Solution:
    def __init__(self):
        self.test_values = [
            {
                'N': 1041,
                'expect': 5
            },
            {
                'N': 32,
                'expect': 0
            },
            {
                'N': 2147483647,
                'expect': 0
            },
            {
                'N': 17,
                'expect': 3
            }
        ]

    def solution(self, N):
        raise NotImplementedError("You must implement.")

    def test(self):
        for test_value in self.test_values:
            s = self.solution(test_value.get('N'))
            print(test_value, 'result', s)
            assert s == test_value.get('expect')


class Solution1(Solution):

    def __init__(self):
        super().__init__()

    def solution(self, N):
        n = "{0:b}".format(N)
        s = re.sub(r'0+$', '', n)
        zeros = s.split('1')
        max_val = 0
        for zero in zeros:
            max_val = max(max_val, len(zero))
        return max_val


if __name__ == '__main__':
    solution = Solution1()
    solution.test()
