from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, HSeparator, Push,
    theme, popup, Checkbox
)

def janelaRecuperarSenha():
    theme('Dark Purple')
    layout = [
        # ------------------------------------------------------------------
        #   Parte superior e botão voltar
        # ------------------------------------------------------------------
        [
            Image(),

            Push(),

            Button('VOLTAR')
        ],
        # ------------------------------------------------------------------
        #   Linha horizontal
        # ------------------------------------------------------------------
        [
            HSeparator()
        ],
        # ------------------------------------------------------------------
        #   Parte: Recuperar senha
        # ------------------------------------------------------------------
        [
            Text('RECUPERAR SENHA')
        ],

        [
            Text('CPF')
        ],

        [
            Input('ex.: 123.456.789-x')
        ],
        # ------------------------------------------------------------------
        #   Parte inferior e botão recuperar
        # ------------------------------------------------------------------
        [
            Push(),

            Button('VERIFICAR')
        ]
    ]
    return Window('Verificar',
                  layout=layout,
                  #size=(300, 320)
                  )
janelacpf = janelaRecuperarSenha()
janelacpf.read()

def janelaNovaSenha():
    theme('Dark Purple')

    layout = [
        # ------------------------------------------------------------------
        #   Parte superior e botão voltar
        # ------------------------------------------------------------------
        [
            Image(),

            Push(),

            Button('Voltar')
        ],
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
            Text('Nova Senha(repetir)')
        ],

        [
            Input('*****')
        ],
        # ------------------------------------------------------------------
        #   Parte inferior e botão recuperar
        # ------------------------------------------------------------------
        [
            Push(),

            Button('RECUPERAR')
        ]
    ]
    return Window('NovaSenha',
                  layout=layout
                  )
janelasenha = janelaNovaSenha()
janelasenha.read()