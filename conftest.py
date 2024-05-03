import pytest
from data import Data
from praktikum.burger import *
from unittest.mock import Mock
from praktikum.ingredient import *


@pytest.fixture(scope='function')
def ingredient():
    ingredient = Ingredient(Data.Ingredient[0], Data.Ingredient[1], Data.Ingredient[2])
    return ingredient


@pytest.fixture(scope='function')
def burger():
    burger = Burger()
    return burger


@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = Data.Burger[0]
    mock_bun.get_price.return_value = Data.Burger[1]
    return mock_bun


@pytest.fixture(scope='function')
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = Data.Ingredient[1]
    mock_ingredient.get_price.return_value = Data.Ingredient[2]
    mock_ingredient.get_type.return_value = Data.Ingredient[0]
    return mock_ingredient
