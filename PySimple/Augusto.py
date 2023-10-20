from PySimpleGUI import (
    WIN_CLOSED, MenubarCustom,
    Window
)


def teste():
    layout = [
        [
            MenubarCustom(
                [
                 ['Menu',
                     ['Cliente', ['Cadastro'],
                      'Financeiro',
                      'Logistica',
                      'Relatórios',
                      'Produtos',
                      'Fornecedores']
                  ]
                ],
                bar_font=(100, 20)
            )
        ]
    ]

    return Window(title='',
                  layout=layout,
                  finalize=True,
                  size=(500, 500))


janela = teste()

janela.read()
