from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, HSeparator, Push,
    theme, popup, Checkbox, Spin, Frame
)
from Variavel import *
def janela_contato():
    theme(tema)

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