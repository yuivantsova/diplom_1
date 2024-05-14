from praktikum.bun import Bun
from data import *


class TestBun:

    def test_get_name_bun_true(self):
        bun = Bun(Data.Bun[0], Data.Bun[1])
        assert bun.get_name() == Data.Bun[0]

    def test_gey_price_bun_true(self):
        bun = Bun(Data.Bun[0], Data.Bun[1])
        assert bun.get_price() == Data.Bun[1]