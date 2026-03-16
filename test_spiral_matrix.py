"""测试 spiral matrix 的各种情况"""
import unittest
from spiral_matrix import Solution


class TestSpiralMatrix(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_3x3(self):
        """标准 3x3 矩阵"""
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(self.sol.spiralOrder(matrix), expected)

    def test_3x4(self):
        """3行4列矩阵（题目示例）"""
        matrix = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]]
        expected = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEqual(self.sol.spiralOrder(matrix), expected)

    def test_4x3(self):
        """4行3列矩阵"""
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12]]
        expected = [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
        self.assertEqual(self.sol.spiralOrder(matrix), expected)

    def test_1x1(self):
        """单元素"""
        matrix = [[42]]
        expected = [42]
        self.assertEqual(self.sol.spiralOrder(matrix), expected)

    def test_1xn_single_row(self):
        """单行矩阵"""
        matrix = [[1, 2, 3, 4, 5]]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.sol.spiralOrder(matrix), expected)

    def test_mx1_single_col(self):
        """单列矩阵"""
        matrix = [[1],
                  [2],
                  [3],
                  [4],
                  [5]]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.sol.spiralOrder(matrix), expected)

    def test_2x2(self):
        """2x2 矩阵"""
        matrix = [[1, 2],
                  [3, 4]]
        expected = [1, 2, 4, 3]
        self.assertEqual(self.sol.spiralOrder(matrix), expected)

    def test_2x3(self):
        """2行3列"""
        matrix = [[1, 2, 3],
                  [4, 5, 6]]
        expected = [1, 2, 3, 6, 5, 4]
        self.assertEqual(self.sol.spiralOrder(matrix), expected)

    def test_3x2(self):
        """3行2列"""
        matrix = [[1, 2],
                  [3, 4],
                  [5, 6]]
        expected = [1, 2, 4, 6, 5, 3]
        self.assertEqual(self.sol.spiralOrder(matrix), expected)

    def test_empty_matrix(self):
        """空矩阵"""
        matrix = []
        expected = []
        self.assertEqual(self.sol.spiralOrder(matrix), expected)

    def test_empty_row(self):
        """有空行的矩阵"""
        matrix = [[]]
        expected = []
        self.assertEqual(self.sol.spiralOrder(matrix), expected)

    def test_5x5(self):
        """5x5 矩阵（奇数维，中心只剩一个元素）"""
        matrix = [[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25]]
        expected = [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21,
                    16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]
        self.assertEqual(self.sol.spiralOrder(matrix), expected)

    def test_4x4(self):
        """4x4 矩阵（偶数维）"""
        matrix = [[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]]
        expected = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
        self.assertEqual(self.sol.spiralOrder(matrix), expected)


if __name__ == '__main__':
    unittest.main()
