from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, HSeparator, Push,
    theme, popup, Checkbox, Frame
)
def janela_contato():
    theme('LightBlue2')

    layout_meio1 = [
        [
            Text('E-mail')
        ],

        [
            Input('ex.:dorival@contato.com')
        ]

    ]

    layout_meio2 = [
        [
            Text('Telefone')
        ],

        [
            Input('ex.:(XX)96050-52XX')
        ]

    ]

    layout_baixo1 = [
        [
            Text('Rua')
        ],

        [
            Input(disabled=True)
        ],

        [
            Text('Complemento')
        ],

        [
            Input()
        ],

        [
            Text('Cep')
        ],

        [
            Input('ex.:02222-000')
        ],

        [
            HSeparator()
        ],

        [
            Button('VOLTAR'),

            Push(),

            Button('BUSCAR')
        ]
    ]

    layout_baixo2 = [
        [
            Text('Bairro')
        ],

        [
            Input(disabled=True)
        ],

        [
            Text('Cidade')
        ],

        [
            Input(disabled=True)
        ],

        [
            Text('Estado')
        ],

        [
            Input(disabled=True)
        ],

        [
            HSeparator()
        ],

        [
            Push(),

            Button('CADASTRAR')
        ]
    ]

    layout_columa_meio = [
        [
            Column(layout_meio1),

            VSeparator(),

            Column(layout_meio2)
        ],
    ]

    layout_columa_baixo = [
        [
            Column(layout_baixo1),

            VSeparator(),

            Column(layout_baixo2)
        ]
    ]

    layout = [
        [
            Frame('CONTATO',
                  layout_columa_meio),
        ],

        [
            Frame('ENDEREÇO',
                  layout_columa_baixo)
        ]
    ]

    return Window('CONTATO',
                  layout=layout,
                  )

contato = janela_contato()
contato.read()