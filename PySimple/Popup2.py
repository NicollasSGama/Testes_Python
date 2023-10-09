import PySimpleGUI as sg
import pandas as pd


# --- functions ---

def GUI_POPUP(text, data):
    layout = [
        [sg.Text(text)],
        [sg.Listbox(data, size=(20, 5), key='SELECTED')],
        [sg.Button('OK')],
    ]

    window = sg.Window('POPUP', layout).Finalize()

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'OK':
            break
        else:
            print('OVER')

    window.close()

    print('[GUI_POPUP] event:', event)
    print('[GUI_POPUP] values:', values)

    if values and values['SELECTED']:
        return values['SELECTED']


def GUI_MAIN(data):
    strategies = data['STRATEGIES'].tolist()
    for_show = data['FOR_SHOW'].tolist()

    layout = [
        [sg.Button('SEND')],
        [sg.Text('STRATEGY', size=(20, 1)), sg.Input(size=(20, 1), key='STRATEGY'), sg.Button('SELECTION')],
        [sg.Text('FOR_SHOW', size=(20, 1)), sg.Listbox(for_show, size=(20, 5), key='FOR_SHOW', enable_events=False)],
    ]

    window = sg.Window('GUI', layout).Finalize()

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'SEND':
            break
        elif event == 'SELECTION':
            selected = GUI_POPUP('STRATEGY', strategies)
            print('selected:', selected)
            if selected:
                window['STRATEGY'].update(selected[0])

                mask = (data['STRATEGIES'] == selected[0])
                for_show = data['FOR_SHOW'][mask].tolist()

                window['FOR_SHOW'].update(for_show)

        else:
            print('OVER')

    window.close()

    print('[GUI_MAIN] event:', event)
    print('[GUI_MAIN] values:', values)


# --- main ---

if __name__ == '__main__':
    # df_strategies = pd.read_excel(r'path/Strategies.xlsx', 'Strategies')
    df_strategies = pd.DataFrame({
        'STRATEGIES': ['A', 'B', 'C'],
        'FOR_SHOW': [1, 2, 3]
    })

    GUI_MAIN(df_strategies)