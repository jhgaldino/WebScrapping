from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


url = "http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar"
option = Options()
option.headless = True
driver = webdriver.Firefox()
 
# Abrindo o site
driver.get(url)
 
# localizando o no botão da versão mais recente a partir do nome da classe
link = driver.find_element_by_class_name("alert-link")
 
# clicando no botão
link.click()

try:
   #esperar 5 segundos, localizar e  clicar no botão de abrir o pdf via nome da classe
    element = WebDriverWait(driver,5).until(
       EC.presence_of_element_located((By.CLASS_NAME,"btn.btn-primary.btn-sm.center-block"))
    )
    element.click()
   #esperar 5 segundos, localizar e  clicar no botão de download via nome da classe
    element = WebDriverWait(driver,5).until(
       EC.presence_of_element_located((By.ID,"download"))
    )
    element.click()
#sair do navegador
except:
    driver.quit()