from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, HSeparator, Push,
    theme, popup
)
def janelas():
    theme('DarkPurple')

    layout_direita = [
        [
            Image(filename='teste.png',
                  key='-IMAGEM-')
        ]
    ]

    layout_esquerda = [
        [
            Text('Email:'),
            Input(key='-EMAIL-')
        ],

        [
            Text('Senha:'),
            Input(key='-SENHA-',
                  password_char='*')
        ],

        [
             Push(),
             Button('Login'),
             Push(),
             Button('Esqueci a senha'),
             Push()
        ]
    ]

    layout = [
        [
            Column(layout_direita),
            VSeparator(),
            Column(layout_esquerda)
        ]
    ]

    return Window(
        'Título da Janela',
        layout=layout,
        size=(450, 200)
    )

window = janelas()

while True:
    event, values = window.read()
    #print(event, values)
    match(event):
        case 'Login':
            popup('Login realizado!')
            window['-IMAGEM-'].update(filename='teste_2.png')
        case 'Esqueci a senha':
            popup('O seu e-mail é {}'.format('-EMAIL-'))
        case None:
            break
        case _:
            print(event, values)

window.close()
