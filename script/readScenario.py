
import pandas as pd
import json


def read_json(file):
    with open(file, encoding='utf-8') as f:
        data = json.load(f)
    df_scenario = pd.DataFrame(data)

    return df_scenario

filepath = './data/scenario.json'

df_scenario = read_json(filepath)
print(df_scenario.head())