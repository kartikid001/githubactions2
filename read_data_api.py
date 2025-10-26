import requests
import pandas as pd

response = request.get("https://jsonplaceholder.typicode.com/users")
# by defaily we get response in text format
data = response.json()
df=pd.DataFrame(data)
print(df)