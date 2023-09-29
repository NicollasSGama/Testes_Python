from PySimpleGUI import (
    Window, FileBrowse
)

layout = [
    [
        FileBrowse(enable_events=True)
    ]
]
window = Window('Exemplo', layout=layout)
window.read()
window.close()