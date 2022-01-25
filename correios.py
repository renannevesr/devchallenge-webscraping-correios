from selenium import webdriver
from webdriver_manager.chrome import *
import time

cep = input(' Insira o cep:')
browser = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://buscacepinter.correios.com.br/app/endereco/index.php'
browser.get(url)
time.sleep(2)
Acessar = browser.find_element_by_xpath(
    '//*[@id="endereco"]')
time.sleep(2)
Acessar.send_keys(cep)
time.sleep(2)
pesquisa = browser.find_element_by_xpath(
    '//*[@id="btn_pesquisar"]')
pesquisa.click()
time.sleep(2)
try:
    logradouro = browser.find_element_by_xpath(
        '//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
    bairro = browser.find_element_by_xpath(
        '//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
    localidade = browser.find_element_by_xpath(
        '//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
    print(logradouro, bairro, localidade)
except:
    print('CEP não encontrado')
