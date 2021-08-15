
import unittest


class TestChallenge(unittest.TestCase):

    def test_challenge(self):
        print("Test case: empty array")
        A = []
        merge_sort(A)
        self.assertEqual(A, [])
        print("Test case: one element array")
        A = [1]
        merge_sort(A)
        self.assertEqual(A, [1])
        print("Test case: two element array")
        A = [7, 3]
        merge_sort(A)
        self.assertEqual(A, [3, 7])
        print("Test case: multiple element array")
        A = [1, 4, 8, 2, 9, 5, 6, 7, 3]
        merge_sort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6, 7, 8, 9])
 
        print('Success: merge_sort')


def main():
    test = TestChallenge()
    test.test_challenge()


if __name__ == '__main__':
    main()
