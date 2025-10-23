#!/usr/bin/env python3
"""
Food Detection Model Testing Script
Use your trained YOLOv8 model to detect food in new images
"""

from ultralytics import YOLO
import cv2
import os

def test_food_detection(image_path, model_path="best.pt"):
    """
    Test food detection on a single image
    
    Args:
        image_path (str): Path to the image file
        model_path (str): Path to the trained model (default: best.pt)
    """
    # Load the trained model
    model = YOLO(model_path)
    
    # Run inference
    results = model(image_path)
    
    # Display results
    for r in results:
        # Show the image with predictions
        im_array = r.plot()  # plot a BGR numpy array of predictions
        cv2.imshow("Food Detection", im_array)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Print detection details
        print(f"Detected {len(r.boxes)} food items:")
        for box in r.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            class_name = model.names[class_id]
            print(f"  - {class_name}: {confidence:.2f}")

def batch_test_images(folder_path, model_path="best.pt"):
    """
    Test food detection on all images in a folder
    
    Args:
        folder_path (str): Path to folder containing images
        model_path (str): Path to the trained model
    """
    model = YOLO(model_path)
    
    # Get all image files
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    image_files = [f for f in os.listdir(folder_path) 
                   if f.lower().endswith(image_extensions)]
    
    print(f"Found {len(image_files)} images to process...")
    
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        print(f"\nProcessing: {image_file}")
        
        results = model(image_path)
        for r in results:
            print(f"Detected {len(r.boxes)} food items in {image_file}")
            for box in r.boxes:
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                class_name = model.names[class_id]
                print(f"  - {class_name}: {confidence:.2f}")

if __name__ == "__main__":
    # Example usage:
    
    # Test on a single image
    # test_food_detection("path/to/your/image.jpg")
    
    # Test on all images in a folder
    # batch_test_images("path/to/your/images/folder")
    
    # Test on your existing test dataset
    batch_test_images("dataset/images/test")
