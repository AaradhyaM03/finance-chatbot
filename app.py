import streamlit as st
from chatbot import get_financial_advice
from budget_tracker import plot_budget

st.title("💰 AI-Powered Personal Finance Chatbot")

# Chatbot Section
st.header("💬 Financial Advice Chatbot")
user_input = st.text_input("Ask a finance question:")
if user_input:
    advice = get_financial_advice(user_input)
    st.write("🧠 AI Advice: ", advice)

# Budget Tracking Section
st.header("📊 Budget Tracking")
if st.button("Show Budget Analysis"):
    st.pyplot(plot_budget())
