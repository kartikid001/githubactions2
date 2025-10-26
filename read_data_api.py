import requests
import pandas as pd
import os

token = os.getenv("API_TOKEN")
print(f"Token: {token}")
if token=="1234abcd":
    print("correct")
else:
    print("incorrect")

# response = requests.get("https://jsonplaceholder.typicode.com/users")
# # by defaily we get response in text format
# data = response.json()
# df=pd.DataFrame(data)
# df = df[["id", "name"]]
# print(df)