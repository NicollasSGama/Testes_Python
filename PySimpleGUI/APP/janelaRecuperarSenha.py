from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, HSeparator, Push,
    theme, popup, Checkbox, Frame
)
from Variavel import *

def janela_recuperar_senha():
    theme(tema)
    layout = [
        [
            Text('CPF')
        ],

        [
            Input('ex.: 123.456.789-x')
        ],

        [
            HSeparator()
        ],

        [
            Button('VOLTAR'),

            Push(),

            Button('VERIFICAR')
        ]
    ]

    layout = [
        [
            Frame('RECUPERAR SENHA',
                  layout)
        ]
    ]
    return Window('VERIFICAÇÂO',
                  layout=layout,
                  #size=(300, 320)
                  )
janelacpf = janela_recuperar_senha()
janelacpf.read()

def janela_nova_senha():
    theme('LightBlue2')

    layout = [
        # ------------------------------------------------------------------
        #   Recuperar senha (nova)
        # ------------------------------------------------------------------
        [
            Text('Nova Senha'),
        ],

        [
            Input('*****'),
        ],

        [
            Text('Nova Senha (Confirmar)')
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
        #   Parte inferior e botão recuperar
        # ------------------------------------------------------------------
        [
            Button('VOLTAR'),

            Push(),

            Button('RECUPERAR')
        ]
    ]

    layout = [
        [
            Frame('NOVA SENHA',
                  layout)
        ]
    ]
    return Window('NOVA SENHA',
                  layout=layout
                  )
janelasenha = janela_nova_senha()
janelasenha.read()