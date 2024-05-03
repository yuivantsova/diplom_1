import pytest
from praktikum.ingredient import *
from data import Data
from praktikum import ingredient_types


class TestIngredient:

    def test_get_price(self, ingredient):
        assert ingredient.get_price() == Data.Ingredient[2]

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == Data.Ingredient[1]

    @pytest.mark.parametrize('type',
                             (ingredient_types.INGREDIENT_TYPE_FILLING,
                              ingredient_types.INGREDIENT_TYPE_SAUCE))
    def test_get_type(self, type):
        ingredient = Ingredient(type, Data.Ingredient[1], Data.Ingredient[2])
        assert ingredient.get_type() == type
