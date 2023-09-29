from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, HSeparator, Push,
    theme, popup, Checkbox, Menu, Output
)
from Variavel import *

layout = [
    [
        Menu(menu)
    ],

    [
        Output(size=(80, 30))
    ]
]

janela = Window('Nada',
                layout)
janela.read()