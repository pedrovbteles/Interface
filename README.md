Tela de Login com PySimpleGUI
Este projeto é um exemplo simples de uma tela de login desenvolvida com a biblioteca PySimpleGUI, utilizando interface gráfica em Python.

Como usar
Clone este repositório ou baixe o arquivo .py.

Certifique-se de ter o PySimpleGUI instalado:
pip install PySimpleGUI

Execute o script Python:
python nome_do_arquivo.py

Uma janela será exibida pedindo usuário e senha.

Digite as credenciais:
Usuário: admin
Senha: 123

Clique em Entrar:
Se correto → aparece popup de sucesso.
Se incorreto → aparece popup de erro.

Layout
import PySimpleGUI as sg
sg.theme('DarkBlue')
layout = [
 [sg.Text('Usuário'), sg.Input(key='usuario', size=20)],
 [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
 [sg.Checkbox('Salvar o login?')],
 [sg.Button('Entrar')]
]
janela = sg.Window('Tela de login', layout)

Como funciona o código
Importa o PySimpleGUI:
import PySimpleGUI as sg

Define o layout da janela com os campos de usuário, senha, checkbox e botão.

Cria a janela:
janela = sg.Window('Tela de login', layout)

Loop de eventos:
while True:
 eventos, valores = janela.read()
 if eventos == sg.WIN_CLOSED:
  break
 if eventos == 'Entrar':
  if valores['usuario'] == 'admin' and valores['senha'] == '123':
   sg.popup('Login realizado com sucesso!')
  else:
   sg.popup('Usuário ou senha incorretos.')

Observações
Você pode personalizar os dados de login alterando os valores 'admin' e '123' no código.

Este é um exemplo básico de validação de login sem conexão com banco de dados.

