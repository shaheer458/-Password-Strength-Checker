import streamlit as st 

st.title("🛡️Password Strength Checker")
st.markdown("### 🌟Welcome to Password Strength Checker!")

st.write("Enter a password below to check its strength:")

# Password Input
password = st.text_input("Password", type="password")

# Strength Checker Logic
def check_password_strength(password):
    if len(password) < 6:
        return "Weak"
    elif any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        return "Medium"
    elif len(password) > 10 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password) and any(not char.isalnum() for char in password):
        return "Strong"
    else:
        return "Weak"

# Display Password Strength
if password:
    strength = check_password_strength(password)
    st.subheader(f"Password Strength: {strength}")