SRP : One responsiblity, one reason to change, high cohesion, separation of concerns

Single Responsibility Principle is the first principle of SOLID in Object-Oriented Programming. It states that a class should have only one responsibility and one reason to change.

One reason to change means that a class should handle one cohesive area of functionality. If different business requirements change independently, those responsibilities should be separated into different classes.

For example, in a Data Engineering ETL pipeline, if a single class handles data extraction, data validation, data transformation and data loading, it violates SRP because each operation has a different responsibility and can change independently.

To follow SRP, I would create separate classes such as Extractor, Validator, Transformer and Loader, each handling its own responsibility.

A class can contain multiple methods as long as those methods support the same responsibility. For example, an EmployeeValidator class can contain methods to validate email, age, salary and employee ID.

We can import and reuse these classes wherever required in the application.

Following SRP improves code readability, maintainability, reusability, testability and extensibility. It also promotes better separation of concerns and helps reduce unnecessary coupling between components.

example:
import csv
def extract_data(file_path):
    data = []
    with open(file_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data
    
def validate_data(data):
    valid_records = []
    invalid_records = []
    for row in data:
        if (not row["EmployeeID"].strip()
            or not row["Name"].strip()
            or not row["Age"].strip()
            or not row["Salary"].strip()):
            invalid_records.append(row)
        else:
            valid_records.append(row)
    print("Valid records:", len(valid_records))
    print("Invalid records:", len(invalid_records))
    return valid_records

def transform_data(data):
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

def load_data(data, output_file):
    if not data:
        print("No data available to load.")
        return
    with open(output_file, mode="w", newline="") as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data successfully loaded into {output_file}")

def etl_pipeline(input_file, output_file):
    extracted_data = extract_data(input_file)
    valid_data = validate_data(extracted_data)
    transformed_data = transform_data(valid_data)
    load_data(transformed_data, output_file)
etl_pipeline("employees.csv", "employees_output.csv")