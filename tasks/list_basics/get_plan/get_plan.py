import math


def get_plan(current_production: int, month: int, percent: int):
    # write your code here
    new_plan = []
    production_per_month = current_production
    for i in range(month):
        production_per_month = math.floor(production_per_month * percent / 100) + production_per_month
        new_plan.append(production_per_month)
    return new_plan
