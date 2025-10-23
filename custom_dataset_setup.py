#!/usr/bin/env python3
"""
Custom Dataset Setup for Food Detection
Add your own food images and labels to the existing model
"""

import os
import shutil
import yaml
from pathlib import Path

def setup_custom_dataset():
    """
    Set up the directory structure for your custom dataset
    """
    print("🍽️ Setting up custom dataset structure...")
    
    # Create new dataset directory
    custom_dir = "custom_food_dataset"
    
    # Create directory structure
    directories = [
        f"{custom_dir}/images/train",
        f"{custom_dir}/images/valid", 
        f"{custom_dir}/images/test",
        f"{custom_dir}/labels/train",
        f"{custom_dir}/labels/valid",
        f"{custom_dir}/labels/test"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created: {directory}")
    
    return custom_dir

def copy_existing_dataset(custom_dir):
    """
    Copy existing dataset to new structure
    """
    print("\n📁 Copying existing dataset...")
    
    # Copy existing images and labels
    for split in ['train', 'valid', 'test']:
        # Copy images
        src_images = f"dataset/images/{split}"
        dst_images = f"{custom_dir}/images/{split}"
        
        if os.path.exists(src_images):
            for file in os.listdir(src_images):
                if file.endswith(('.jpg', '.jpeg', '.png')):
                    shutil.copy2(f"{src_images}/{file}", f"{dst_images}/{file}")
            print(f"✅ Copied images from {split}")
        
        # Copy labels
        src_labels = f"dataset/labels/{split}"
        dst_labels = f"{custom_dir}/labels/{split}"
        
        if os.path.exists(src_labels):
            for file in os.listdir(src_labels):
                if file.endswith('.txt'):
                    shutil.copy2(f"{src_labels}/{file}", f"{dst_labels}/{file}")
            print(f"✅ Copied labels from {split}")

def get_custom_foods():
    """
    Get custom food classes from user
    """
    print("\n🍽️ Current food classes in your model:")
    current_classes = ['Apple', 'Chapathi', 'Chicken Gravy', 'Fries', 'Idli', 'Pizza', 'Rice', 'Soda', 'Tomato', 'Vada', 'banana', 'burger']
    
    for i, food in enumerate(current_classes, 1):
        print(f"{i:2d}. {food}")
    
    print("\n➕ Add your custom food classes:")
    print("Enter the names of new foods you want to detect (comma-separated)")
    print("Example: 'Pasta, Sandwich, Salad, Soup, Cake'")
    
    new_foods_input = input("\nYour custom foods: ").strip()
    
    if not new_foods_input:
        print("❌ No custom foods specified.")
        return []
    
    # Parse custom food classes
    custom_foods = [food.strip() for food in new_foods_input.split(',') if food.strip()]
    print(f"\n✅ Adding {len(custom_foods)} custom foods: {custom_foods}")
    
    return custom_foods

def create_custom_config(custom_foods, dataset_path):
    """
    Create YAML configuration for custom dataset
    """
    # Current 12 classes + new custom classes
    current_classes = ['Apple', 'Chapathi', 'Chicken Gravy', 'Fries', 'Idli', 'Pizza', 'Rice', 'Soda', 'Tomato', 'Vada', 'banana', 'burger']
    all_classes = current_classes + custom_foods
    total_classes = len(all_classes)
    
    config_content = f"""# Custom Food Detection Dataset Configuration
path: "{os.path.abspath(dataset_path)}"

# Dataset paths
train: images/train
val: images/valid
test: images/test

# Number of classes
nc: {total_classes}

# Class names
names: {all_classes}

# Training parameters
epochs: 100
batch: 16
imgsz: 640
patience: 20
save_period: 10

# Data augmentation
hsv_h: 0.015
hsv_s: 0.7
hsv_v: 0.4
degrees: 0.0
translate: 0.1
scale: 0.5
shear: 0.0
perspective: 0.0
flipud: 0.0
fliplr: 0.5
mosaic: 1.0
mixup: 0.0
copy_paste: 0.0
"""
    
    config_file = "custom_food_config.yaml"
    with open(config_file, "w") as f:
        f.write(config_content)
    
    print(f"\n📝 Created configuration file: {config_file}")
    print(f"📊 Total classes: {total_classes}")
    print(f"🍽️ All food classes: {all_classes}")
    
    return config_file

def show_data_requirements(custom_foods, dataset_path):
    """
    Show user what data they need to prepare
    """
    print(f"\n📋 DATA REQUIREMENTS FOR YOUR CUSTOM FOODS:")
    print("=" * 60)
    
    for i, food in enumerate(custom_foods, 1):
        class_id = 11 + i  # Starting from ID 12 (after existing 12 classes)
        print(f"\n{i}. {food} (Class ID: {class_id})")
        print(f"   📸 Images needed: 50-100 photos")
        print(f"   📁 Add to: {dataset_path}/images/train/")
        print(f"   🏷️ Labels to: {dataset_path}/labels/train/")
        print(f"   📝 Label format: {class_id} center_x center_y width height")
    
    print(f"\n📁 FOLDER STRUCTURE:")
    print(f"{dataset_path}/")
    print("├── images/")
    print("│   ├── train/     # 70% of your images")
    print("│   ├── valid/     # 20% of your images")
    print("│   └── test/      # 10% of your images")
    print("└── labels/")
    print("    ├── train/     # Corresponding .txt files")
    print("    ├── valid/")
    print("    └── test/")
    
    print(f"\n🛠️ LABELING TOOLS:")
    print("1. Roboflow (easiest): https://roboflow.com")
    print("2. LabelImg (free): pip install labelImg")
    print("3. CVAT (advanced): https://cvat.org")
    
    print(f"\n📝 LABEL FILE FORMAT:")
    print("Each image needs a .txt file with same name")
    print("Format: class_id center_x center_y width height")
    print("Example: 12 0.5 0.5 0.8 0.6  # Custom food at center")

def main():
    print("🍽️ CUSTOM FOOD DATASET SETUP")
    print("=" * 50)
    
    # Step 1: Setup directory structure
    dataset_path = setup_custom_dataset()
    
    # Step 2: Copy existing dataset
    copy_existing_dataset(dataset_path)
    
    # Step 3: Get custom foods from user
    custom_foods = get_custom_foods()
    
    if not custom_foods:
        print("❌ No custom foods specified. Exiting.")
        return
    
    # Step 4: Create configuration
    config_file = create_custom_config(custom_foods, dataset_path)
    
    # Step 5: Show requirements
    show_data_requirements(custom_foods, dataset_path)
    
    print(f"\n🚀 NEXT STEPS:")
    print("1. 📸 Take photos of your custom foods")
    print("2. 🏷️ Label them using Roboflow or LabelImg")
    print("3. 📁 Add images and labels to the folders above")
    print("4. 🚀 Run the training script when ready")
    
    print(f"\n📁 Your dataset is ready at: {dataset_path}")
    print(f"📝 Configuration saved as: {config_file}")

if __name__ == "__main__":
    main()
