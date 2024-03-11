
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

# Iniciar navegador
driver = webdriver.Chrome()

# Acessar site
driver.get("https://www.siteweb.com.br")

# Preencher campos da busca
quartos = driver.find_element(By.ID, "quartos")
quartos.send_keys("1") 

adultos = driver.find_element(By.ID, "adultos")  
adultos.send_keys("2")

destino = driver.find_element(By.ID, "destino")
destino.send_keys("Destino")

data_checkin = driver.find_element(By.ID, "data_checkin")
data = datetime.datetime.now() + datetime.timedelta(days=30)
data_checkin.send_keys(data.strftime("%d/%m/%Y"))

# Clicar em pesquisar
btn_pesquisar = driver.find_element(By.ID, "btnPesquisar")
btn_pesquisar.click()

# Filtrar por preço
preco_minimo = driver.find_element(By.ID, "precoMinimo")  
preco_minimo.send_keys("100")

preco_maximo = driver.find_element(By.ID, "precoMaximo")
preco_maximo.send_keys("200")

# Validar filtro aplicado
resultado = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "resultado"), "R$ 100 - R$ 200")
)

# Finalizar navegador
driver.quit()