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
        workRatePerHour is will be 8 for full time employee and 4 for part timr employee,
        and used for calculating daily wage.

    """
    # defining wage rate per hour.
    wageRatePerHour = 20
    employeeDailyWage = wageRatePerHour * workRatePerHour
    print("Employee Daily wage is : ", employeeDailyWage, "$")


if __name__ == "__main__":

    def isFullTime():
        """

       Description:
           This function  is used for calculating fulltime employee wage.

       Return:
           Here it will call calculate employee wage and return the wage of full time employee.
           This function also pass work rate hour of an employee for full time employee it is 8.

       """

        return calculate_employee_wage(8)

    def isPartTime():
        """

       Description:
           This function  is used for calculating part-time employee wage.
           This function also pass work rate hour of an employee for part time  employee it is 4.

       Return:
           Here it will call calculate employee wage and return the daily wage of part time employee.

       """

        return calculate_employee_wage(4)

    def absent():
        """

       Description:
           This function  is execute if and employee is absent.

       Return:
           Here it will return 0 if an employee is absent.

       """
        return calculate_employee_wage(0)

    switcher = {
        0: isFullTime,
        1: isPartTime,
        2: absent
    }


def checkEmployee(check):
    """

    Description:
        This function  is used for checking if an employee is fulltime or parttime and absent.


    Parameter:
        check contain random number between 0 to 2 and and if the number is 0 then,
        it will go inside switcher and select index 0 values. 


    Return:
        here func() will be returned and based of the value from switcher it will call that function.

    """

    func = switcher.get(check, "nothing")
    return func()


print(" Welcome to Employee Wage Computation Program ")
attendance_check = random.randint(0, 2)
checkEmployee(attendance_check)
