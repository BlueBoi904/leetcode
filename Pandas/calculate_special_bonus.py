import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = (
        employees["salary"]
        * (employees["name"].str[0] != "M")
        * (employees["employee_id"] % 2 == 1)
    )
    return employees[["employee_id", "bonus"]].sort_values(["employee_id"])
