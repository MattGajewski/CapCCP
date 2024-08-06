import PySimpleGUI as pyg

layout = [[pyg.Text(text = "Welcome",
                    expand_x=True,
                    justification='center')], [pyg.Button("OK")], [pyg.Button("Select Image")]]

window = pyg.Window('Collector Capture Project', layout, size = (500,250))

while True:
    event, values = window.read()
    
    if event == "Select Image":
        select_file = pyg.popup_get_file('Select an image', title='Image Selector')
    
    if event == "OK" or event == pyg.WIN_CLOSED:
        break

window.close()