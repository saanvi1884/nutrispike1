#!/usr/bin/env python3
"""
Train Custom Food Detection Model
Train your model with custom food classes
"""

from ultralytics import YOLO
import os
import time

def train_custom_model():
    """
    Train the model with custom dataset
    """
    print("🚀 Starting Custom Food Detection Training")
    print("=" * 50)
    
    # Check if config file exists
    config_file = "custom_food_config.yaml"
    if not os.path.exists(config_file):
        print(f"❌ Configuration file not found: {config_file}")
        print("Please run custom_dataset_setup.py first!")
        return
    
    # Load the existing trained model as starting point
    print("📦 Loading existing model as starting point...")
    model = YOLO("best.pt")
    
    print("🎯 Starting training with custom foods...")
    print("⏱️ This may take 1-3 hours depending on your data size...")
    
    # Start training
    start_time = time.time()
    
    try:
        results = model.train(
            data=config_file,
            epochs=100,
            imgsz=640,
            batch=16,
            patience=20,
            save=True,
            project="custom_food_detection",
            name="custom_foods",
            exist_ok=True,
            pretrained=True,  # Use existing weights as starting point
            optimizer='AdamW',
            lr0=0.01,
            weight_decay=0.0005,
            warmup_epochs=3,
            warmup_momentum=0.8,
            warmup_bias_lr=0.1,
            box=7.5,
            cls=0.5,
            dfl=1.5,
            pose=12.0,
            kobj=2.0,
            label_smoothing=0.0,
            nbs=64,
            overlap_mask=True,
            mask_ratio=4,
            drop_path=0.0,
            plots=True,
            val=True,
            save_period=10
        )
        
        end_time = time.time()
        training_time = (end_time - start_time) / 60  # Convert to minutes
        
        print(f"\n✅ Training completed successfully!")
        print(f"⏱️ Training time: {training_time:.1f} minutes")
        print(f"📁 Results saved in: custom_food_detection/custom_foods/")
        
        # Show best model path
        best_model = "custom_food_detection/custom_foods/weights/best.pt"
        if os.path.exists(best_model):
            print(f"🏆 Best model saved as: {best_model}")
            
            # Test the new model
            print(f"\n🧪 Testing the new model...")
            test_model = YOLO(best_model)
            
            # Test on a sample image if available
            test_images = []
            for split in ['test', 'valid', 'train']:
                test_dir = f"custom_food_dataset/images/{split}"
                if os.path.exists(test_dir):
                    images = [f for f in os.listdir(test_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
                    if images:
                        test_images.append(os.path.join(test_dir, images[0]))
                        break
            
            if test_images:
                print(f"📸 Testing on: {test_images[0]}")
                results = test_model(test_images[0])
                
                print(f"🔍 Detection results:")
                for r in results:
                    for box in r.boxes:
                        class_id = int(box.cls[0])
                        confidence = float(box.conf[0])
                        class_name = test_model.names[class_id]
                        print(f"  - {class_name}: {confidence:.2f}")
                
                # Save test result
                results[0].save("custom_test_result.jpg")
                print(f"💾 Test result saved as: custom_test_result.jpg")
        
        return results
        
    except Exception as e:
        print(f"❌ Training failed: {str(e)}")
        return None

def update_web_app():
    """
    Update the web app to use the new model
    """
    print(f"\n🌐 Updating web application...")
    
    # Backup current model
    if os.path.exists("best.pt"):
        os.rename("best.pt", "best_backup.pt")
        print("💾 Backed up original model as: best_backup.pt")
    
    # Copy new model
    new_model = "custom_food_detection/custom_foods/weights/best.pt"
    if os.path.exists(new_model):
        import shutil
        shutil.copy2(new_model, "best.pt")
        print("✅ Updated web app with new model")
        print("🔄 Restart your web app to use the new model!")
    else:
        print("❌ New model not found")

def main():
    print("🍽️ CUSTOM FOOD DETECTION TRAINING")
    print("=" * 50)
    
    # Check if custom dataset exists
    if not os.path.exists("custom_food_dataset"):
        print("❌ Custom dataset not found!")
        print("Please run custom_dataset_setup.py first to prepare your data.")
        return
    
    # Check if user has added their custom data
    custom_images = []
    for split in ['train', 'valid', 'test']:
        custom_dir = f"custom_food_dataset/images/{split}"
        if os.path.exists(custom_dir):
            images = [f for f in os.listdir(custom_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
            custom_images.extend(images)
    
    if len(custom_images) <= 704:  # Only existing dataset
        print("⚠️  No custom food images detected!")
        print("Please add your custom food images to:")
        print("  - custom_food_dataset/images/train/")
        print("  - custom_food_dataset/images/valid/")
        print("  - custom_food_dataset/labels/train/")
        print("  - custom_food_dataset/labels/valid/")
        print("\nThen run this script again.")
        return
    
    print(f"✅ Found {len(custom_images)} images in custom dataset")
    
    # Ask user if they want to start training
    start_training = input("\n🚀 Start training now? (y/n): ").lower().strip()
    if start_training != 'y':
        print("📝 Ready to train when you are! Run this script again when ready.")
        return
    
    # Start training
    results = train_custom_model()
    
    if results:
        # Ask if user wants to update web app
        update_app = input("\n🌐 Update web app with new model? (y/n): ").lower().strip()
        if update_app == 'y':
            update_web_app()

if __name__ == "__main__":
    main()
