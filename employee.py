import sys
import pytest   # as you requested

def employee_details(name, emp_id, department, salary):
    result = (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )
    return result

# ---- MAIN METHOD USING sys.argv ----
if __name__ == "__main__":
    if len(sys.argv) != 5:
        name = sys.argv[1]
        emp_id = sys.argv[2]
        department = sys.argv[3]
        salary = sys.argv[4]

        print(employee_details(name, emp_id, department, salary))
