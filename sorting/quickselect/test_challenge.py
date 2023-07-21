
import unittest


class TestChallenge(unittest.TestCase):

    def test_challenge(self):
        print('Sorted array asc')
        self.assertEqual(quickselect([0, 1, 2, 3, 4, 5, 6], 4), 3)
        print('Sorted array desc')
        self.assertEqual(quickselect([6, 5, 4, 3, 2, 1, 0], 4), 3)
        print('One element array')
        self.assertEqual(quickselect([1], 1), 1)
        print('Unsorted array - first element')
        self.assertEqual(quickselect([9, 4, 6, 1, 2, 7, 5, 3, 8], 1), 1)
        print('Unsorted array - last element')
        self.assertEqual(quickselect([9, 4, 6, 1, 2, 7, 5, 3, 8], 9), 9)
        print('Unsorted array - middle element')
        self.assertEqual(quickselect([9, 4, 6, 1, 2, 7, 5, 3, 8], 4), 4)
        print('Success: quickselect')


def main():
    test = TestChallenge()
    test.test_challenge()


if __name__ == '__main__':
    main()
