from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator
)

# layout = [
#     [Button('Botão 1'), Button('Coluna 1')], # Linha 1
#     [Text('Aperte o botão 2:'), Button('Botão 2')] # Linha 1
# ]
#
# window = Window(
#     'Título da Janela',
#     size=(600, 400),
#     layout=layout
# )
# window.read()
# window.close()

layout = [
    [
        Image(filename='teste.png')
    ],
    [Text('Email:'), Input()],
    [Text('Senha:'), Input(password_char='*')],
    [Button('Login'), Button('Esqueci a senha')]
]

window = Window(
    'Título da Janela',
    size=(600, 400),
    layout=layout
)

window.read()
window.close()
