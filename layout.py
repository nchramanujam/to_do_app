import FreeSimpleGUI as sg

label =  sg.Text("Type in Todos")
input = sg.Input(tooltip="Enter Todo", key="todos")
add_button = sg.Button("Add")