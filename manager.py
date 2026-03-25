import json
from typing import List, Union
from models import Ingredient, Recipe, Supplier

class RestaurantManager:
    def __init__(self, filepath: str = "restaurant_data.json"):
        self.filepath = filepath
        self.ingredients: List[Ingredient] = []
        self.recipes: List[Recipe] = []
        self.suppliers: List[Supplier] = []
        self.load_data()

    def add_item(self, category: str, item: Union[Ingredient, Recipe, Supplier]):
        target_list = getattr(self, category)
        target_list.append(item)

    def get_all(self, category: str):
        return getattr(self, category)

    def remove_item(self, category: str, item_id: int):
        target_list = getattr(self, category)
        setattr(self, category, [i for i in target_list if i.id != item_id])

    def save_data(self):
        data = {
            "ingredients": [i.model_dump() for i in self.ingredients],
            "recipes": [r.model_dump() for r in self.recipes],
            "suppliers": [s.model_dump() for s in self.suppliers]
        }
        with open(self.filepath, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        try:
            with open(self.filepath, 'r') as f:
                content = json.load(f)
                self.ingredients = [Ingredient(**i) for i in content.get("ingredients", [])]
                self.recipes = [Recipe(**r) for r in content.get("recipes", [])]
                self.suppliers = [Supplier(**s) for s in content.get("suppliers", [])]
        except (FileNotFoundError, json.JSONDecodeError):
            pass

