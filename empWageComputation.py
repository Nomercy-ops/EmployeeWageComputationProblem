"""
@Author: Rikesh Chhetri
@Date: 2021-06-26
@Last Modified by: Rikesh Chhetri
@Last Modified time: 2021-06-26 15:02:30
@Title : Program Aim is to Calculate the Employee Daily and Monthly Wage.
"""

import random

# variable for storing employee monthly wage and work rate per hour.
employeeMonthlyWage = 0
employeeWorkRatePerHour = 0
employeeDailyWage = 0


def calculate_employee_wage(workRatePerHour):
    """

    Description:
        This method is called for getting Fulltime employee
        daily wage and part time employee daily wages,
        By multiplying workrateperhour and wagerateperhour.
        Employee monthly wage is also calculated here and stored the value inside global variable employee monthly wage.


    Parameter:
        workRatePerHour  will be 8 for full time employee and 4 for part timr employee,
        and used for calculating daily wage.

    """

    # global variable employee monthly wage.
    global employeeMonthlyWage
    global employeeWorkRatePerHour
    global employeeDailyWage

    # assigning employee work rate per hour with work rate per hour.
    employeeWorkRatePerHour = workRatePerHour
    # constant variable
    WAGE_RATE_PER_HOUR = 20

    employeeDailyWage = WAGE_RATE_PER_HOUR * workRatePerHour
    employeeMonthlyWage += employeeDailyWage
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


def getWorkHours(employeeHours):
    """

    Description:
        This function  is used for calculating employee daily work hour.


    Parameter:
        employee hour is used for getting employee daily hour if an employee is
        full time it will store 8 and if employee is part time it wil store 4.

    """

    print("Employee Work Hours is :", employeeHours)


print(" Welcome to Employee Wage Computation Program ")

# Constant variable
WORKING_DAYS_PER_MONTH = 20
WORKING_HOURS_PER_MONTH = 100

# instance variable
totalWorkingDays = 0
totalWorkingHours = 0

# Dictionary for storing  Day , daily and monthly wage of an employee
storingEmployeeWages = {}


while (totalWorkingHours <= WORKING_HOURS_PER_MONTH and totalWorkingDays < WORKING_DAYS_PER_MONTH):

    attendance_check = random.randint(0, 2)
    checkEmployee(attendance_check)

    # increamenting days.
    totalWorkingDays += 1
    totalWorkingHours += employeeWorkRatePerHour
    getWorkHours(employeeWorkRatePerHour)

    # updating daily wage into dictionary within while loop.
    storingEmployeeWages.update({totalWorkingDays: employeeDailyWage})


# printing employee monthly wage outside of for loop.
print("Employee Monthly wage is : ", employeeMonthlyWage, "$")

# storing total wage of employee into dictionary
storingEmployeeWages.update({'Total Wage': employeeMonthlyWage})

# printing employee wages stored inside list.
print(storingEmployeeWages)
