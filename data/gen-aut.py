import json
import os
import time, requests
import pandas as pd

addr = 'http://192.168.43.139/9'
df = pd.DataFrame({"time":[], "cooler":[], "fan":[]})
if not os.path.exists('data.csv'):df.to_csv('data.csv', index=False)

while True:
    df = pd.read_csv('data.csv')
    i=len(df)
    data = requests.get(addr)
    data=data.json()
    new_data=[time.time(), data[5], data[6]]
    df.loc[i]=new_data
    df.to_csv('data.csv', index=False)
    print(new_data)
    time.sleep(60*1)

	