import openai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Function to generate financial advice
def get_financial_advice(user_query):
    client = openai.OpenAI(api_key=OPENAI_API_KEY)  # New OpenAI client

    response = client.chat.completions.create(  # Updated method
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a financial assistant providing personalized finance advice."},
            {"role": "user", "content": user_query}
        ]
    )

    return response.choices[0].message.content  # Updated response format

# Test the chatbot
if __name__ == "__main__":
    user_input = input("Ask me a finance question: ")
    print(get_financial_advice(user_input))
