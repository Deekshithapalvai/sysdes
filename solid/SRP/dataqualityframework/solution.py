from datetime import datetime

def validate_transaction_id(transaction):
    return transaction.get("id") is not None

def validate_amount(transaction):
    return transaction.get("amount", 0) > 0

def validate_email(transaction):
    email = transaction.get("email", "")
    return "@" in email and "." in email

def validate_date(transaction):
    try:
        datetime.strptime(transaction["date"], "%Y-%m-%d")
        return True
    except (ValueError, KeyError):
        return False


    
class TransactionValidator:

    def __init__(self, rules):
        self.rules = rules

    def validate(self, transaction):
        return all(
            rule(transaction)
            for rule in self.rules
        )
validator = TransactionValidator([
    validate_transaction_id,
    validate_amount,
    validate_email,
    validate_date
])
transaction = {
    "id": 101,
    "amount": 500,
    "email": "user@gmail.com",
    "date": "2026-11-23"
}

print(validator.validate(transaction))
