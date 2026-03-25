import unittest
import os
import json
from pydantic import ValidationError
from models import Supplier, Ingredient, Recipe
from manager import RestaurantManager

class TestModels(unittest.TestCase):
    def test_supplier_valid(self):
        s = Supplier(id=1, name="Test", email="test@example.com")
        self.assertEqual(s.email, "test@example.com")

    def test_supplier_invalid_email(self):
        with self.assertRaises(ValidationError):
            Supplier(id=1, name="Test", email="invalid-email")

    def test_ingredient_valid(self):
        i = Ingredient(id=1, name="Tomato", stock_level=10, supplier_id=1)
        self.assertEqual(i.stock_level, 10)

    def test_ingredient_invalid_stock(self):
        with self.assertRaises(ValidationError):
            Ingredient(id=1, name="Tomato", stock_level=-5, supplier_id=1)

    def test_recipe_valid(self):
        r = Recipe(id=1, name="Soup", prep_time_mins=15)
        self.assertEqual(r.prep_time_mins, 15)

    def test_recipe_invalid_prep_time(self):
        with self.assertRaises(ValidationError):
            Recipe(id=1, name="Soup", prep_time_mins=0)

class TestManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_data.json"
        # We ensure it's removed before starting just in case
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.manager = RestaurantManager(filepath=self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_and_get_all(self):
        i = Ingredient(id=1, name="Tomato", stock_level=10, supplier_id=1)
        self.manager.add_item("ingredients", i)
        items = self.manager.get_all("ingredients")
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].name, "Tomato")

    def test_remove_item(self):
        i = Ingredient(id=1, name="Tomato", stock_level=10, supplier_id=1)
        self.manager.add_item("ingredients", i)
        self.manager.remove_item("ingredients", 1)
        items = self.manager.get_all("ingredients")
        self.assertEqual(len(items), 0)

    def test_save_and_load(self):
        s = Supplier(id=1, name="Test Supplier", email="test@test.com")
        self.manager.add_item("suppliers", s)
        self.manager.save_data()
        
        # New manager to load data
        new_manager = RestaurantManager(filepath=self.test_file)
        new_manager.load_data()
        suppliers = new_manager.get_all("suppliers")
        self.assertEqual(len(suppliers), 1)
        self.assertEqual(suppliers[0].name, "Test Supplier")

if __name__ == '__main__':
    unittest.main()