from PySimpleGUI import (
    theme
)
# ---------------------------------------------
# Variáveis universais
# ---------------------------------------------
tema = 'BluePurple'

# ---------------------------------------------
# janelaCadastro
# ---------------------------------------------
meses = [
         'Janeiro', 'Fevereiro', 'Março',
         'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro',
         'Outubro', 'Novembro', 'Dezembro'
         ]
# -------------
dias = [
        'Dom', 'Seg', 'Ter',
        'Qua', 'Qui', 'Sex',
        'Sab'
        ]
# -------------
lista_cargo = [
    'Administrador',
    'Funcionário',
    'Motorista',
    'Financeiro'
    ]
# -------------
lista_carga = [
    'Carga de 4h',
    'Carga de 6h',
    'Carga de 8h'
    ]
# ---------------------------------------------
# janelaPrincipal
# ---------------------------------------------
menu = [
    ['&Relatório',
     ['Atrasos/Faltas',
      ['Gráficos',
       'Lista'
       ],
      'Hora-Extra',
      ['Gráficos',
       'Lista'
       ],
      ]
     ],

    ['&Ponto',
     ['Entrada',
      ['Entrada',
       'Saída',
       'Hora-Extra'
       ],
      'Almoço',
      ['Saída-Almoço',
       'Volta-Almoço'
       ],
      ]
     ],

    ['&Listar',
     ['Funcionários',
      ['Hora-Extra'
       ]
      ]
     ],

    ['&Sobre',
     ['Autores'
      ]
     ]
]
# ---------------------------------------------