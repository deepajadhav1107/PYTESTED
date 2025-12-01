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
    # sys.argv[0] → script name
    # sys.argv[1] → name
    # sys.argv[2] → emp_id
    # sys.argv[3] → department
    # sys.argv[4] → salary

    if len(sys.argv) != 5:
        print("Usage: python employee.py <name> <emp_id> <department> <salary>")
        sys.exit(1)

    name = sys.argv[1]
    emp_id = sys.argv[2]
    department = sys.argv[3]
    salary = sys.argv[4]

    print(employee_details(name, emp_id, department, salary))
