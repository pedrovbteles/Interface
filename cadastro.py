import PySimpleGUI as sg

# Layout
sg.theme('DarkBlue')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=20)],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Tela de login', layout)

# Loop de eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'admin' and valores['senha'] == '123':
            sg.popup('Login realizado com sucesso!')
        else:
            sg.popup('Usuário ou senha incorretos.')