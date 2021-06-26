"""
@Author: Rikesh Chhetri
@Date: 2021-06-26 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-26 15:02:30
@Title : Program Aim is to Calculate the Employee Daily and Monthly  Wage.
"""

import random


def calculate_employee_wage():
    """

    Description:
        This method is called for getting attendance of an employee 
        by genetaring random num between o and 1.
        if number is 0 then employee is present else employee is absent.
    
    """

    print(" Welcome to Employee Wage Computation Program ")
    attendance_check = random.randint(0, 1)

    if(attendance_check == 0):
        print("Employee is Present")

    else:
        print("Employee is Absent")


calculate_employee_wage()
