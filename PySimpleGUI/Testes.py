from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, HSeparator, Push,
    theme, popup, FileBrowse
)

def janela_A():
    layout = [
        [
            Text('Janela A'),
            Button('Janela A'),
            Button('Janela B')
        ],

        [
            Button('Botão 2')
        ]
    ]
    return Window('Janela A', layout=layout)

def janela_B():
    layout = [
        [
            Text('Janela B'),
            Button('Janela A'),
            Button('Janela B')
        ],
    ]
    return Window('Janela B', layout=layout)

window = janela_A()

while True:
    events, values = window.read()
    match(events):
        case 'Janela A' | 'Janela B':
            window.close() # Fechar a janela antes de abrir outra para não abrir uma janela atrás da outra
            match(events): #Trocar para outra janela pois o 'events e values' são '=' a window
                case 'Janela A':
                    window = janela_B()
                case 'Janela B':
                    window = janela_A()
                case None:
                    break

window.close()