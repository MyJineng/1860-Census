from urllib import request
import ssl
import pandas as pd

url ="https://en.wikipedia.org/wiki/1860_United_States_census"
context = ssl._create_unverified_context()
response = request.urlopen(url, context=context)
url = response.read()

Tables = pd.read_html(url)
print(f'Tables: {len(Tables)}')

Table_1 = pd.read_html(url, match='Population of the US States and Territories')
print(len(Table_1))
df = Table_1[0]
df.head()
print(df.head())
df.to_excel(r'C:\Users\Andrew Amato\1860_Census.xlsx', index = False)