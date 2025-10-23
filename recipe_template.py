#!/usr/bin/env python3
"""
Create Excel template for recipes
"""

import pandas as pd
import os

def create_recipe_template():
    """
    Create an Excel template for recipes
    """
    print("📝 Creating recipe template...")
    
    # Sample data for the template
    sample_recipes = [
        {
            'Food Name': 'Apple',
            'Recipe Title': 'Apple Cinnamon Oatmeal',
            'Ingredients': '1 apple, 1 cup oats, 2 cups milk, 1 tsp cinnamon, 1 tbsp honey',
            'Instructions': '1. Dice apple into small pieces. 2. Cook oats with milk for 5 minutes. 3. Add apple and cinnamon. 4. Sweeten with honey.',
            'Cooking Time': '10 minutes',
            'Difficulty Level': 'Easy',
            'Servings': '2'
        },
        {
            'Food Name': 'Pizza',
            'Recipe Title': 'Homemade Margherita Pizza',
            'Ingredients': 'Pizza dough, 1 cup tomato sauce, 2 cups mozzarella, fresh basil, olive oil',
            'Instructions': '1. Preheat oven to 450°F. 2. Roll out dough. 3. Add sauce and cheese. 4. Bake for 12-15 minutes. 5. Top with basil.',
            'Cooking Time': '25 minutes',
            'Difficulty Level': 'Medium',
            'Servings': '4'
        },
        {
            'Food Name': 'Rice',
            'Recipe Title': 'Perfect Basmati Rice',
            'Ingredients': '1 cup basmati rice, 2 cups water, 1 tsp salt, 1 tbsp butter',
            'Instructions': '1. Rinse rice until water runs clear. 2. Boil water with salt. 3. Add rice and butter. 4. Simmer covered for 15 minutes.',
            'Cooking Time': '20 minutes',
            'Difficulty Level': 'Easy',
            'Servings': '4'
        },
        {
            'Food Name': 'Burger',
            'Recipe Title': 'Classic Beef Burger',
            'Ingredients': '1 lb ground beef, 4 burger buns, lettuce, tomato, onion, cheese, ketchup, mustard',
            'Instructions': '1. Form beef into 4 patties. 2. Season with salt and pepper. 3. Grill for 4-5 minutes per side. 4. Toast buns. 5. Assemble with toppings.',
            'Cooking Time': '15 minutes',
            'Difficulty Level': 'Easy',
            'Servings': '4'
        },
        {
            'Food Name': 'Fries',
            'Recipe Title': 'Crispy French Fries',
            'Ingredients': '4 large potatoes, 2 tbsp oil, salt, pepper, paprika',
            'Instructions': '1. Cut potatoes into strips. 2. Soak in cold water for 30 minutes. 3. Pat dry and toss with oil and spices. 4. Bake at 425°F for 25-30 minutes.',
            'Cooking Time': '45 minutes',
            'Difficulty Level': 'Easy',
            'Servings': '4'
        }
    ]
    
    # Create DataFrame
    df = pd.DataFrame(sample_recipes)
    
    # Save to Excel
    template_file = "recipe_template.xlsx"
    df.to_excel(template_file, index=False, engine='openpyxl')
    
    print(f"✅ Recipe template created: {template_file}")
    print("\n📋 Template format:")
    print("Column A: Food Name")
    print("Column B: Recipe Title") 
    print("Column C: Ingredients")
    print("Column D: Instructions")
    print("Column E: Cooking Time")
    print("Column F: Difficulty Level")
    print("Column G: Servings")
    
    print(f"\n📝 Instructions:")
    print("1. Open the Excel file")
    print("2. Add your own recipes following the format")
    print("3. Save the file")
    print("4. Upload it to the web app")
    
    return template_file

if __name__ == "__main__":
    create_recipe_template()
