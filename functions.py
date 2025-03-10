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

def logar(driver):
    login = driver.find_element(By.ID,'nav-link-accountList')
    login.click()
    email = driver.find_element(By.NAME,'email')
    email.send_keys('gabrielfeliperm3@gmail.com')
    email.send_keys(Keys.RETURN)
    password = driver.find_element(By.NAME,'password')
    password.send_keys('gati2913')
    password.send_keys(Keys.RETURN)

def carregarTela(driver):
    while True:
        try:
          WebDriverWait(driver,1).until(
              EC.visibility_of_element_located((By.NAME,'field-keywords'))
          )
          break
        except:
            pass


def adicionarPedidos(pedidos,driver):
    for pedido in pedidos:
      pesquisa = driver.find_element(By.NAME,'field-keywords')
      pesquisa.send_keys(pedido)
      pesquisa.send_keys(Keys.RETURN)

      livro = driver.find_element(By.CLASS_NAME,'s-image')
      livro.click()

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

# def confirmarPedido(driver):
#     confirmar = driver.find_element(By.CLASS_NAME,'a-button-text')
#     confirmar.click()


def encerrar(driver):
    input('Sair')
    driver.close()