def calculate_taxes(income: int) -> float:
    # write your code here
    if income <= 1000:
        return income * 0.02
    if 1000 < income <= 10000:
        return income * 0.03
    if income > 10000:
        return income * 0.05
