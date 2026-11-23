import csv
import json
import pandas as pd
from sqlalchemy import create_engine


class LoadData:

    @staticmethod
    def load_csv(data, output_file):
        if not data:
            print("No data to load")
            return

        with open(output_file, "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=data[0].keys()
            )
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def load_json(data, output_file):
        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_excel(data, output_file):
        df = pd.DataFrame(data)
        df.to_excel(output_file, index=False)

    @staticmethod
    def load_parquet(data, output_file):
        df = pd.DataFrame(data)
        df.to_parquet(output_file, index=False)

    @staticmethod
    def load_txt(data, output_file):
        with open(output_file, "w") as file:
            for row in data:
                file.write(str(row) + "\n")

    @staticmethod
    def load_database(data, table_name, connection_url):
        if not data:
            print("No data to load")
            return

        df = pd.DataFrame(data)
        engine = create_engine(connection_url)

        with engine.begin() as connection:
            df.to_sql(
                table_name,
                connection,
                if_exists="append",
                index=False
            )
