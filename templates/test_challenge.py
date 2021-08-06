
import unittest


class TestChallenge(unittest.TestCase):

    def test_challenge(self):
        self.assertEqual(foo(None), None)
        self.assertEqual(foo(0), 0)
        self.assertEqual(foo('bar'), 'bar')
        print('Success: test_foo')


def main():
    test = TestChallenge()
    test.test_challenge()


if __name__ == '__main__':
    main()
