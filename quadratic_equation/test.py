import unittest
from main import solve
from math import nan, inf


class TestQuadraticEquationSolve(unittest.TestCase):
    def test_no_roots(self):
        res = solve(1, 0, 1)
        self.assertEqual([], res)

    def test_two_root(self):
        res = solve(1, 0, -1)
        self.assertEqual([1, -1], res)

    def test_one_root(self):
        res = solve(1, 2, 1)
        self.assertEqual([-1], res)

    def test_a_about_zero(self):
        a = 0.3 - (0.1 + 0.2)
        with self.assertRaises(ValueError):
            solve(a, 2, 1)

    def test_d_about_zero(self):
        b = 2 + 0.1 + 0.2
        a = 1.3225
        c = 1
        res = solve(a, b, c)
        self.assertAlmostEqual(-0.869565217, res[0], places=9)

    def test_nan(self):
        with self.assertRaises(ValueError):
            solve(nan, 2, 1)

    def test_inf(self):
        with self.assertRaises(ValueError):
            solve(1, inf, 1)

    def test_neg_inf(self):
        with self.assertRaises(ValueError):
            solve(1, 2, -inf)


if __name__ == '__main__':
    unittest.main()
