#!/usr/bin/env python3
"""
Food Detection Web App
A simple Flask web application for food detection using your trained YOLOv8 model
"""

from flask import Flask, render_template, request, jsonify, send_from_directory
from ultralytics import YOLO
import cv2
import numpy as np
import os
import base64
from io import BytesIO
from PIL import Image
from ingredients_manager import IngredientsManager

app = Flask(__name__)

# Load the trained model
model = YOLO("best.pt")

# Load ingredients manager
ingredients_manager = IngredientsManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_food():
    try:
        print("Received request for food detection")
        print("Files in request:", list(request.files.keys()))
        
        # Get the uploaded image
        if 'image' not in request.files:
            print("No 'image' key in request.files")
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['image']
        print(f"File received: {file.filename}")
        
        if file.filename == '':
            print("Empty filename")
            return jsonify({'error': 'No image selected'}), 400
        
        # Read and process the image
        image = Image.open(file.stream)
        image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        # Run inference
        results = model(image_cv)
        
        # Process results
        detections = []
        ingredients_list = []
        
        for r in results:
            for box in r.boxes:
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                class_name = model.names[class_id]
                
                # Get bounding box coordinates
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                
                detections.append({
                    'class': class_name,
                    'confidence': round(confidence, 2),
                    'bbox': [int(x1), int(y1), int(x2), int(y2)]
                })
                
                # Get ingredients for this food
                ingredients = ingredients_manager.get_ingredients(class_name)
                if ingredients:
                    ingredients_list.append({
                        'food': class_name,
                        'ingredients': ingredients
                    })
        
        # Create annotated image
        annotated_image = results[0].plot()
        annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
        
        # Convert to base64 for web display
        pil_image = Image.fromarray(annotated_image_rgb)
        buffer = BytesIO()
        pil_image.save(buffer, format='JPEG')
        img_str = base64.b64encode(buffer.getvalue()).decode()
        
        return jsonify({
            'detections': detections,
            'annotated_image': img_str,
            'count': len(detections),
            'ingredients': ingredients_list
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'model_loaded': True})

@app.route('/ingredients')
def get_all_ingredients():
    """Get all available foods with ingredients"""
    return jsonify({
        'foods': ingredients_manager.get_all_foods(),
        'count': len(ingredients_manager.ingredients)
    })

@app.route('/ingredients/<food_name>')
def get_ingredients(food_name):
    """Get ingredients for specific food"""
    ingredients = ingredients_manager.get_ingredients(food_name)
    if ingredients:
        return jsonify({'food': food_name, 'ingredients': ingredients})
    else:
        return jsonify({'error': f'No ingredients found for {food_name}'}), 404

@app.route('/ingredients', methods=['POST'])
def update_ingredients():
    """Update ingredients for a food"""
    try:
        data = request.json
        food_name = data.get('food_name')
        ingredients = data.get('ingredients')
        
        if not food_name or not ingredients:
            return jsonify({'error': 'food_name and ingredients are required'}), 400
        
        ingredients_manager.add_ingredients(food_name, ingredients)
        return jsonify({'message': f'Ingredients updated for {food_name}'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/ingredients/quantity', methods=['POST'])
def update_quantity():
    """Update quantity for a specific ingredient"""
    try:
        data = request.json
        food_name = data.get('food_name')
        ingredient_name = data.get('ingredient_name')
        new_quantity = data.get('quantity')
        
        if not all([food_name, ingredient_name, new_quantity]):
            return jsonify({'error': 'food_name, ingredient_name, and quantity are required'}), 400
        
        success = ingredients_manager.update_quantity(food_name, ingredient_name, new_quantity)
        if success:
            return jsonify({'message': f'Quantity updated for {ingredient_name}'})
        else:
            return jsonify({'error': f'Ingredient {ingredient_name} not found for {food_name}'}), 404
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)
