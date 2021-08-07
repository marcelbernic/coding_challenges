
import unittest

class TestChallenge(unittest.TestCase):

    def test_challenge(self):
        print('Test: Empty array')
        self.assertEqual(lomuto_partition([], 0, 0), None)
        print('Test: One element array')
        self.assertEqual(lomuto_partition([0], 0, 0), 0)
        print('Test: Sorted array')
        self.assertEqual(lomuto_partition([5, 2, 3, 4, 1, 6, 7, 8, 9], 0, 8), 4)
        print('Test: Random array')
        self.assertEqual(lomuto_partition([6, 2, 4, 9, 5, 3, 1, 7, 8], 0, 8), 5)
        print('Success: lomuto_partition')

def main():
    test = TestChallenge()
    test.test_challenge()

if __name__ == '__main__':
    main()
