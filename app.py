import streamlit as st

st.title("Instagram Account Detection")

# Inputs
followers = st.number_input("Followers", min_value=0)
following = st.number_input("Following", min_value=0)
bio = st.selectbox("Has Bio?", ["Yes", "No"])
profile_pic = st.selectbox("Has Profile Picture?", ["Yes", "No"])
highlights = st.selectbox("Has Highlights?", ["Yes", "No"])
account_type = st.selectbox("Account Type", ["Public", "Private"])

# Convert
bio = 1 if bio == "Yes" else 0
profile_pic = 1 if profile_pic == "Yes" else 0
highlights = 1 if highlights == "Yes" else 0
public = 1 if account_type == "Public" else 0

# Button
if st.button("Check Account"):

    diff = abs(followers - following)

    # --- NEW ACCOUNT ---
    if followers < 50 and following < 50 and bio == 0 and highlights == 0 and public == 0:
        st.warning("This is likely a NEW account ⚠️")

    # --- FAKE ACCOUNT ---
    elif (bio == 0 and profile_pic == 0 and 
          (followers < 50 or followers > 1000 or diff > 500)):
        st.error("This account is likely FAKE ❌")

    # --- REAL ACCOUNT ---
    else:
        if bio == 1 and profile_pic == 1 and diff <= 100:
            st.success("This account is likely REAL ✅")
        else:
            st.info("This account appears NORMAL / MIXED 🤔")
