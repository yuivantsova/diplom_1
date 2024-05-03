from praktikum import ingredient_types


class Data:

    Burger = ['Булка', 300]
    Ingredient = [ingredient_types.INGREDIENT_TYPE_FILLING, 'tomato', 10]
    result_price = (Burger[1]) * 2 + Ingredient[2]
    result_receipt = f'(==== {Burger[0]} ====)\n' \
                     f'= {(Ingredient[0].lower())} {Ingredient[1]} =\n' \
                     f'(==== {Burger[0]} ====)\n' \
                     '\n' \
                     f'Price: 610'
