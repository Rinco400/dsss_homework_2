import unittest
from math_quiz import random_interger_A, random_operator_B, result_calculation_C


class TestMathGame(unittest.TestCase):

    def test_random_integer_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_interger_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator_B(self):
        o = {'+','-','*'}
        for _ in range(1000):
             rand_operator = random_operator_B()
             self.assertTrue(rand_operator in o)

    def test_result_calculation_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (9, 2, '-', '9 - 2', 7),
                (5, 2, '*', '5 * 2', 10),
                
            ]

            for n1, n2, o, expected_problem, expected_answer in test_cases:
                problem, answer = result_calculation_C(n1,n2,o)
                self.assertEqual(problem,expected_problem)
                self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
