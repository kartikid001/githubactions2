import requests
import pandas as pd

response = requests.get("https://jsonplaceholder.typicode.com/users")
# by defaily we get response in text format
data = response.json()
df=pd.DataFrame(data)
df = df[["id", "name"]]
print(df)