
import unittest

class TestChallenge(unittest.TestCase):

    def test_challenge(self):
        print("Test case: empty array")
        self.assertEqual(quicksort([]), [])
        print("Test case: one element array")
        self.assertEqual(quicksort([1]), [1])
        print("Test case: two element array")
        self.assertEqual(quicksort([7, 3]), [3, 7])
        print("Test case: multiple element array")
        self.assertEqual(quicksort([1, 4, 8, 2, 9, 5, 6, 7, 3]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
 
        print('Success: quicksort')

def main():
    test = TestChallenge()
    test.test_challenge()


if __name__ == '__main__':
    main()
