import PySimpleGUIQt as sg


def SelectTab(self, index):
    try:
        self.QT_QTabWidget.setCurrentIndex(index)
    except:
        pass


def GetCurrent(self):
    try:
        index = self.QT_QTabWidget.currentIndex()
    except:
        pass
    return index


Tab1 = sg.Tab(layout=[[sg.Text("Tab1")], ], title="Tab1")
Tab2 = sg.Tab(layout=[[sg.Text("Tab2")], ], title="Tab2")
Tab3 = sg.Tab(layout=[[sg.Text("Tab3")], ], title="Tab3")
Tabs = sg.TabGroup([[Tab1, Tab2, Tab3]])
layout = [[sg.Text("Tab")], [Tabs], [sg.Button("SelectTab")], [sg.Button("Exit")], ]
window = sg.Window("Tabs").Layout(layout).Finalize()

while True:
    event, values = window.Read()
    if event is None or event == "Exit":
        break
    elif event == "SelectTab":
        current = GetCurrent(Tabs)
        if current == 0:
            index = 1
        elif current == 1:
            index = 0
        SelectTab(Tabs, index)
window.Close()
