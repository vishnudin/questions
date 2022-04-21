#!/usr/bin/env -S python3
import openpyxl
import pandas as pd


def validate_employee_device():
    file_name = "table_data.xlsx"
    employees_data = pd.read_excel(file_name, sheet_name="Employees")
    device_data = pd.read_excel(file_name, sheet_name="Devices")

    for ind in employees_data.index:
        employee_id = employees_data['id'][ind]
        first_name = employees_data['first_name'][ind]
        last_name = employees_data['last_name'][ind]
        department = employees_data['department'][ind]
        if employee_id in device_data.employee_id.values:
            continue
        else:
            print('Emp ID:', employee_id, '-', first_name, last_name, 'of', department, 'department has not recorded for company issued devices.')
    return True


if __name__ == '__main__':
    validate_employee_device()
