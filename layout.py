import FreeSimpleGUI as sg
import functions

label =  sg.Text("Type in Todos")
input = sg.Input(tooltip="Enter Todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True,
                      size=[45, 10])
delete_button = sg.Button("Complete")