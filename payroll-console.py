import os
#You wil write a program to create a screen which will allow the user to find the weekly pay earned by an employee.


#Variable Setup START

projectName = 'Payroll Program By Will Hellinger'

employeeNames = []
employeeIDs = []
employeePaycodes = []
employeeHours = []
employeeShifts = []

paycodes = {
    "1" : 10,
    "2" : 12.50,
    "3" : 15.00,
    "4" : 17.50,
    "5" : 20.00
}

taxRate = .14
insuranceRate = .05
overTimeRate = 1.5

#Variable Setup END

def clearScreen():
    if str(os.name) == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def loadEmployees():
    clearScreen()
    print(f'{projectName}: Employee Add ("Done" to quit)')
    print('Employee First & Last Name | ID | Pay Code | Hours Worked | Shift')
    global employeeNames, employeeIDs, employeePaycodes, employeeHours, employeeShifts

    inputs = ['Employee First', 'Last Name', 'ID', 'Pay Code', 'Hours Worked', 'Shift']

    while True:
        data = str(input('')).split(' ')
        if data[0] == 'Done':
            break
    
        if len(data) < 6:
            print(f'Missing Input: {inputs[len(data)]}')
        elif len(data) >= 6:
            employeeNames.append(f'{data[0]} {data[1]}')
            employeeIDs.append(data[2])
            employeePaycodes.append(data[3])
            employeeHours.append(data[4])
            employeeShifts.append(data[5])


def calculateCosts():
    global employeeNames, employeeIDs, employeePaycodes, employeeHours, employeeShifts, taxRate, insuranceRate, overTimeRate

    clearScreen()
    print(projectName)

    for a in range(len(employeeNames)):
        overTime = 0

        if int(employeeHours[a]) > 40:
            overTime = int(employeeHours[a]) - 40
            overTime = round((overTime * (paycodes[employeePaycodes[a]] * overTimeRate)) * 100)/100

            takeHomeAmount = paycodes[employeePaycodes[a]] * 40

        elif int(employeeHours[a]) <= 40:
            takeHomeAmount = paycodes[employeePaycodes[a]] * int(employeeHours[a])

        takeHomeAmount += overTime
        tax = round((takeHomeAmount * taxRate)* 100) / 100
        insurance = round((takeHomeAmount *insuranceRate) * 100) / 100
        takeHomeAmount -= (tax + insurance)

        print(f'{employeeNames[a]} (ID: {employeeIDs[a]} | Shift: {employeeShifts[a]}): {paycodes[employeePaycodes[a]]}/hour for {employeeHours[a]} hours | Tax: ${tax} | Insurance: ${insurance} | Overtime: ${overTime} | Take Home Pay: ${takeHomeAmount}')
    
    input('Press Enter to Continue...')


def clearEmployees():
    global employeeNames, employeeIDs, employeePaycodes, employeeHours, employeeShifts
    employeeNames = []
    employeeIDs = []
    employeePaycodes = []
    employeeHours = []
    employeeShifts = []

clearScreen()

while True:
    print(projectName)
    command = str(input('Command: (Add | Calculate | Clear | Exit): '))
    if command == 'Add' or command == 'add':
        loadEmployees()
    elif command == 'Calculate' or command == 'calculate':
        try:
            calculateCosts()
        except Exception as error:
            input('Encountered unknown error')
    elif command == 'Clear' or command == 'clear':
        clearEmployees()
    elif command == 'Exit' or command == 'exit':
        exit()
    else:
        input('Unknown Command, Press Enter to Continue...')
    clearScreen()