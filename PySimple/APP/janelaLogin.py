from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, HSeparator, Push,
    theme, popup, Checkbox, Frame
)
from Variavel import *

def janelaLogin():
    theme(tema)

    layout_entrar = [
        # ------------------------------------------------------------------
        #   Bloco para entrar
        # ------------------------------------------------------------------
        [
            Text('CPF')
        ],

        [
            Input('ex.: 182.254.XXX-X')
        ],

        [
            Text('Senha')
        ],

        [
            Input('*****')
        ],
        # ------------------------------------------------------------------
        #   Linha horizontal
        # ------------------------------------------------------------------
        [
            HSeparator()
        ],
        # ------------------------------------------------------------------
        #   Entrar no programa
        # ------------------------------------------------------------------
        [
            Checkbox('LEMBRE-ME'),

            Push(),

            Button('ESQUECI A SENHA'),

            Button('ENTRAR')
        ]
    ]

    layout = [
        [
            Frame('ENTRAR',
                  layout_entrar)
        ]

    ]

    return Window('ENTRAR',
                  layout=layout,
                  # size=(300, 320)
                  )

janelalogin = janelaLogin()
janelalogin.read()