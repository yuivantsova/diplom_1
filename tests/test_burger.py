from data import *
from praktikum.bun import *


class TestBurger:

    def test_set_buns_true(self, burger, mock_bun):

        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):

        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self, burger, mock_ingredient):

        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger, mock_ingredient):

        ingred_0 = mock_ingredient
        burger.add_ingredient(ingred_0)
        ingred_1 = mock_ingredient
        burger.add_ingredient(ingred_1)
        burger.move_ingredient(1, 0)

        assert burger.ingredients == [ingred_1, ingred_0]

    def test_get_price(self, burger, mock_ingredient, mock_bun):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == Data.result_price

    def test_get_receipt(self, burger, mock_ingredient, mock_bun):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_receipt() == Data.result_receipt


