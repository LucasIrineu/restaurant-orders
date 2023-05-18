# Req 3
from src.models.dish import Dish
from src.models.ingredient import Ingredient
from typing import List, Dict
import csv
# test = MenuData('tests/mocks/menu_base_data.csv')


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.data = self.read(source_path)
        self.dishes = self.create_menu()

    def read(self, path: str) -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    def create_menu(self):
        menu = set()
        data = self.data
        for recipe in data:
            price = float(recipe['price'])
            ingredient = Ingredient(recipe['ingredient'])
            recipe_amount = int(recipe['recipe_amount'])
            dish = Dish(recipe['dish'], price)
            dish.add_ingredient_dependency(ingredient, recipe_amount)

            if dish not in menu:
                menu.add(dish)
            else:
                for item in menu:
                    if item == dish:
                        item.add_ingredient_dependency(
                            ingredient, recipe_amount
                        )
        return menu
