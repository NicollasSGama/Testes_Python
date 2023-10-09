import pandas as pd
import time
import os
import datetime as dt
import numpy as np
import PySimpleGUI as sg

tab1_layout = [
    [
        sg.T('Tab 1')
    ],

    [
        sg.InputText('data 1'),
        sg.FileBrowse('data 1 download',
                      key='file 1')
    ]
]

tab2_layout = [
    [
        sg.T('Tab 2')
    ],
    [
        sg.InputText('data 2'),
        sg.FileBrowse('data 2 download',
                      key='file 2')
    ],
]

layout = [
    [sg.TabGroup([[sg.Tab('Tab 1', tab1_layout),
                   sg.Tab('Tab 2', tab2_layout)
                   ]])],
    [sg.Button('Run'), sg.CloseButton("Cancel")]]

window = sg.Window('Multiple tabs one window').Layout(layout)


def sum_tab1(file_1):
    df = pd.read_excel(file_1)
    df["sum"] = df["column 1"] + df["column 2"]
    folder = os.path.dirname(file_1)
    writer = pd.ExcelWriter(folder + "\\sum_output.xlsx")
    df.to_excel(writer, index=False)
    writer.save()


def multiply_tab2(file_2):
    df = pd.read_excel(file_2)
    df["multiply"] = df["column 1"] * df["column 2"]
    folder = os.path.dirname(file_2)
    writer = pd.ExcelWriter(folder + "\\multiply_output.xlsx")
    df.to_excel(writer, index=False)
    writer.save()


while True:
    button, values = window.Read()
    if button in (None, "Quit", "Cancel"):
        window.Close()
        break
    elif button == 'Run':
        if values["file 1"] != "data 1":
            print("Running first tab")
            sum_tab1(values["file 1"])
            print("Output generation completed. Please Close Window")

        if values["file 2"] != "data 2":
            print("Running second tab")
            multiply_tab2(values["file 2"])
            print("Completed. Please Close Window")

window.Close()