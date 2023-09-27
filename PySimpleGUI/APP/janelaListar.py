from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, HSeparator, Push,
    theme, popup, Checkbox, Spin, Frame
)
def janela_contato():
    theme('LightBlue2')

    layout = [
        [
            Text('Qualquer'),
            Spin(list(range(0, 90)), initial_value=0)
        ]
    ]

    layout = [
        [
            Frame('Qt Frame',
                  layout)
        ]

    ]
    return Window('Teste',
                  layout=layout)

janela=janela_contato()

janela.read()