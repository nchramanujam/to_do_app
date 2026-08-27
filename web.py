import streamlit as st

import functions

def add_todo():
    add_todo = st.session_state["add_todo"] + "\n"
    todos.append(add_todo)
    functions.write_todos(todos)

todos = functions.get_todos()
st.title("Todos App")

for todo in todos:
    st.checkbox(todo)

st.text_input(label='',placeholder="Add new Todos", on_change=add_todo, key="add_todo")


st.session_state