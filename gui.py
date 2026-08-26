import functions
import FreeSimpleGUI as sg
import layout as l
import time


window = sg.Window("My Todo App", layout = [[l.clock],[l.label],
                                            [l.input, l.add_button],
                                            [l.list_box, l.edit_button , l.delete_button], [l.exit_button]],
                   font=("Helvetica", 12))

while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select item", font=("Helvetica", 12))
        case "todos":
            window['todo'].update(value = values['todos'][0])
        case "Complete":
            try:
                todo_to_delete = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_delete)
                todos.pop(index)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select item",  font=("Helvetica", 12))
        case "Exit":
            exit()
        case sg.WIN_CLOSED:
            break

window.close()