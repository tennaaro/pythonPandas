import pandas as pd
import matplotlib.pyplot as plt
part1 = pd.read_csv("task3-part1-input.csv")
part1['Date'] = pd.to_datetime(part1['Date'], format="%Y/%m/%d")
part1 = part1.sort_values(by=['Date'], ascending=[True])


#Part 1
#1
filtered_df = part1.loc[(part1['Date'] >= '2019-01-01')]
print(filtered_df)

#2
filtered_df.set_index('Date', inplace=True)
filtered_df = filtered_df.resample('D').bfill().reset_index()
print(filtered_df)

#3
filtered_df["PriceReversePythonic"] = filtered_df["Price"].values[::-1]
# I could not figure this part out
filtered_df["PriceReverseRecursive"] = filtered_df["Price"].values[::-1]
print(filtered_df)

#4
print(filtered_df['PriceReversePythonic'].equals(filtered_df['PriceReverseRecursive']))

#Part 2
filtered_df.plot(x="Date", y=["Price", "PriceReversePythonic"], figsize=(12, 7))
plt.title("Price vs PriceReversePythonic")
plt.ylabel("Amount in dollars")
# plt.legend(bbox_to_anchor=(1.43, 1.1))
plt.show()