import unittest
from part2 import revise, ac3, minimum_remaining_values

import unittest

class TestReviseFunction(unittest.TestCase):
    def test_basic_constraint_satisfaction_direct(self):
        csp = {
            'variables': {'v1': [1, 2], 'v2': [1, 3]},
            'constraints': {('v1', 'v2'): [(1, 1)]}
        }
        self.assertTrue(revise(csp, 'v1', 'v2'))
        self.assertEqual(csp['variables']['v1'], [1])

    def test_basic_constraint_satisfaction_reversed(self):
        csp = {
            'variables': {'v1': [1, 2], 'v2': [1, 3]},
            'constraints': {('v1', 'v2'): [(1, 1)]}
        }
        self.assertTrue(revise(csp, 'v2', 'v1'))
        self.assertEqual(csp['variables']['v2'], [1])

    def test_no_constraint_between_variables(self):
        csp = {
            'variables': {'v1': [1, 2], 'v2': [3, 4]},
            'constraints': {}
        }
        self.assertFalse(revise(csp, 'v1', 'v2'))
        self.assertEqual(csp['variables']['v1'], [1, 2])

    def test_all_values_removed(self):
        csp = {
            'variables': {'v1': [1, 2], 'v2': [3]},
            'constraints': {('v1', 'v2'): [(1, 4), (2, 5)]}
        }
        self.assertTrue(revise(csp, 'v1', 'v2'))
        self.assertEqual(csp['variables']['v1'], [])

    def test_no_values_removed(self):
        csp = {
            'variables': {'v1': [1, 2], 'v2': [1, 2]},
            'constraints': {('v1', 'v2'): [(1, 1), (2, 2)]}
        }
        self.assertFalse(revise(csp, 'v1', 'v2'))
        self.assertEqual(csp['variables']['v1'], [1, 2])

    def test_complex_constraints_with_reversal(self):
        csp = {
            'variables': {'v1': [1, 2, 3], 'v2': [2, 3, 4]},
            'constraints': {('v2', 'v1'): [(3, 1), (4, 2)]}
        }
        self.assertTrue(revise(csp, 'v1', 'v2'))
        self.assertEqual(csp['variables']['v1'], [1, 2])

    def test_constraint_with_multiple_valid_options(self):
        csp = {
            'variables': {'v1': [1, 2, 3], 'v2': [2, 3]},
            'constraints': {('v1', 'v2'): [(1, 2), (2, 3), (3, 2)]}
        }
        self.assertFalse(revise(csp, 'v1', 'v2'))
        self.assertEqual(csp['variables']['v1'], [1, 2, 3])

    def test_repeated_values_in_constraints(self):
        csp = {
            'variables': {'v1': [1, 2, 3, 4], 'v2': [1, 2, 3, 4]},
            'constraints': {('v1', 'v2'): [(1, 1), (1, 1), (2, 2), (2, 2), (3, 3), (4, 4)]}
        }
        self.assertFalse(revise(csp, 'v1', 'v2'))
        self.assertEqual(csp['variables']['v1'], [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
