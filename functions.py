from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ininicializarDriver():
    driver = webdriver.Edge()
    return driver

def acessarSite(driver):
    driver.get("https://www.amazon.com.br/Livros/b?node=6740748011")

# def logar(driver):
#     login = driver.find_element(By.ID,'nav-link-accountList')
#     login.click()
#     email = driver.find_element(By.NAME,'email')
#     email.send_keys('emailteste@gmail.com')
#     email.send_keys(Keys.RETURN)
#     password = driver.find_element(By.NAME,'password')
#     password.send_keys('senhateste')
#     password.send_keys(Keys.RETURN)

def carregarTela(driver):
    while True:
        try:
          WebDriverWait(driver,1).until(
              EC.visibility_of_element_located((By.NAME,'field-keywords'))
          )
          break
        except:
            pass


def adicionarPedidos(lista,driver):
    for index, row in lista.iterrows():
      pesquisa = driver.find_element(By.NAME,'field-keywords')
      pesquisa.send_keys(row['Livros'])
      pesquisa.send_keys(Keys.RETURN)

      #Única parte que falta - preciso selecionar algo que existem em todos html
      livro = driver.find_element(By.XPATH, f'//img[@class="s-image" and @data-image-index="1"]')
      livro.click()

      while True:
          try:
              WebDriverWait(driver,1).until(
                  EC.element_to_be_clickable((By.NAME,'submit.add-to-cart'))
              )
              break
          except:
              pass
  

      carrinho = driver.find_element(By.NAME,'submit.add-to-cart')
      carrinho.click()

def finalizarPedido(driver):
    comprar = driver.find_element(By.NAME,'proceedToRetailCheckout')
    comprar.click()

def pagarComPix(driver):
   pix = driver.find_element(By.XPATH, "//*[contains(@value, 'instrumentId=amzn1.pm.pma.pix')]")
   pix.click()

def gerarQRCode(driver):
    qrcode = driver.find_element(By.CLASS_NAME,'a-button-input')
    qrcode.click()

def confirmarPedido(driver):
    while True:
        try:
          WebDriverWait(driver,1).until(
              EC.element_to_be_clickable((By.ID, 'prime-panel-fallback-button'))
          )
          break
        except:
            pass

    confirmar = driver.find_element(By.ID,'prime-panel-fallback-button')
    confirmar.click()

def clicarConfirmarPedido(driver):
    while True:
        try:
          WebDriverWait(driver,1).until(
              EC.element_to_be_clickable((By.ID, 'placeOrder'))
          )
          break
        except:
            pass

    confirmar = driver.find_element(By.ID,'placeOrder')
    confirmar.click()

   


def encerrar(driver):
    input('Sair')
    driver.close()