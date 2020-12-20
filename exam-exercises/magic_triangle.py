import unittest


def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    if n == 2:
        print(triangle)
    else:
        for i in range(2, n):
            row = [0] * (i + 1)
            for j in range(i + 1):
                if j - 1 >= 0 and j < len(triangle):
                    row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                else:
                    row[j] = 1
            triangle.append(row)

    return triangle


class Tests(unittest.TestCase):
    def test_zero(self):
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        actual = get_magic_triangle(5)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()