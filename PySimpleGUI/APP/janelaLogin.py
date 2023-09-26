from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, HSeparator, Push,
    theme, popup, Checkbox
)

def janelaLogin():
    theme('DarkPurple')

    layout = [
        # ------------------------------------------------------------------
        #   Parte superior e botão registro
        # ------------------------------------------------------------------
        [
            Image(),

            Text('Entrar'),

            Push(),

            Button('Registrar', key='-REG-')
        ],
        # ------------------------------------------------------------------
        #   Linha horizontal
        # ------------------------------------------------------------------
        [
          HSeparator()
        ],

        [
            # Tentar separar
        ],
        # ------------------------------------------------------------------
        #   Entrar Email
        # ------------------------------------------------------------------
        [
            Text('EMAIL')
        ],

        [
            Input('ex.: dolores@contato.com',
                  pad=(5, 10)
                 )
        ],
        # ------------------------------------------------------------------
        #   Entrar Senha
        # ------------------------------------------------------------------
        [
            Text('SENHA')
        ],

        [
            Input('*****',
                  pad=(5, 10)
                  )
        ],
        # ------------------------------------------------------------------
        #   Entrar no programa
        # ------------------------------------------------------------------
        [
            Checkbox('LEMBRE-ME'),

            Push(),

            Button('ENTRAR')
        ]
    ]
    return Window('Login',
                  layout=layout,
                  size=(300, 320)
                  )

janelalogin = janelaLogin()
janelalogin.read()