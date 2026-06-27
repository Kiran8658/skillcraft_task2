import pandas as pd
df = pd.read_csv('data/train.csv')
print("First 5 rows:")
print(df.head())
print("\nData info:")
print(df.info())
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:")
print(df.duplicated().sum())

df = df.drop_duplicates()
print("\nShape After Removing Duplicates:")
print(df.shape)

df["Order Date"]=pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"]=pd.to_datetime(df["Ship Date"], dayfirst=True)
print("\nUpdated Data Types:")
print(df.dtypes)

df.to_csv('data/cleaned_train.csv', index=False)
print("\n cleaned_train.csv file has been saved successfully as cleaned_train.csv.")