#!/usr/bin/env python3
"""
Simple Ingredients Manager for Food Detection App
Handles ingredients lists with editable quantities
"""

import json
import os
from typing import Dict, List, Optional

class IngredientsManager:
    def __init__(self):
        """
        Initialize Ingredients Manager
        """
        self.ingredients = {}
        self.load_default_ingredients()
    
    def load_default_ingredients(self):
        """
        Load default ingredients for common foods
        """
        self.ingredients = {
            'apple': [
                {'name': 'Apples', 'quantity': '2', 'unit': 'pieces'},
                {'name': 'Sugar', 'quantity': '1', 'unit': 'tbsp'},
                {'name': 'Cinnamon', 'quantity': '1', 'unit': 'tsp'},
                {'name': 'Butter', 'quantity': '1', 'unit': 'tbsp'}
            ],
            'pizza': [
                {'name': 'Pizza dough', 'quantity': '1', 'unit': 'ball'},
                {'name': 'Tomato sauce', 'quantity': '1/2', 'unit': 'cup'},
                {'name': 'Mozzarella cheese', 'quantity': '2', 'unit': 'cups'},
                {'name': 'Fresh basil', 'quantity': '10', 'unit': 'leaves'},
                {'name': 'Olive oil', 'quantity': '2', 'unit': 'tbsp'}
            ],
            'rice': [
                {'name': 'Basmati rice', 'quantity': '1', 'unit': 'cup'},
                {'name': 'Water', 'quantity': '2', 'unit': 'cups'},
                {'name': 'Salt', 'quantity': '1', 'unit': 'tsp'},
                {'name': 'Butter', 'quantity': '1', 'unit': 'tbsp'}
            ],
            'burger': [
                {'name': 'Ground beef', 'quantity': '1', 'unit': 'lb'},
                {'name': 'Burger buns', 'quantity': '4', 'unit': 'pieces'},
                {'name': 'Lettuce', 'quantity': '4', 'unit': 'leaves'},
                {'name': 'Tomato', 'quantity': '1', 'unit': 'large'},
                {'name': 'Onion', 'quantity': '1', 'unit': 'medium'},
                {'name': 'Cheese slices', 'quantity': '4', 'unit': 'slices'}
            ],
            'fries': [
                {'name': 'Potatoes', 'quantity': '4', 'unit': 'large'},
                {'name': 'Vegetable oil', 'quantity': '2', 'unit': 'tbsp'},
                {'name': 'Salt', 'quantity': '1', 'unit': 'tsp'},
                {'name': 'Black pepper', 'quantity': '1/2', 'unit': 'tsp'},
                {'name': 'Paprika', 'quantity': '1/2', 'unit': 'tsp'}
            ],
            'chapathi': [
                {'name': 'Whole wheat flour', 'quantity': '2', 'unit': 'cups'},
                {'name': 'Water', 'quantity': '3/4', 'unit': 'cup'},
                {'name': 'Salt', 'quantity': '1', 'unit': 'tsp'},
                {'name': 'Oil', 'quantity': '2', 'unit': 'tbsp'}
            ],
            'banana': [
                {'name': 'Bananas', 'quantity': '3', 'unit': 'ripe'},
                {'name': 'Flour', 'quantity': '1', 'unit': 'cup'},
                {'name': 'Sugar', 'quantity': '1/2', 'unit': 'cup'},
                {'name': 'Eggs', 'quantity': '2', 'unit': 'pieces'},
                {'name': 'Baking powder', 'quantity': '1', 'unit': 'tsp'}
            ],
            'idli': [
                {'name': 'Rice', 'quantity': '2', 'unit': 'cups'},
                {'name': 'Urad dal', 'quantity': '1', 'unit': 'cup'},
                {'name': 'Salt', 'quantity': '1', 'unit': 'tsp'},
                {'name': 'Water', 'quantity': '1', 'unit': 'cup'}
            ],
            'chicken gravy': [
                {'name': 'Chicken pieces', 'quantity': '1', 'unit': 'lb'},
                {'name': 'Onions', 'quantity': '2', 'unit': 'large'},
                {'name': 'Tomatoes', 'quantity': '3', 'unit': 'medium'},
                {'name': 'Ginger garlic paste', 'quantity': '1', 'unit': 'tbsp'},
                {'name': 'Red chili powder', 'quantity': '1', 'unit': 'tsp'},
                {'name': 'Turmeric', 'quantity': '1/2', 'unit': 'tsp'},
                {'name': 'Oil', 'quantity': '3', 'unit': 'tbsp'}
            ],
            'soda': [
                {'name': 'Carbonated water', 'quantity': '1', 'unit': 'cup'},
                {'name': 'Sugar', 'quantity': '2', 'unit': 'tbsp'},
                {'name': 'Lemon juice', 'quantity': '1', 'unit': 'tbsp'},
                {'name': 'Ice cubes', 'quantity': '4', 'unit': 'pieces'}
            ],
            'tomato': [
                {'name': 'Tomatoes', 'quantity': '4', 'unit': 'medium'},
                {'name': 'Onion', 'quantity': '1', 'unit': 'medium'},
                {'name': 'Garlic', 'quantity': '3', 'unit': 'cloves'},
                {'name': 'Olive oil', 'quantity': '2', 'unit': 'tbsp'},
                {'name': 'Salt', 'quantity': '1', 'unit': 'tsp'},
                {'name': 'Black pepper', 'quantity': '1/2', 'unit': 'tsp'}
            ],
            'vada': [
                {'name': 'Urad dal', 'quantity': '1', 'unit': 'cup'},
                {'name': 'Onions', 'quantity': '1', 'unit': 'medium'},
                {'name': 'Green chilies', 'quantity': '2', 'unit': 'pieces'},
                {'name': 'Ginger', 'quantity': '1', 'unit': 'inch'},
                {'name': 'Curry leaves', 'quantity': '10', 'unit': 'leaves'},
                {'name': 'Salt', 'quantity': '1', 'unit': 'tsp'},
                {'name': 'Oil', 'quantity': '1', 'unit': 'cup'}
            ]
        }
        print("📝 Loaded default ingredients")
    
    def get_ingredients(self, food_name: str) -> Optional[List[Dict]]:
        """
        Get ingredients list for a specific food
        
        Args:
            food_name: Name of the food item
            
        Returns:
            List of ingredients with quantities or None if not found
        """
        food_key = food_name.lower().strip()
        
        # Try exact match first
        if food_key in self.ingredients:
            return self.ingredients[food_key]
        
        # Try partial matches
        for key, ingredients in self.ingredients.items():
            if food_key in key or key in food_key:
                return ingredients
        
        return None
    
    def add_ingredients(self, food_name: str, ingredients: List[Dict]):
        """
        Add or update ingredients for a food
        
        Args:
            food_name: Name of the food
            ingredients: List of ingredient dictionaries
        """
        self.ingredients[food_name.lower().strip()] = ingredients
        print(f"✅ Added ingredients for: {food_name}")
    
    def update_quantity(self, food_name: str, ingredient_name: str, new_quantity: str):
        """
        Update quantity for a specific ingredient
        
        Args:
            food_name: Name of the food
            ingredient_name: Name of the ingredient
            new_quantity: New quantity value
        """
        food_key = food_name.lower().strip()
        if food_key in self.ingredients:
            for ingredient in self.ingredients[food_key]:
                if ingredient['name'].lower() == ingredient_name.lower():
                    ingredient['quantity'] = new_quantity
                    print(f"✅ Updated {ingredient_name} quantity to {new_quantity}")
                    return True
        return False
    
    def save_to_json(self, filename: str = "ingredients.json"):
        """
        Save ingredients to JSON file
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.ingredients, f, indent=2, ensure_ascii=False)
            print(f"💾 Saved ingredients to: {filename}")
        except Exception as e:
            print(f"❌ Error saving ingredients: {e}")
    
    def load_from_json(self, filename: str = "ingredients.json"):
        """
        Load ingredients from JSON file
        """
        try:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    self.ingredients = json.load(f)
                print(f"📖 Loaded ingredients from: {filename}")
        except Exception as e:
            print(f"❌ Error loading ingredients: {e}")
    
    def get_all_foods(self) -> List[str]:
        """
        Get list of all foods with ingredients
        """
        return list(self.ingredients.keys())

# Example usage and testing
if __name__ == "__main__":
    # Test the ingredients manager
    im = IngredientsManager()
    
    # Test getting ingredients
    ingredients = im.get_ingredients("apple")
    if ingredients:
        print(f"Ingredients for Apple:")
        for ingredient in ingredients:
            print(f"  - {ingredient['quantity']} {ingredient['unit']} {ingredient['name']}")
    
    # Test updating quantity
    im.update_quantity("apple", "Apples", "3")
    
    # Save ingredients
    im.save_to_json()
