import unittest

from shuffle_test import checkshufflecycle, intershuffle


class OutShuffleTests(unittest.TestCase):
    def test_interleaves_halves_without_changing_input(self):
        deck = list(range(1, 9))
        self.assertEqual(intershuffle(deck), [1, 5, 2, 6, 3, 7, 4, 8])
        self.assertEqual(deck, list(range(1, 9)))

    def test_known_periods(self):
        for cards, expected in [(2, 1), (4, 2), (8, 3), (52, 8), (54, 52)]:
            with self.subTest(cards=cards):
                self.assertEqual(checkshufflecycle(list(range(cards))), expected)

    def test_period_matches_modular_order(self):
        for cards in range(4, 102, 2):
            modulus = cards - 1
            period, residue = 1, 2 % modulus
            while residue != 1:
                residue = (2 * residue) % modulus
                period += 1
            with self.subTest(cards=cards):
                self.assertEqual(checkshufflecycle(list(range(cards))), period)

    def test_rejects_empty_and_odd_decks(self):
        for deck in [[], [1], [1, 2, 3]]:
            with self.subTest(deck=deck):
                with self.assertRaises(ValueError):
                    intershuffle(deck)


if __name__ == "__main__":
    unittest.main()
