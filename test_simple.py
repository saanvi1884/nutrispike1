#!/usr/bin/env python3
"""
Simple test script to verify the food detection model works
"""

from ultralytics import YOLO
import cv2
import os

def test_model():
    print("Loading model...")
    model = YOLO("best.pt")
    print("Model loaded successfully!")
    
    # Test on one of the test images
    test_image_path = "dataset/images/test/1_jpg.rf.13c4c9afbe207034512c537dfac2c12d.jpg"
    
    if os.path.exists(test_image_path):
        print(f"Testing on: {test_image_path}")
        results = model(test_image_path)
        
        print(f"Detected {len(results[0].boxes)} food items:")
        for box in results[0].boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            class_name = model.names[class_id]
            print(f"  - {class_name}: {confidence:.2f}")
        
        # Save the result
        results[0].save("test_result.jpg")
        print("Result saved as test_result.jpg")
    else:
        print("Test image not found, trying to find any test image...")
        test_dir = "dataset/images/test"
        if os.path.exists(test_dir):
            images = [f for f in os.listdir(test_dir) if f.endswith('.jpg')]
            if images:
                test_image = os.path.join(test_dir, images[0])
                print(f"Testing on: {test_image}")
                results = model(test_image)
                
                print(f"Detected {len(results[0].boxes)} food items:")
                for box in results[0].boxes:
                    class_id = int(box.cls[0])
                    confidence = float(box.conf[0])
                    class_name = model.names[class_id]
                    print(f"  - {class_name}: {confidence:.2f}")
                
                results[0].save("test_result.jpg")
                print("Result saved as test_result.jpg")
            else:
                print("No test images found")
        else:
            print("Test directory not found")

if __name__ == "__main__":
    test_model()
