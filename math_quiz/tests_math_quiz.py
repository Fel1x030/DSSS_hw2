import unittest
from math_quiz import getnum, getsym, prob_result

class TestMathGame(unittest.TestCase):

    def test_getnum(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for i in range(1000):  # Test a large number of random values
            rand_num = getnum(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_getsym(self):
        getsym() in {'+', '-', '*'}

    def test_prob_result(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 9, '*', '3 * 9', 27),
                (3, 7, '-', '3 - 7', -4),
                (7, 2, '-', '7 - 2', 5),
                (5, 0, '*', '5 * 0', 0)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                prob_result(num1,num2,operator) == expected_problem, expected_answer

if __name__ == "__main__":
    unittest.main()
