import functions
import FreeSimpleGUI as sg
import layout as l

window = sg.Window("My Todo App", layout = [[l.label], [l.input, l.add_button]], font=("Helvetica", 12))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todos"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()