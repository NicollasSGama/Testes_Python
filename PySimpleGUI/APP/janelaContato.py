from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, HSeparator, Push,
    theme, popup, Checkbox, MenubarCustom,
    Menubar
)
def janela_contato():
    theme('DarkPurple')

    layout = [
        [
            Menubar(
                [
                    ['Arquivo', ['Sair']],

                    ['Editar',['Edite-me']]
                ]
            )
        ],

        [
            MenubarCustom(
                [
                    ['Nada', ['Nada']]
                ]
            )
        ]
    ]
    return Window('Menu',
                  layout=layout,
                  size=(600, 400)
                  )

contato = janela_contato()
contato.read()