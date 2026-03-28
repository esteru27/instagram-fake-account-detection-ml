# Instagram Fake Account Detection

A Streamlit web application that classifies Instagram accounts as REAL or FAKE using machine learning.

## 🌐 Live Demo
https://instagram-fake-account-detection-ml-tgrga39pieqsbalpu6ye4a.streamlit.app/

## 🚀 Features
- Detects fake or real Instagram accounts  
- Uses profile features such as:
  - Followers  
  - Following  
  - Posts  
  - Bio information  
- Simple and interactive user interface  
- Instant prediction results  

## 🧠 Model Information
- Model Used: Random Forest Classifier  
- Library: Scikit-learn  
- Accuracy: ~90% (depends on dataset split)  

## 📊 Dataset
- File: `instagram_fake_accounts.csv`  
- Contains features like:
  - Followers  
  - Following  
  - Posts  
  - Bio length  
  - Profile information  
- Used for training and testing the model  

## ⚙️ How It Works
1. User enters Instagram profile details  
2. The trained machine learning model processes the input  
3. The app predicts whether the account is:
   - REAL ✅  
   - FAKE ❌  

## 🛠️ Technologies Used
- Python  
- Pandas  
- Scikit-learn  
- Streamlit  

## 📂 Project Structure
```
instagram-fake-account-detection-ml/
│
├── app.py
├── train_model.py
├── dataset/
│   └── instagram_fake_accounts.csv
├── requirements.txt
└── README.md
```

## ▶️ How to Run

**1. Install dependencies**
```
pip install -r requirements.txt
```

**2. Run the app**
```
streamlit run app.py
```

## 📊 Output
- REAL Account ✅  
- FAKE Account ❌  


## 🔮 Future Improvements
- Improve model accuracy  
- Add more features (engagement rate, comments, likes)  
- Enhance UI design  

## 📄 License
MIT License
