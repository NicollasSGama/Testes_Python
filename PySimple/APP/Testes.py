from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, HSeparator, Push,
    theme, popup, Checkbox, Frame, Menu, Output,
    MenubarCustom
)

from Variavel import *
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
#
# theme(tema)
# menu = [
#     [
#         ['Nada', ['Nada']]
#     ]
# ]
#
# layout = [
#     [
#         MenubarCustom(menu)
#     ],
#
#     [
#         Output(size=(80, 30))
#     ]
# ]
#
# janela = Window('Nada',
#                 layout,
#                 )
#
# janela.read()

# menu = [
#     ['&Projeto'],
#     ['&Editar'],
#     ['&Visualizar'],
#     ['&Layout', ['Bonito', 'Feio', 'Mais-Menos']]
# ]
#
# layout = [
#     [Menu(menu)],
#     [Output(size=(80, 30))]
# ]
#
# janela = Window('Teste', layout=layout)
#
# janela.read()
#
import PySimpleGUI as sg
import datetime as dt
dt=dt.datetime.today()
layout = [
    [
        sg.Input(readonly=True,
                 enable_events=True,
                 key='Input 1'),
    ],

    [
        sg.CalendarButton('Calendário',
                          close_when_date_chosen=False,
                          format='%d-%m-%Y',
                          key='-CALENDARIO-',
                          default_date_m_d_y=(9,12,2023),
                          target='Input 1')
    ]
]

window = sg.Window('Calendario', layout)

while True:

    event, values = window.read()



window.close()