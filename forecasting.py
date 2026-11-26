import pandas as pd

train = pd.read_csv("store-sales-time-series-forecasting/train.csv")
stores = pd.read_csv("store-sales-time-series-forecasting/stores.csv")

train['date'] = pd.to_datetime(train['date'])


# print(train.head())
# print(stores.head())

merged_df = train.merge(stores, on = 'store_nbr', how = 'left')


merged_df['month'] = merged_df.date.dt.to_period('M')
print(merged_df.groupby('month').sales.sum().sort_values(ascending=False).head(10))
print(merged_df.groupby('store_nbr').sales.sum().sort_values(ascending=False).head(10))
print(merged_df.groupby(['month', 'store_nbr']).sales.sum().sort_values(ascending = False).head(10))
# print(train.shape[0])
# print(merged_df.shape[0])

# print(merged_df.groupby('month').sales.sum().sum())
# print(merged_df.sales.sum())
#print(merged_df.head())
# session1
# print('///////////////')
# print('no of stores')
# print(train['store_nbr'].nunique())
# print(f'no of family: {train["family"].nunique()}')
# print(f'date range: {train["date"].min()} to {train["date"].max()}')
# print(f'family sales: {train.groupby("family")["sales"].sum().idxmax()}')
