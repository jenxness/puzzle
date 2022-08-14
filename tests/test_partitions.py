import unittest

from puzzle.partitions import common, partition


class TestPartitions(unittest.TestCase):
    def test_partition(self):
        cases = [
            ((12, 4, list(range(1, 10))), [(1, 2, 3, 6), (1, 2, 4, 5)]),
        ]

        for args, result in cases:
            with self.subTest(target=args[0], size=args[1]):
                self.assertEqual(partition(*args), result)

    def test_common(self):
        cases = [
            ([(1, 2, 3, 6), (1, 2, 4, 5)], {1, 2}),
        ]

        for arg, result in cases:
            with self.subTest(solutions=arg):
                self.assertEqual(common(arg), result)
