
import unittest


class TestChallenge(unittest.TestCase):

    def test_challenge(self):
        self.assertEqual(birth_date_death_date(None), None)
        self.assertEqual(birth_date_death_date(0), 0)
        self.assertEqual(birth_date_death_date('bar'), 'bar')
        print('Success: birth_date_death_date')


def main():
    test = TestChallenge()
    test.test_challenge()


if __name__ == '__main__':
    main()
