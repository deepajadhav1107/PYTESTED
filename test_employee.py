from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Alice\n"
        "Employee ID: E1001\n"
        "Department: IT\n"
        "Salary: 55000"
    )

    assert employee_details("Alice", "E1001", "IT", 55000) == expected_output
