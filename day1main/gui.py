import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type of To_Do")
input_box = PySimpleGUI.InputText(tooltip="Enter To Do", key= "todo")
add_button = PySimpleGUI.Button("Add")

window=PySimpleGUI.Window('My To-Do List',
                          layout = [[[label], [input_box, add_button]]],
                          font=('Helvertica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event :
        case 'Add' :
            todos = functions.get_store()
            new_todos = values['todo'] + '\n'
            todos.append(new_todos)
            functions.write_store(todos)
        case PySimpleGUI.WINDOW_CLOSED :
            break

window.close()