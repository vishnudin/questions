#!/usr/bin/env -S python3
import openpyxl
import pandas as pd
import sys
import json


def update_config_details():
    env = sys.argv[1]
    input_file_name = r"configs/input.csv"
    input_data = pd.read_csv(input_file_name)
    data = input_data.loc[input_data['ENV'] == env]

    host = data.iloc[0]['host']
    port = data.iloc[0]['port']
    dbname = data.iloc[0]['dbname']
    user = data.iloc[0]['user']
    password = data.iloc[0]['password']

    json_file_name = r"configs/config.json"
    json_file = open(json_file_name, "r")
    json_object = json.load(json_file)
    json_file.close()

    json_object[env]["host"] = host
    json_object[env]["port"] = int(port)
    json_object[env]["dbname"] = dbname
    json_object[env]["user"] = user
    json_object[env]["password"] = password
    update_json_file = open(json_file_name, "w")
    json.dump(json_object, update_json_file, indent=4)
    update_json_file.close()
    print("Successfully updated Json config for", env, 'environment.')


if __name__ == '__main__':
    update_config_details()
