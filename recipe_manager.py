#!/usr/bin/env python3
"""
Recipe Manager for Food Detection App
Handles recipe database and provides recipes for detected foods
"""

import pandas as pd
import json
import os
from typing import Dict, List, Optional

class RecipeManager:
    def __init__(self, excel_file: str = None):
        """
        Initialize Recipe Manager
        
        Args:
            excel_file: Path to Excel file with recipes
        """
        self.recipes = {}
        self.excel_file = excel_file
        
        if excel_file and os.path.exists(excel_file):
            self.load_from_excel(excel_file)
        else:
            self.load_default_recipes()
    
    def load_from_excel(self, excel_file: str):
        """
        Load recipes from Excel file
        
        Expected Excel format:
        - Column A: Food Name
        - Column B: Recipe Title
        - Column C: Ingredients
        - Column D: Instructions
        - Column E: Cooking Time
        - Column F: Difficulty Level
        - Column G: Servings
        """
        try:
            print(f"📖 Loading recipes from: {excel_file}")
            
            # Read Excel file
            df = pd.read_excel(excel_file)
            
            # Process each row
            for index, row in df.iterrows():
                food_name = str(row.iloc[0]).strip().lower()  # Food name
                recipe_title = str(row.iloc[1]).strip() if pd.notna(row.iloc[1]) else f"{food_name.title()} Recipe"
                ingredients = str(row.iloc[2]).strip() if pd.notna(row.iloc[2]) else "Ingredients not specified"
                instructions = str(row.iloc[3]).strip() if pd.notna(row.iloc[3]) else "Instructions not provided"
                cooking_time = str(row.iloc[4]).strip() if pd.notna(row.iloc[4]) else "Not specified"
                difficulty = str(row.iloc[5]).strip() if pd.notna(row.iloc[5]) else "Medium"
                servings = str(row.iloc[6]).strip() if pd.notna(row.iloc[6]) else "4"
                
                # Store recipe
                self.recipes[food_name] = {
                    'title': recipe_title,
                    'ingredients': ingredients,
                    'instructions': instructions,
                    'cooking_time': cooking_time,
                    'difficulty': difficulty,
                    'servings': servings
                }
            
            print(f"✅ Loaded {len(self.recipes)} recipes from Excel")
            
        except Exception as e:
            print(f"❌ Error loading Excel file: {e}")
            print("📝 Using default recipes instead")
            self.load_default_recipes()
    
    def load_default_recipes(self):
        """
        Load default recipes for common foods
        """
        self.recipes = {
            'apple': {
                'title': 'Apple Cinnamon Oatmeal',
                'ingredients': '1 apple, 1 cup oats, 2 cups milk, 1 tsp cinnamon, 1 tbsp honey',
                'instructions': '1. Dice apple into small pieces. 2. Cook oats with milk for 5 minutes. 3. Add apple and cinnamon. 4. Sweeten with honey.',
                'cooking_time': '10 minutes',
                'difficulty': 'Easy',
                'servings': '2'
            },
            'pizza': {
                'title': 'Homemade Margherita Pizza',
                'ingredients': 'Pizza dough, 1 cup tomato sauce, 2 cups mozzarella, fresh basil, olive oil',
                'instructions': '1. Preheat oven to 450°F. 2. Roll out dough. 3. Add sauce and cheese. 4. Bake for 12-15 minutes. 5. Top with basil.',
                'cooking_time': '25 minutes',
                'difficulty': 'Medium',
                'servings': '4'
            },
            'rice': {
                'title': 'Perfect Basmati Rice',
                'ingredients': '1 cup basmati rice, 2 cups water, 1 tsp salt, 1 tbsp butter',
                'instructions': '1. Rinse rice until water runs clear. 2. Boil water with salt. 3. Add rice and butter. 4. Simmer covered for 15 minutes.',
                'cooking_time': '20 minutes',
                'difficulty': 'Easy',
                'servings': '4'
            },
            'burger': {
                'title': 'Classic Beef Burger',
                'ingredients': '1 lb ground beef, 4 burger buns, lettuce, tomato, onion, cheese, ketchup, mustard',
                'instructions': '1. Form beef into 4 patties. 2. Season with salt and pepper. 3. Grill for 4-5 minutes per side. 4. Toast buns. 5. Assemble with toppings.',
                'cooking_time': '15 minutes',
                'difficulty': 'Easy',
                'servings': '4'
            },
            'fries': {
                'title': 'Crispy French Fries',
                'ingredients': '4 large potatoes, 2 tbsp oil, salt, pepper, paprika',
                'instructions': '1. Cut potatoes into strips. 2. Soak in cold water for 30 minutes. 3. Pat dry and toss with oil and spices. 4. Bake at 425°F for 25-30 minutes.',
                'cooking_time': '45 minutes',
                'difficulty': 'Easy',
                'servings': '4'
            }
        }
        print("📝 Loaded default recipes")
    
    def get_recipe(self, food_name: str) -> Optional[Dict]:
        """
        Get recipe for a specific food
        
        Args:
            food_name: Name of the food item
            
        Returns:
            Recipe dictionary or None if not found
        """
        food_key = food_name.lower().strip()
        
        # Try exact match first
        if food_key in self.recipes:
            return self.recipes[food_key]
        
        # Try partial matches
        for key, recipe in self.recipes.items():
            if food_key in key or key in food_key:
                return recipe
        
        # Try common variations
        variations = {
            'chapathi': 'chapati',
            'chicken gravy': 'chicken',
            'banana': 'banana',
            'tomato': 'tomato',
            'vada': 'vada',
            'idli': 'idli',
            'soda': 'soda'
        }
        
        for food, variation in variations.items():
            if food_key == food or food_key == variation:
                if variation in self.recipes:
                    return self.recipes[variation]
        
        return None
    
    def add_recipe(self, food_name: str, recipe: Dict):
        """
        Add or update a recipe
        
        Args:
            food_name: Name of the food
            recipe: Recipe dictionary
        """
        self.recipes[food_name.lower().strip()] = recipe
        print(f"✅ Added recipe for: {food_name}")
    
    def save_to_json(self, filename: str = "recipes.json"):
        """
        Save recipes to JSON file
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.recipes, f, indent=2, ensure_ascii=False)
            print(f"💾 Saved recipes to: {filename}")
        except Exception as e:
            print(f"❌ Error saving recipes: {e}")
    
    def load_from_json(self, filename: str = "recipes.json"):
        """
        Load recipes from JSON file
        """
        try:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    self.recipes = json.load(f)
                print(f"📖 Loaded recipes from: {filename}")
        except Exception as e:
            print(f"❌ Error loading recipes: {e}")
    
    def get_all_foods(self) -> List[str]:
        """
        Get list of all foods with recipes
        """
        return list(self.recipes.keys())
    
    def search_recipes(self, query: str) -> List[Dict]:
        """
        Search recipes by query
        
        Args:
            query: Search query
            
        Returns:
            List of matching recipes
        """
        query = query.lower().strip()
        results = []
        
        for food, recipe in self.recipes.items():
            if (query in food or 
                query in recipe['title'].lower() or 
                query in recipe['ingredients'].lower() or 
                query in recipe['instructions'].lower()):
                results.append({'food': food, 'recipe': recipe})
        
        return results

# Example usage and testing
if __name__ == "__main__":
    # Test the recipe manager
    rm = RecipeManager()
    
    # Test getting a recipe
    recipe = rm.get_recipe("apple")
    if recipe:
        print(f"Recipe for Apple: {recipe['title']}")
        print(f"Ingredients: {recipe['ingredients']}")
    
    # Test adding a new recipe
    rm.add_recipe("pasta", {
        'title': 'Spaghetti Carbonara',
        'ingredients': 'Spaghetti, eggs, parmesan, bacon, black pepper',
        'instructions': '1. Cook pasta. 2. Fry bacon. 3. Mix eggs and cheese. 4. Combine all ingredients.',
        'cooking_time': '20 minutes',
        'difficulty': 'Medium',
        'servings': '4'
    })
    
    # Save recipes
    rm.save_to_json()
