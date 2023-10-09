import PySimpleGUI as sg
import pandas as pd

columns = ["STRATEGY", "FOR_SHOW"]
param = (20,3) # size of the main window

df_strategies = pd.read_excel(r'path/Strategies.xlsx', 'Strategies')

def GUI(df_strategies):
    sg.theme('Dark Brown 1')
    listing = [sg.Text(u, size = param) for u in columns]
    core = [
    sg.Input(size = param, key='STRATEGY'),
    sg.Listbox(list(df_strategies['STRATEGIES ']), size=(20,2), enable_events=False)
    ]

    mesh = [[x,y] for (x,y) in list(zip(listing, core))]
    layout =[[sg.Button("SEND")]]+ mesh
    mesh[0].append(sg.Button('SELECTION'))
    window = sg.Window('GUI', layout, font='Courier 12').Finalize()
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "SEND":
            break
        elif event == 'SELECTION':
            sg.popup_scrolled(list(df_strategies['STRATEGIES ']))

        else:
            print("OVER")
    window.close()
GUI(df_strategies)