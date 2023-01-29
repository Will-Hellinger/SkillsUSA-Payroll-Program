import PySimpleGUI as sg

#Variable Setup START

projectName = 'Payroll Program By Will Hellinger'

paycodes = {"1": 10, 
            "2": 12.50, 
            "3": 15.00, 
            "4": 17.50, 
            "5": 20.00
           }

taxRate = .14
insuranceRate = .05
overTimeRate = 1.5

#Variable Setup END

layout = [[sg.Text(projectName)],
          [sg.Text('Employee First & Last Name'),sg.Input(key='_NAME_')], 
          [sg.Text('ID'), sg.Input(key='_ID_')],
          [sg.Text('Pay Code'), sg.Input(key='_PAYCODE_')],
          [sg.Text('Hours Worked'), sg.Input(key='_HOURS_')],
          [sg.Text('Shift'), sg.Input(key='_SHIFT_')], 
          [sg.Button("Calculate")],
          [sg.Button('Clear')],
          [sg.Button('Exit ')],
          [sg.Text('Employee Name: ', key='_NAME_TEXT_')],
          [sg.Text('ID: ', key='_ID_TEXT_')],
          [sg.Text('Pay Code: ', key='_PAYCODE_TEXT_')],
          [sg.Text('Hours Worked: ', key='_HOURS_TEXT_')],
          [sg.Text('Shift: ', key='_SHIFT_TEXT_')],
          [sg.Text('Tax: ', key='_TAX_TEXT_')],
          [sg.Text('Insurance: ', key='_INSURANCE_TEXT_')],
          [sg.Text('Overtime: ', key='_OVERTIME_TEXT_')],
          [sg.Text('Total TakeHome: ', key='_TOTAL_TEXT_')],
        ]

# Create the window
window = sg.Window(projectName, layout, resizable=True)


def clear():
    clearElements = ['_ID_', '_NAME_', '_PAYCODE_', '_HOURS_', '_SHIFT_']
    for a in range(len(clearElements)):
        window.Element(clearElements[a]).Update('')
    changeElements = ['_NAME_TEXT_', '_ID_TEXT_', '_PAYCODE_TEXT_', '_HOURS_TEXT_', '_SHIFT_TEXT_', '_TAX_TEXT_', '_INSURANCE_TEXT_', '_OVERTIME_TEXT_', '_TOTAL_TEXT_']
    changeText = ['Employee Name: ', 'ID: ', 'Pay Code: ', 'Hours Worked: ', 'Shift: ', 'Tax: ', 'Insurance: ', 'Overtime: ', 'Total TakeHome: ']
    for a in range(len(changeElements)):
        window.Element(changeElements[a]).Update(changeText[a])

def calculateCosts(employeeNames, employeeIDs, employeeHours, employeePaycodes, employeeShifts):
    global paycodes, taxRate, insuranceRate, overTimeRate

    print(projectName)

    for a in range(len(employeeNames)):
        overTime = 0

        if int(employeeHours[a]) > 40:
            overTime = int(employeeHours[a]) - 40
            overTime = round((overTime *(paycodes[str(employeePaycodes[a])] * overTimeRate)) * 100) / 100

            takeHomeAmount = paycodes[str(employeePaycodes[a])] * 40

        elif int(employeeHours[a]) <= 40:
            takeHomeAmount = paycodes[str(employeePaycodes[a])] * int(
                employeeHours[a])

        takeHomeAmount += overTime
        tax = round((takeHomeAmount * taxRate)* 100) / 100
        insurance = round((takeHomeAmount *insuranceRate) * 100) / 100
        takeHomeAmount -= (tax + insurance)

        window.Element('_NAME_TEXT_').Update(f'Employee Name: {employeeNames[a]}')
        window.Element('_ID_TEXT_').Update(f'ID: {employeeIDs[a]}')
        window.Element('_PAYCODE_TEXT_').Update(f'PayCode: {str(employeePaycodes[a])}')
        window.Element('_HOURS_TEXT_').Update(f'Hours Worked: {employeeHours[a]}')
        window.Element('_SHIFT_TEXT_').Update(f'Shift: {employeeShifts[a]}')
        window.Element('_TAX_TEXT_').Update(f'Tax: ${tax}')
        window.Element('_INSURANCE_TEXT_').Update(f'Insurance: ${insurance}')
        window.Element('_OVERTIME_TEXT_').Update(f'Overtime: ${overTime}')
        window.Element('_TOTAL_TEXT_').Update(f'Total Takehome: ${takeHomeAmount}')
        print(f'{employeeNames[a]} (ID: {employeeIDs[a]} | Shift: {employeeShifts[a]}): {paycodes[str(employeePaycodes[a])]}/hour for {employeeHours[a]} hours | Tax: ${tax} | Insurance: ${insurance} | Overtime: ${overTime} | Take Home Pay: ${takeHomeAmount}')

while True:
    event, values = window.read()
    if event == 'Calculate':
        calculateCosts([values['_NAME_']], [values['_ID_']], [values['_HOURS_']], [int(values['_PAYCODE_'])], [values['_SHIFT_']])
    if event == 'Clear':
        clear()
    if event == "Exit " or event == sg.WIN_CLOSED:
        break
window.close()