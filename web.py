import streamlit as st

import functions

def add_todo():
    add_todo = st.session_state["add_todo"] + "\n"
    todos.append(add_todo)
    functions.write_todos(todos)

todos = functions.get_todos()
st.title("Todos App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='',placeholder="Add new Todos", on_change=add_todo, key="add_todo")


st.session_state