#%%
import pandas as pd;

df = pd.read_csv("../DATASET_for_cleaning/customers-10000.csv")

# pd.set_option("display.max_columns" , None);
# pd.set_option("display.width" , None)
# print(df.shape);
# print(df.info())

# print(df.describe(include="all"))
# print(df.nunique())  # how much varition that dataset has

# print(df.isnull().sum())

#calculation percentage of missing data 
# missing = df.isnull().sum()

# percentage = (missing / len(df)) * 100
# print(percentage)

#check duplicate value

# print(df.duplicated().sum())
#to check specfic column

# print(df['Email'].duplicated().sum())
# to add underscore to connect the name of column which contain the spaces
df.columns = (
    df.columns.str.strip().str.lower().str.replace(' ' , '_')
)

# print(df.columns)

text_columns = [
    'first_name',
    "last_name",
    "company",
    "city",
    "country"
]

for column in text_columns:
    df[column] = df[column].str.strip()

df['first_name'] = df['first_name'].str.title()
df['last_name'] = df['last_name'].str.title()
df["email"] = df['email'].str.strip().str.lower()

# print(df.iloc[2:4].to_string())

email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

valid_email = df["email"].str.match(email_pattern, na=False)

print(valid_email.value_counts())


# %%
