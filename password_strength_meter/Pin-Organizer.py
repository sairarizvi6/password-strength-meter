import re
import streamlit as st 

#***************Approach styling****************
st.set_page_config(page_title="🔐 Password Strength Analyzer", page_icon="🛡️", layout="centered")

#*************Custom CSS for Enhanced UI**************"
st.markdown("""
    <style>
        /* Center Align Content */
        .main {text-align: center;}

        /* Responsive Input Field */
        .stTextInput > div > div > input {
            width: 100%;
            padding: 12px;
            font-size: 16px;
            border-radius: 8px;
            border: 1px solid #ccc;
            text-align: center;
        }

        /* Stylish Button */
        .stButton button {
            width: 100%;
            background: linear-gradient(to right, #007BFF, #0056b3);
            color: white;
            font-size: 18px;
            padding: 12px;
            border-radius: 8px;
            border: none;
            transition: 0.3s;
        } 

        /* Hover Effect */
        .stButton button:hover { 
            background: linear-gradient(to right, #0056b3, #00408a);
            transform: scale(1.05);
        }

        /* Result Box Styling */
        .stAlert {
            padding: 10px;
            border-radius: 8px;
            font-size: 16px;
        }
        
        /* Expander Styling */
        .stExpander {
            border-radius: 8px;
            border: 1px solid #007BFF;
        }
    </style>
""", unsafe_allow_html=True)

# ******Title & Brief Overview******************
st.title("🔐 Password Strength Meter")
st.write("🔎 **Check your password security and get suggestions to make it stronger!**")

# ********Password Security Assessment Function**********
def check_password_strength(password):
    score = 0
    feedback = []

    # ***********Ensure Minimum Password Length**********
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("⚠️ Ensure your password is **at least 8 characters long**.")

    # ***********Validate Upper and Lowercase Characters******
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("⚠️ Include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    # ****Confirm Number Requirement*****
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("⚠️ For improved security, use at least one number (0-9) in your password.")

    # ****Confirm Use of Special Characters (!@#$%^&*)*****
    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("⚠️ Make sure to add at least**one special character** from [!@#$%&*].")

    # ******Indicate Password Strength*****
    if score == 4:
        st.success("✅ **Strong Password!**  Your password is highly secure. 🔒")
    elif score == 3:
        st.info("🟡 **Moderate Password!** Consider adding more security elements. 🔑")
    else:
        st.error("❌ **Weak Password!** Your password needs improvement. 🛑")

    # ****Offer Recommendations for Improvement*****
    if feedback:
        with st.expander("💡 **Tips to Strengthen Your Password** "):
            for item in feedback:
                st.write(item)

# ***Password Input Area******
password = st.text_input("🔑 Enter your password:", type="password", help="Create a strong password for better security.")

# Button to Check Strength
if st.button("🔍 Evaluate Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password before checking!")