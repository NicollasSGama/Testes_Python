from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, HSeparator, Push,
    theme, popup, Checkbox, Frame, Menu, Output,
    Menubar
)

# Menubar(
#     [
#         ['Arquivo', ['Sair']],
#
#         ['Editar', ['Edite-me']]
#     ]
# )
# ],
#
# [
# MenubarCustom(
#     [
#         ['Nada', ['Nada']]
#     ]
# )

menu = [
    ['&Projeto'],
    ['&Editar'],
    ['&Visualizar'],
    ['&Layout', ['Bonito', 'Feio', 'Mais-Menos']]
]

layout = [
    [Menu(menu)],
    [Output(size=(80, 30))]
]

janela = Window('Teste', layout=layout)

janela.read()