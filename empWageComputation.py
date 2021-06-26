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
        This method is called for getting  employee daily wage,
        By multiplying workrateperhour and wagerateperhour.
        
    Parameter:
        workRatePerHour is will be 8 for full time employee and used for calculating daily wage.

    """

    wageRatePerHour = 20
    employeeDailyWage = wageRatePerHour * workRatePerHour
    print("Employee Daily wage is : " , employeeDailyWage ,"$")


if __name__ == "__main__":
   
    print(" Welcome to Employee Wage Computation Program ")
    attendance_check = random.randint(0, 1)
    
    # Taking fulltime as a constant variables
    IS_FULL_TIME = 1
    if(attendance_check == IS_FULL_TIME):
        calculate_employee_wage(8)

    else:
        calculate_employee_wage(0)
