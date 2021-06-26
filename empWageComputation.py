"""
@Author: Rikesh Chhetri
@Date: 2021-06-26 
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-26 15:02:30
@Title : Program Aim is to Calculate the Employee Daily and Monthly  Wage.
"""

import random


def calculate_employee_wage(workRatePerHour):
    """

    Description:
        This method is called for getting Fulltime employee 
        daily wage and part time employee daily wages,
        By multiplying workrateperhour and wagerateperhour.


    Parameter:
        workRatePerHour is will be 8 for full time employee and used for calculating daily wage.

    """

    wageRatePerHour = 20
    employeeDailyWage = wageRatePerHour * workRatePerHour
    print("Employee Daily wage is : ", employeeDailyWage, "$")


if __name__ == "__main__":

    print(" Welcome to Employee Wage Computation Program ")
    attendance_check = random.randint(0, 2)

    # Taking fulltime as a constant variables
    IS_FULL_TIME = 1
    IS_PART_TIME = 2
    if(attendance_check == IS_FULL_TIME):
        calculate_employee_wage(8)

    elif(attendance_check == IS_PART_TIME):
        calculate_employee_wage(4)

    else:
        calculate_employee_wage(0)
