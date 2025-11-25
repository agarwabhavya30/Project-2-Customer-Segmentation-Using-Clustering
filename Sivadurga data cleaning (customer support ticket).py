
import pandas as pd
df=pd.read_csv("C:\customers.csv",encoding="latin-1")
print(df.head())

#Getting the info#
import pandas as pd
df=pd.read_csv("C:\customers.csv",encoding="latin-1")
print(df.info())

#cleaning the date format#
import pandas as pd
df=pd.read_csv("C:\customers.csv",encoding="latin-1")
df['Date of Purchase'] = pd.to_datetime(df['Date of Purchase'], format='%d-%m-%Y', errors='coerce')
print(df["Date of Purchase"].head())

import pandas as pd
df=pd.read_csv("C:\customers.csv",encoding="latin-1")
df['First Response Time'] = pd.to_datetime(df['First Response Time'], format='%d-%m-%Y %H:%M', errors='coerce')
print(df["First Response Time"].head(10))

#converting to datetime#
import pandas as pd
df=pd.read_csv("C:\customers.csv",encoding="latin-1")
df["First Response Time"] = pd.to_datetime(df["First Response Time"], dayfirst=True, errors='coerce')
print(df["First Response Time"].head(10))


#Removing and replacing null values#
import pandas as pd
df=pd.read_csv("C:\customers.csv",encoding="latin-1")
for col in df.columns:
    if df[col].dtype == 'object':   # Categorical
        df[col].fillna(df[col].mode()[0], inplace=True)
df.fillna(df.median(numeric_only=True), inplace=True)
print(df.info())