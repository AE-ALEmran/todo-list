import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type of To_Do")
input_box = PySimpleGUI.InputText(tooltip="Enter To Do")
add_button = PySimpleGUI.Button("Add")

window=PySimpleGUI.Window('My To-Do List', layout=[[[label], [input_box, add_button]]])
window.read()
window.close()