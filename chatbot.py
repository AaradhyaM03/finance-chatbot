import openai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Function to generate financial advice
def get_financial_advice(user_query):
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a financial assistant providing personalized finance advice."},
            {"role": "user", "content": user_query}
        ]
    )

    return response["choices"][0]["message"]["content"]

# Test the chatbot
if __name__ == "__main__":
    user_input = input("Ask me a finance question: ")
    print(get_financial_advice(user_input))
