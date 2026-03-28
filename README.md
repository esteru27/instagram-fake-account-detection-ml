# Instagram Fake Account Detection

A Streamlit web application that classifies Instagram accounts as REAL or FAKE using machine learning.

## 🌐 Live Demo
https://instagram-fake-account-detection-ml-tgrga39pieqsbalpu6ye4a.streamlit.app/

## 🚀 Features
- Detects fake or real Instagram accounts
- Uses profile features such as:
  - Followers
  - Following
  - Bio information
- Simple and interactive user interface

## 🛠️ Technologies Used
- Python
- Streamlit
- Scikit-learn
- Pandas

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

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the app:
```
streamlit run app.py
```

## 📊 Output
- REAL Account ✅  
- FAKE Account ❌  

## 🔮 Future Improvements
- Improve model accuracy
- Add more features (engagement rate, posts analysis)
- Enhance UI design

## 📄 License
MIT License
