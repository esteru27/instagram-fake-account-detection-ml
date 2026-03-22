import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("dataset/instagram_fake_accounts.csv")

X = data.drop("fake", axis=1)
y = data["fake"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

st.title("Instagram Fake Account Detection")

followers = st.number_input("Followers")
following = st.number_input("Following")
posts = st.number_input("Posts")
profile_pic = st.selectbox("Profile Picture (1 = Yes, 0 = No)", [0,1])
bio_length = st.number_input("Bio Length")

if st.button("Check Account"):
    
    result = model.predict([[followers, following, posts, profile_pic, bio_length]])

    if result[0] == 1:
        st.error("This account is likely FAKE")
    else:
        st.success("This account is likely REAL")