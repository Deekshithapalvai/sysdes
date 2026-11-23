class Validator:
    def validate_data(self, data):
        valid_records = []
        invalid_records = []
        for row in data:
            if (
                not row["EmployeeID"].strip()
                or not row["Name"].strip()
                or not row["Age"].strip()
                or not row["Salary"].strip()
            ):
                invalid_records.append(row)
            else:
                valid_records.append(row)
        print("Valid records:", len(valid_records))
        print("Invalid records:", len(invalid_records))
        return valid_records, invalid_records
