import csv
import json
import pandas as pd
import requests
from sqlalchemy import create_engine

class ExtractData:
    # 1. Extract data from CSV files
    def extract_data_csv(self, file_path):
        data = []
        with open(file_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
    # 2. Extract data from JSON files
    def extract_data_json(self, file_path):
        with open(file_path, mode="r") as file:
            data = json.load(file)
        return data
    # 3. Extract data from SQL databases
    def extract_data_sql(self, connection_string, query):
        engine = create_engine(connection_string)
        try:
            with engine.connect() as db_connection:
                data = pd.read_sql(query, db_connection)
            return data
        finally:
            engine.dispose()
    # 4. Extract data from REST APIs
    def extract_data_api(self, api_url):
        response = requests.get(api_url, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data

extractor = ExtractData()
csv_data = extractor.extract_data_csv("employees.csv")
print("CSV Data:", csv_data)

json_data = extractor.extract_data_json("employees.json")
print("JSON Data:", json_data)

api_data = extractor.extract_data_api(
    api_url= "www.example.com"
)
print("API Data:", api_data)
