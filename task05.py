def calculate_salary(hours: int, rate: float) -> float:
    return hours * rate
def calculate_tax(salary: float) -> float:
    return salary * 0.12

def net_salary(salary: float) -> float:
    tax = calculate_tax(salary)
    return salary - tax
