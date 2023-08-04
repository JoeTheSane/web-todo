import streamlit as st
import functions

todos_from_file = functions.get_todos()
def add_todo():
    todo_to_add = st.session_state["new_todo"] + "\n"
    todos_from_file.append(todo_to_add)
    functions.write_todos(todos_from_file)

todos = functions.get_todos()
st.title("ToDo Hero")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="input_new_todo", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")
