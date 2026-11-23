You receive transaction data from multiple sources. You must validate:
- Transaction ID should not be NULL.
- Transaction amount should be positive.
- Email should follow a valid format.
- Transaction date should be valid.

class TransactionValidator:

    def validate(self, transaction):
        if transaction["id"] is None:
            raise ValueError("Missing ID")

        if transaction["amount"] <= 0:
            raise ValueError("Invalid amount")

        if "@" not in transaction["email"]:
            raise ValueError("Invalid email")

        return True


composition : HAS-A, Component Objects, Delegation, Modularity,Loose Coupling, Flexibility,Maintainability.
Composition is an object-oriented programming design technique that establishes a HAS-A relationship between classes. It allows one class to contain objects of other classes, called component objects, and delegate specific responsibilities to them to achieve its functionality.
