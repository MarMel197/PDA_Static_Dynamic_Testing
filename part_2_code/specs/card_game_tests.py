import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("hearts", 1)
        self.card2 = Card("clubs", 5)
        self.cards = [self.card1, self.card2]
        self.CardGame = CardGame()

    def test_check_for_ace__True(self):
        self.assertEqual(True, CardGame.check_for_ace(self, self.card1))

    def test_check_for_ace__False(self):
        self.assertEqual(False, CardGame.check_for_ace(self, self.card2))

    def test_check_highest_card(self):
        self.assertEqual(self.card2, CardGame.highest_card(self, self.card1, self.card2))

    def test_check_highest_card__swapped(self):
        self.card1 = Card("clubs", 5)
        self.card2 = Card("hearts", 1)
        self.assertEqual(self.card1, CardGame.highest_card(self, self.card1, self.card2))

    def test_check_cards_total(self):
        self.assertEqual("You have a total of 6", CardGame.cards_total(self, self.cards))