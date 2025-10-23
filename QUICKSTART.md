# 🍽️ Food Detection - Quick Start Guide

Your YOLOv8 food detection model is ready to use! Here are the different ways you can use it:

## 🚀 Option 1: Test Your Model (Python Script)

```bash
# Install dependencies
pip install -r requirements.txt

# Test on a single image
python test_model.py

# Or modify the script to test on your own images
```

## 🌐 Option 2: Web Application

```bash
# Install dependencies
pip install -r requirements.txt

# Run the web app
python app.py

# Open your browser and go to: http://localhost:5000
```

## 📊 Option 3: Analyze Your Training Results

Your model has already been trained! Check out the results in the `Results/` folder:
- `confusion_matrix.png` - Shows how well your model performs on each food class
- `F1_curve.png` - F1 score performance
- `PR_curve.png` - Precision-Recall curve
- `val_batch*_pred.jpg` - Sample predictions on validation data

## 🎯 What Your Model Can Detect

Your trained model can identify these 12 food items:
- Apple
- Chapathi  
- Chicken Gravy
- Fries
- Idli
- Pizza
- Rice
- Soda
- Tomato
- Vada
- Banana
- Burger

## 📈 Model Performance

Based on your training results, you can see:
- How accurate the model is for each food type
- Which foods it detects best
- Areas where it might need improvement

## 🔧 Next Steps

1. **Test on new images** - Try the web app or Python script
2. **Improve the model** - If needed, you can retrain with more data
3. **Deploy** - Use the web app for real-world applications
4. **Integrate** - Use the Python script in your own applications

## 🆘 Need Help?

- Check the `README.md` for detailed setup instructions
- Look at the Jupyter notebook `yolov8_training.ipynb` to see how the model was trained
- The model file `best.pt` contains your trained weights

Happy food detecting! 🎉
