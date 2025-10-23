# 🍽️ Data Preparation Guide for New Food Classes

## 📋 Step-by-Step Process

### 1. **Collect Images** 📸
- Take **at least 50-100 photos** of each new food item
- Include different angles, lighting, and backgrounds
- Show the food in various states (whole, cut, cooked, etc.)
- Use good quality images (at least 640x640 pixels)

### 2. **Create Labels** 🏷️
For each image, you need to create a corresponding `.txt` file with bounding box coordinates.

**Label Format:**
```
class_id center_x center_y width height
```

**Example for a pizza image:**
```
0 0.5 0.5 0.8 0.6
```

### 3. **Organize Your Data** 📁
```
new_food_dataset/
├── images/
│   ├── train/          # 70% of your images
│   ├── valid/          # 20% of your images  
│   └── test/           # 10% of your images
└── labels/
    ├── train/          # Corresponding label files
    ├── valid/
    └── test/
```

### 4. **Labeling Tools** 🛠️

#### **Option A: Roboflow (Recommended)**
1. Go to [roboflow.com](https://roboflow.com)
2. Create a new project
3. Upload your images
4. Draw bounding boxes around food items
5. Export in YOLO format

#### **Option B: LabelImg (Free)**
1. Install: `pip install labelImg`
2. Run: `labelImg`
3. Open your images
4. Draw bounding boxes
5. Save as YOLO format

#### **Option C: CVAT (Advanced)**
1. Install CVAT server
2. Create project and tasks
3. Annotate images
4. Export in YOLO format

### 5. **Class ID Mapping** 🔢

Your current classes and their IDs:
```
0: Apple
1: Chapathi  
2: Chicken Gravy
3: Fries
4: Idli
5: Pizza
6: Rice
7: Soda
8: Tomato
9: Vada
10: banana
11: burger
```

**New classes will get IDs:**
```
12: [Your first new food]
13: [Your second new food]
... and so on
```

### 6. **Quality Checklist** ✅

- [ ] At least 50 images per new food class
- [ ] Images show food from different angles
- [ ] Good lighting and clear visibility
- [ ] Bounding boxes tightly around food items
- [ ] No overlapping bounding boxes
- [ ] Consistent labeling across all images
- [ ] Proper train/valid/test split (70/20/10)

### 7. **Example Workflow** 🔄

1. **Take photos** of your new food items
2. **Upload to Roboflow** or use LabelImg
3. **Draw bounding boxes** around each food item
4. **Export labels** in YOLO format
5. **Organize files** in the correct folder structure
6. **Run the retraining script**

### 8. **Tips for Better Results** 💡

- **Diverse backgrounds**: Kitchen, restaurant, home, outdoor
- **Different lighting**: Natural light, artificial light, dim lighting
- **Various states**: Fresh, cooked, partially eaten, different sizes
- **Multiple angles**: Top view, side view, close-up, far away
- **Real-world scenarios**: Plates, bowls, hands holding food

### 9. **Common Mistakes to Avoid** ❌

- Too few images per class (< 30)
- Poor quality or blurry images
- Inconsistent bounding box sizes
- Missing labels for some food items
- Wrong class IDs in label files
- Imbalanced dataset (some classes have way more images)

### 10. **Validation** 🔍

Before training, verify:
- [ ] All images have corresponding label files
- [ ] Label files have correct format
- [ ] Class IDs are correct
- [ ] Train/valid/test split is proper
- [ ] No missing or corrupted files

## 🚀 Ready to Start?

1. **Collect your food images**
2. **Label them using Roboflow or LabelImg**
3. **Organize in the correct folder structure**
4. **Run the retraining script**

Need help with any step? Just ask! 🤝
