import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ecommerce_sales.csv")

top_customers = (
    df.groupby("Customer_Name")["Net_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print(top_customers)

top_customers.plot(kind="bar")

plt.title("Top 5 Customers")
plt.xlabel("Customer")
plt.ylabel("Net Sales")

plt.savefig("Top_Customers.png")

plt.show()