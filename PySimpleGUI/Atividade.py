# Criar uma tela
# Atribuir dados
# Salvar no txt

from PySimpleGUI import (
    Text, Input, Button, Column,
    HSeparator, VSeparator, Push,
    Window, Frame, CalendarButton,
    theme
)

def janela_atividade():
    theme('DarkBlue3')

    layout_esquerdo = [
        [
            Text('Nome')
        ],

        [
            Input(key='-NOME-')
        ],

        [
            Text('Sobrenome')
        ],

        [
            Input(key='-SOBRENOME-')
        ],

        [
            Text('CPF')
        ],

        [
            Input(key='-CPF-')
        ],

        [
            HSeparator()
        ],

        [
            Button('CHECAR',
                   key='CPF_B'),
        ]
    ]

    layout_direito = [
        [
            Text('Senha')
        ],

        [
            Input(key='-SENHA-')
        ],

        [
            Text('Senha (Confirmar)')
        ],

        [
            Input(key='-SENHA_C-')
        ],


        [
            Text('Nascimento')
        ],

        [
            Input(readonly=True,
                  enable_events=True,
                  key='-CALENDARIO-')
        ],

        [
            HSeparator()
        ],

        [
            CalendarButton('CALENDÁRIO',
                           default_date_m_d_y=(1, 1, 2023),
                           format='%d-%m-%y',
                           close_when_date_chosen=False,
                           key='-CALENDARIO_B-'
                           ),

            Push(),

            Button('REGISTRAR',
                   key='-REGISTRAR-',
                   )
        ]
    ]

    layout_total = [
        [
            Column(layout_esquerdo),

            VSeparator(),

            Column(layout_direito)
        ]
    ]

    layout = [
        [
            Frame('DADOS',
                  layout_total)
        ]
    ]
    return Window('ATIVIDADE',
                  layout)

janela_atividade().read()
