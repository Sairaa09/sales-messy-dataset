import pandas as pd
import numpy as np

df= pd.read_csv('C:/Users/Mian Mohsin/Desktop/data_project/sales_messy_data.csv')

# Clean column names
df.columns= (
    df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
)
#` Convert Unknown or error values into NaN`
df.replace(['UNKNOWN', 'ERROR', ''], np.nan, inplace=True)
# Convert required columns to numeric
numeric_cols= ['quantity','total_spent']
for col in numeric_cols:
    df[col]=pd.to_numeric(df[col], errors='coerce')

# convert date column to datetime
df['transaction_date']=pd.to_datetime(df['transaction_date'], errors='coerce')

# Clean categorical columns
cat_col=['item','payment_method','location']
for col in cat_col:
    df[col]=(
        df[col]
        .str.title()
        .str.strip()
        .fillna('Unknown')
        
    )

invalid_spents=df[
    df['quantity'].notna() &
    df['price_per_unit'].notna() &
    df['total_spent'].notna()&
    (df['total_spent']!= df['quantity']*df['price_per_unit'])

]
# print(invalid_spents.shape[0])
# not invalid_spents find

mask=(
    df['quantity'].notna() &
    df['price_per_unit'].notna() &
    (df['total_spent'].isna()|
    (df['total_spent']!=df['quantity']*df['price_per_unit']))
)

df.loc[mask,'total_spent'] = df.loc[mask,'quantity'] * df.loc[mask,'price_per_unit']
#only 1 row with NaN total_spent after cleaning so it is better to drop that row
df.dropna(subset=['total_spent','quantity','price_per_unit'], inplace=True)

df.to_csv('C:/Users/Mian Mohsin/Desktop/data_project/cleaned_sales_data.csv', index=False)

print(df.isna().sum())
print(df.shape)
