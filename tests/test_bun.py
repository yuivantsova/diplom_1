from praktikum.bun import Bun
from data import *


class TestBun:

    def test_get_name_bun_true(self):
        bun = Bun(Data.Burger[0], Data.Burger[1])
        assert bun.get_name() == 'Булка'

    def test_gey_price_bun_true(self):
        bun = Bun(Data.Burger[0], Data.Burger[1])
        assert bun.get_price() == 300