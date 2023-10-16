# Criar uma tela
# Atribuir dados
# Salvar no txt

from PySimpleGUI import (
    Text, Input, Button, Column,
    HSeparator, VSeparator, Push,
    Window, Frame, CalendarButton,
    theme, popup
)


def janela_atividade():
    theme('BluePurple')

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
            Input(key='-CPF-',
                  size=(34, 1)
                  ),

            Button('CHECAR',
                   key='CPF_B'
                   ),
        ],

        [
            HSeparator()
        ],

        [
            Button('FECHAR',
                   key='-FECHAR-'
                   )
        ]
    ]

    layout_direito = [
        [
            Text('Senha')
        ],

        [
            Input(key='-SENHA-',
                  password_char='*'
                  )
        ],

        [
            Text('Senha (Confirmar)')
        ],

        [
            Input(key='-SENHA_C-',
                  password_char='*'
                  )
        ],

        [
            Text('Data de nascimento')
        ],

        [
            Input(readonly=True,
                  enable_events=True,
                  key='-CALENDARIO-',
                  size=(30, 1)
                  ),

            CalendarButton('CALENDÁRIO',
                           default_date_m_d_y=(1, 1, 2000),
                           format='%d/%m/%Y',
                           close_when_date_chosen=False,
                           key='-CALENDARIO_B-'
                           ),
        ],

        [
            HSeparator()
        ],

        [
            Push(),

            Button('REGISTRAR',
                   key='-REGISTRAR-'
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
                  layout,
                  )


janela = janela_atividade()

while True:
    eventos, valores = janela.read()
    match eventos:
        case '-REGISTRAR-':
            nome = valores['-NOME-']
            sobrenome = valores['-SOBRENOME-']
            with open('Dados.txt, a+') as file:
                file.write(f'{nome} {sobrenome}')
                popup('Registro realizado!')
        case '-FECHAR-' | None:
            break

janela.close()
