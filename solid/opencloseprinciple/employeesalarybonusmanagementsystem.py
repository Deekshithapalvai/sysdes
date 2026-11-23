from abc import ABC, abstractmethod

class BonusStrategy(ABC):

    @abstractmethod
    def calculate_bonus(self, employee):
        pass

class FixedBonus(BonusStrategy):

    def __init__(self, percentage):

        if isinstance(percentage, bool) or not isinstance(percentage, (int, float)):
            raise TypeError("Percentage must be numeric")

        if not 0 <= percentage <= 100:
            raise ValueError("Invalid percentage")

        self.percentage = percentage

    def calculate_bonus(self, employee):
        return employee.salary * self.percentage / 100

class PerformanceBonus(BonusStrategy):

    def calculate_bonus(self, employee):

        score = employee.performance_score

        if score is None or isinstance(score, bool) or not isinstance(score, (int, float)):
            raise ValueError(" score required")

        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100")

        if score >= 90:
            percentage = 30
        elif score >= 75:
            percentage = 20
        elif score >= 50:
            percentage = 10
        else:
            percentage = 0

        return employee.salary * percentage / 100

class Employee:

    def __init__(self, name, salary, performance_score=None):

        if isinstance(salary, bool) or not isinstance(salary, (int, float)):
            raise TypeError("Salary must be numeric")

        if salary <= 0:
            raise ValueError("Salary must be positive")

        self.name = name
        self.salary = salary
        self.performance_score = performance_score


class BonusCalculator:

    def calculate(self, employee, strategy):

        if not isinstance(strategy, BonusStrategy):
            raise TypeError("Invalid bonus strategy")

        return strategy.calculate_bonus(employee)



employee = Employee("Alex", 50000, 85)

calculator = BonusCalculator()

strategies = [
    FixedBonus(20),
    FixedBonus(10),
    FixedBonus(5),
    FixedBonus(25),
    FixedBonus(30),
    PerformanceBonus()
]

for strategy in strategies:

    bonus = calculator.calculate(employee, strategy)

    print(f"{type(strategy).__name__}: {bonus:.2f}")