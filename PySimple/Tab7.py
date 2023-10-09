import PySimpleGUI as sg


sg.theme('GreenTan')
tab2_layout = [[sg.Text('This is inside tab 2')],
               [sg.Text('Tabs can be anywhere now!')]]

tab1_layout = [[sg.Text('Type something here and click button'), sg.Input(key='in')]]

tab3_layout = [[sg.Text('This is inside tab 3')]]
tab4_layout = [[sg.Text('This is inside tab 4')]]


layout = [[sg.Text('My Window!')], [sg.Frame('A Frame', layout=
                                                                       # Code change here
    [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]], tab_location="left", key='1'),
      sg.TabGroup([[sg.Tab('Tab3', tab3_layout), sg.Tab('Tab 4', tab4_layout)]], tab_location='right', key='2')]])]]

window = sg.Window('My window with tabs', layout, default_element_size=(12,1), finalize=True)

print('Are there enough tabs for you?')

while True:
    event, values = window.read()
    print(event, values)
    if event is None:           # always,  always give a way out!
        break

window.close()