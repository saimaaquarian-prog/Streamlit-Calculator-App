# ============================================
# 🧮 Streamlit Calculator App
# ============================================

import streamlit as st

# Page setup
st.set_page_config(page_title="Calculator App", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator")
st.write("Perform basic arithmetic operations easily!")

# Input fields
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter first number:", value=0.0)
with col2:
    num2 = st.number_input("Enter second number:", value=0.0)

# Operation selector
operation = st.selectbox(
    "Choose operation:",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"]
)

# Compute button
if st.button("Calculate"):
    try:
        if operation == "Addition (+)":
            result = num1 + num2
            st.success(f"✅ Result: {num1} + {num2} = {result}")
        elif operation == "Subtraction (-)":
            result = num1 - num2
            st.success(f"✅ Result: {num1} - {num2} = {result}")
        elif operation == "Multiplication (×)":
            result = num1 * num2
            st.success(f"✅ Result: {num1} × {num2} = {result}")
        elif operation == "Division (÷)":
            if num2 == 0:
                st.error("❌ Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                st.success(f"✅ Result: {num1} ÷ {num2} = {result}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
