import PySimpleGUI as pyg

def main_menu():
    
    layout = [[pyg.Text(text = "Welcome",
                        expand_x=True,
                        justification='center')], 
            [pyg.Button("Select Image")], 
            [pyg.Button("Close")]
            ]

    window = pyg.Window('Collector Capture Project', layout, size = (500,250))

def signup_login():
    layout4 = [
        [pyg.Text('Login and Signup')],
        [pyg.Button('Login'), pyg.Button('Signup')]
    ]
    
    window2 = pyg.Window('Login and Signup', layout4, finalize= True)
    
    while True:
        event, values = window.read()
        
        if event == 'Login':
            login()
            
        if event == 'Signup':
            signup()
        
        if event == None:
            break
        

def login():
    layout2 = [
        [pyg.Text('Username')],
        [pyg.Input(key='user')],
        [pyg.Text('Password')],
        [pyg.Input(key='pw', password_char='*')],
        [pyg.OK(),pyg.Cancel()]
    ]

    window3 = pyg.Window('login', layout2, finalize=True)
    
    while True:
        event, values = window.read()
        
        if event == pyg.OK or event == pyg.WIN_CLOSED:
            break
        username = values['user']
        password = values['pw']
        
    window3.close()
    
def signup():
    layout3 = [
        [pyg.Text('Username')],
        [pyg.Input(key='user')],
        [pyg.Text('Password')],
        [pyg.Input(key='pw', password_char='*')],
        [pyg.OK(),pyg.Cancel()]
    ]

    window2 = pyg.Window('login', layout3, finalize=True)
    
    while True:
        event, values = window.read()
        
        if event == pyg.OK or event == pyg.WIN_CLOSED:
            break
        username = values['user']
        password = values['pw']
        
    window.close()
    
signup_login()
    
    
while True:
    event, values = window.read()
    
    if event == "Select Image":
        select_file = pyg.popup_get_file('Select an image', title='Image Selector')
    
    if event == "Close" or event == pyg.WIN_CLOSED:
        break

window.close()