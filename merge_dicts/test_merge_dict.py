from merge_dict import dict_merge, decision_func_sum

import unittest


class MergeDictTestCase(unittest.TestCase):

    def test_merge_dict(self):

        # merge two simple dicts
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        merge_result = dict_merge(dict1, dict2)
        expected_result = {'a': 1, 'b': 2, 'c': 4}
        self.assertEqual(merge_result, expected_result)

        # merge two simple dicts with sum
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        merge_result = dict_merge(dict1, dict2, decision_func=decision_func_sum)
        expected_result = {'a': 1, 'b': 5, 'c': 4}
        self.assertEqual(merge_result, expected_result)

        # merge two simple dicts with sum and different value types for duplicated key
        dict1 = {'a': 1, 'b': '2'}
        dict2 = {'b': 3, 'c': 4}
        merge_result = dict_merge(dict1, dict2, decision_func=decision_func_sum)
        expected_result = 'Please check your dict'
        self.assertIn(expected_result, merge_result)


if __name__ == '__main__':
    unittest.main()
