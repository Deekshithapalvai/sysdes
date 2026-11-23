class TransformData:
    def transform_data(self, data):
        transformed_data = []
        for row in data:
            transformed_row = {
                "EmployeeID": int(row["EmployeeID"]),
                "Name": row["Name"].strip().title(),
                "Age": int(row["Age"]),
                "Salary": float(row["Salary"])
            }
            transformed_data.append(transformed_row)
        return transformed_data
