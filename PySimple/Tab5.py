import PySimpleGUIQt as sg

def SelectTab(self, index):
    try:
        self.QT_QTabWidget.setCurrentIndex(index)
    except :
        pass


def GetCurrent(self):
    try:
        index=self.QT_QTabWidget.currentIndex()
    except:
        index=None
    return index

sg.TabGroup.SelectTab = SelectTab
sg.TabGroup.GetCurrent = GetCurrent

Tab1=sg.Tab(layout=[[sg.Text("Tab1")],],title="Tab1")
Tab2=sg.Tab(layout=[[sg.Text("Tab2")],],title="Tab2")
Tab3=sg.Tab(layout=[[sg.Text("Tab3")],],title="Tab3")
Tabs=sg.TabGroup([[Tab1,Tab2,Tab3]], key='_TAB_GROUP_')
layout = [[sg.Text("Tab")], [Tabs], [sg.Button("SelectTab")],[sg.Button("Exit")],]
window = sg.Window("Tabs").Layout(layout).Finalize()

while True:
    event, values = window.Read()
    if event is None or event == "Exit":
        break
    elif event is None or event == "SelectTab":
        current = window.Element('_TAB_GROUP_').GetCurrent()
        # current = Tabs.GetCurrent()
        if current == 0:
            index=1
        elif current==1:
            index=0
        else: index=0

        window.Element('_TAB_GROUP_').SelectTab(index)
        # Tabs.SelectTab(index)

window.Close()