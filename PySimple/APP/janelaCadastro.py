from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, HSeparator, Push,
    theme, popup, Checkbox, Frame, CalendarButton,
    Combo, Radio
)
from Variavel import *

# Deixar tudo um em baixo do outro
def janela_cadastro():
    theme(tema)

    layout_cima_e = [
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
            Text('CPF')
        ],

        [
            Input('ex.: 123.456.789-x',
                  key='-CPF-'
                  )
        ],

        [
            Button('CHECAR',
                   target='-CPF-'
                   )
        ],

        [
            Text('Cargo')
        ],

        [
            Combo(lista_cargo,
                  'Escolha um cargo',
                  size=(43, 0)
                  )
        ]
    ]

    layout_cima_d = [
        [
            Text('Sobrenome')
        ],

        [
            Input('ex.: da Silva')
        ],

        [
            Text('Nascimento')
        ],

        [
            Input(readonly=True,
                  enable_events=True,
                  key='-NASCIMENTO-'
                  )
        ],

        [
            CalendarButton('CALENDÁRIO',
                           close_when_date_chosen=False,
                           format='%d-%m-%Y',
                           month_names=(meses),
                           day_abbreviations=(dias),
                           default_date_m_d_y=(1, 1, 2023),
                           target='-NASCIMENTO-'
                           )
        ],

        [
            Text('Carga horária')
        ],

        [
            Combo(lista_carga,
                  'Escolha a carga',
                  size=(43, 0)
                  )
        ]
    ]

    layout_baixo_e = [
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
            Text('Nível')
        ],

        [
            Radio('Adm',
                  1
                  ),

            Radio('Comum',
                  1,
                  default=True
                  )
        ],

        [
            HSeparator()
        ],

        [
            Button('VOLTAR')
        ]
    ]

    layout_baixo_d = [
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
            Push(),

            Button('CADASTRAR')
        ]
    ]

    layout_baixo =[
        [
            Column(layout_baixo_e),

            VSeparator(),

            Column(layout_baixo_d)
        ]
    ]

    layout_cima = [
        [
            Column(layout_cima_e),

            VSeparator(),

            Column(layout_cima_d)
        ]
    ]

    layout = [
        [
            Frame('CADASTRAR USUÁRIO',
                  layout_cima)
        ],

        [
            Frame('CONTA',
                  layout_baixo)
        ]
    ]
    return Window('CADASTRAR',
                  layout=layout,
                  )

janelacadastro = janela_cadastro()

while True:
    eventos, valores = janelacadastro.read()

