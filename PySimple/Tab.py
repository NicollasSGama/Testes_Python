import PySimpleGUI as sg
import baza # external file with my databse

sg.theme("GreenTan")

left_col = [sg.Button("Create")],[sg.Button("Read")],[sg.Button("Update")],[sg.Button("Delete")]

data = baza.get_db_obiad()
print(data)
headings2 = ['Id', 'Name', '1', '2', '3']
layout_1 = [[sg.Table(values=data[0:][:], headings=headings2, max_col_width= True,
                    auto_size_columns=False,
                    display_row_numbers=False,
                    enable_events=True,
                    justification='c',
                    alternating_row_color='lightyellow',
                    key='-TAB_1-',
                    row_height=35)]]

data1 = baza.get_db_podkladka()
headings3 = ['Id','Name']
layout_2 = [[sg.Table(values=data1[0:][:], headings=headings3, max_col_width= True,
                    auto_size_columns=False,
                    display_row_numbers=False,
                    enable_events=True,
                    justification='c',
                    alternating_row_color='lightyellow',
                    key='-TAB_2-',
                    row_height=35)]]

data2 = baza.get_db_mieso()
headings4 = ['Id','Name']
layout_3 = [[sg.Table(values=data2[0:][:], headings=headings4, max_col_width= True,
                    auto_size_columns=False,
                    display_row_numbers=False,
                    enable_events=True,
                    justification='c',
                    alternating_row_color='lightyellow',
                    key='-TAB_3-',
                    row_height=35)]]

data3 = baza.get_db_dodatki()
headings5 = ['Id','Name']
layout_4 = [[sg.Table(values=data3[0:][:], headings=headings5, max_col_width= True,
                    auto_size_columns=False,
                    display_row_numbers=False,
                    enable_events=True,
                    justification='c',
                    alternating_row_color='lightyellow',
                    key='-TAB_4-',
                    row_height=35)]]

tab_group = sg.TabGroup([[sg.Tab("Tab 1", layout_1),
                             sg.Tab("Tab 2", layout_2),
                             sg.Tab("Tab 3", layout_3),
                             sg.Tab("Tab 4", layout_4)]],
                             enable_events=True)
right_col = [[tab_group]]


layout = [[sg.Column(left_col, justification="c"), sg.Column(right_col)]]

window = sg.Window("", layout).Finalize()
window.Maximize()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Create":
        pass
    elif event == "Read":
        pass
    elif event == "Update":
        pass
    elif event == "Delete":
        if sg.popup_yes_no("Are you sure you want to delete this record?"):
            curr_sel_tab= tab_group.find_key_from_tab_name(tab_group.Get())
            print(curr_sel_tab)
        else:
            break

window.close()