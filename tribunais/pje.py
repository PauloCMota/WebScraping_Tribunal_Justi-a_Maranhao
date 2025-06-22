from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from utils.credentials import get_credentials

def acessar_expediente(tj_prefix, data_busca):
    user, password = get_credentials(tj_prefix)
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)

    try:
        driver.get("https://pje.tjma.jus.br/pje/login.seam")
        wait = WebDriverWait(driver, 20)

        # Espera o campo de username aparecer
        username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
        username_input.clear()
        username_input.send_keys(user)

        # Espera o campo de senha aparecer
        password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
        password_input.clear()
        password_input.send_keys(password)

        # Espera o botão de login e clica
        login_btn = wait.until(EC.element_to_be_clickable((By.ID, "loginButton")))
        login_btn.click()

        # Aguarda pós-login (ajuste conforme necessário, pode ser uma tela, ou algum seletor novo)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # TODO: Você deve adicionar aqui a lógica real para navegar até a aba "expediente" e extrair os prazos.
        # O exemplo abaixo é fictício.
        prazos_hoje = []
        # Exemplo fictício, ajuste conforme o sistema real:
        # expedientes = driver.find_elements(By.CSS_SELECTOR, ".expediente-row")
        # for exp in expedientes:
        #     data_prazo = exp.find_element(By.CSS_SELECTOR, ".data-prazo").text
        #     if data_prazo == data_busca:
        #         processo = exp.find_element(By.CSS_SELECTOR, ".processo-numero").text
        #         descricao = exp.find_element(By.CSS_SELECTOR, ".descricao").text
        #         prazos_hoje.append({
        #             "processo": processo,
        #             "prazo": data_prazo,
        #             "descricao": descricao
        #         })
        return prazos_hoje
    finally:
        driver.quit()