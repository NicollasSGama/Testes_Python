# Criar uma tela
# Atribuir dados
# Salvar no txt

from PySimpleGUI import (
    Text, Input, Button, Column,
    HSeparator, VSeparator, Push,
    Window, Frame
)

def janela_atividade():

    layout = [
        [
            Text('Nome')
        ],

        [
            Input()
        ],

        [

        ]
    ]

    layout = [
        [
            Frame('Dados',
                  layout)
        ]
    ]
    return Window('ATIVIDADE',
                  layout)

janela_atividade().read()
