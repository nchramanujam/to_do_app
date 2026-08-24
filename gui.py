import functions
import FreeSimpleGUI as sg

layout = [
    [sg.Text("My Todo List")],
    [sg.Input(tooltip="Enter Todo"), sg.Button("Add")]
]

window = sg.Window("My Todo list", layout)
window.read()
window.close()