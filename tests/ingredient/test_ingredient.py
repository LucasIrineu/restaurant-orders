from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    egg = Ingredient('ovo')
    egg_copy = Ingredient('ovo')
    salmon = Ingredient('salmão')

    assert egg.__hash__() == hash('ovo')
    assert egg.__repr__() == "Ingredient('ovo')"
    assert egg.name == 'ovo'
    assert egg.restrictions == {Restriction.ANIMAL_DERIVED}

    assert egg.__eq__(salmon) is False
    assert egg.__eq__(egg_copy) is True

    assert hash(salmon) != hash(egg)
