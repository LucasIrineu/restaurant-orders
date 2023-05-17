from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    gohan = Dish('gohan', 5.50)
    gohan_copy = Dish('gohan', 5.50)
    gohan.add_ingredient_dependency(Ingredient('rice'), 5)

    assert gohan.name == 'gohan'
    assert gohan.__repr__() == "Dish('gohan', R$5.50)"
    assert gohan.__hash__() == hash(gohan.__repr__())
    assert gohan.__eq__(gohan_copy) is True
    assert gohan.recipe == {Ingredient('rice'): 5}
    assert gohan.get_ingredients() == {Ingredient('rice')}
    assert gohan.get_restrictions() == set()

    with pytest.raises(TypeError):
        Dish('gohan', 'preço')
    with pytest.raises(ValueError):
        Dish('gohan', -1)
