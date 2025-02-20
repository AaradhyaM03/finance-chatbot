import pandas as pd
import matplotlib.pyplot as plt

# Sample Budget Data
data = {
    "Category": ["Rent", "Groceries", "Entertainment", "Savings", "Utilities"],
    "Amount": [1200, 400, 150, 500, 200]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Function to visualize spending
def plot_budget():
    df.plot(kind="bar", x="Category", y="Amount", legend=False)
    plt.xlabel("Expense Category")
    plt.ylabel("Amount ($)")
    plt.title("Monthly Expense Distribution")
    plt.show()

# Test budget tracking
if __name__ == "__main__":
    plot_budget()
