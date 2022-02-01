from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from PySimpleGUI import PySimpleGUI as sg

option = Options()
option.headless = True


def pesquisa():
    browser = webdriver.Firefox(options=option)
    url = 'https://buscacepinter.correios.com.br/app/endereco/index.php'
    browser.get(url)
    browser.implicitly_wait(1)
    Acessar = browser.find_element(By.XPATH, '//*[@id="endereco"]')
    Acessar.send_keys(cep)
    pesquisa = browser.find_element(By.XPATH,
                                    '//*[@id="btn_pesquisar"]')
    pesquisa.click()
    browser.implicitly_wait(2)

    try:
        logradouro = browser.find_element(By.XPATH,
                                          '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
        bairro = browser.find_element(By.XPATH,
                                      '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
        localidade = browser.find_element(By.XPATH,
                                          '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
        janela.FindElement('_output_').Update('')
        print("Logradouro: " + logradouro)
        print("Bairro: " + bairro)
        print("Cidade: " + localidade)
    except:
        janela.FindElement('_output_').Update('')
        print('CEP não encontrado')


sg.theme('LightGrey2')
layout2 = [
    [sg.Text('Cep'), sg.Input(key='CepPesquisa')],
    [sg.Output(size=(40, 10), key='_output_')],
    [sg.Button('Pesquisar'), sg.Button('Limpar')]
]
janela = sg.Window('Busca de cep', layout2)
while True:
    eventos, valores = janela.read() 
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Pesquisar':
        cep = valores['CepPesquisa']
        print("Aguarde estamos localizando o CEP")
        pesquisa()
    if eventos == 'Limpar':
        janela.FindElement('_output_').Update('')
