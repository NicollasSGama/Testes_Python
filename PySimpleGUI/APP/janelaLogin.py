from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, HSeparator, Push,
    theme, popup, Checkbox, Frame
)

def janelaLogin():
    theme('LightBlue2')

    layout_entrar = [
        # ------------------------------------------------------------------
        #   Bloco para entrar
        # ------------------------------------------------------------------
        [
            Text('E-mail')
        ],

        [
            Input('ex.: dolores@contato.com')
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