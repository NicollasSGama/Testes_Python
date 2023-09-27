from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, HSeparator, Push,
    theme, popup, Checkbox, Frame
)
# Deixar tudo um em baixo do outro
def janela_cadastro():
    theme('LightBlue2')

    layoutp = [
        # ------------------------------------------------------------------
        #   Bloco para registar funcionário
        # ------------------------------------------------------------------
        [
            Text('Nome'),
        ],

        [
            Input('ex.: Dolores'),
        ],

        [
            Text('Sobrenome')
        ],

        [
            Input('ex.: da Silva')
        ],

        [
            Text('CPF')
        ],

        [
            Input('ex.: 123.456.789-x')
        ],

        [
            Button('CHECAR')
        ]
    ]

    layoutu = [
        # ------------------------------------------------------------------
        #   Bloco para registar usuário
        # ------------------------------------------------------------------
        [
            Text('Nome de usuário')
        ],

        [
            Input('ex.: dolores_31')
        ],

        [
            Button('CHECAR')
        ],

        [
            Text('Senha'),
        ],

        [
            Input('*****'),
        ],

        [
            Text('Senha (Confirmar)')
        ],

        [
            Input('*****')
        ],

        [
            HSeparator()
        ],

        [
            Button('VOLTAR'),

            Push(),

            Button('CADASTRAR')
        ]
    ]
    layout = [
        [
            Frame('CADASTRAR USUÁRIO',
                  layoutp)
        ],

        [
            Frame('CONTA',
                  layoutu)
        ]
    ]
    return Window('CADASTRAR',
                  layout=layout,
                  )

janelacadastro = janela_cadastro()
janelacadastro.read()