import PySimpleGUI as sg
from database import db_querys as db

def delete_record(table: list, row: list, index: int) -> None:
    db.delete_db_item(table="records_data", key=row[0])
    del table[index]


window = sg.Window("Vinyl Catalogue", table_layout)

while True:
    event, values = window.read()

    if event == "-RECORDSTABLE-":
        try:
            row_index = values["-RECORDSTABLE-"][0]
            selected_row = table_array[row_index]
        except IndexError:
            continue

    if event == "-DELETERECORD-":
        try:
            delete_record(table_array, selected_row, row_index)
            window['-RECORDSTABLE-'].update(table_array)
            sg.popup(f"Deleted {selected_row[1]} {selected_row[2]}", title="Delete successful")
        except NameError:
            sg.popup_error("Please select row to delete", title="Error")


    elif event == "-EXPORTCSV":
        export_csv(table_array)

    elif event == "-QUIT-":
        break

window.close()