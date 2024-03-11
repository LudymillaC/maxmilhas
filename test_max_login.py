import pytest
from selenium import webdriver

@pytest.fixture
def driver():
  driver = webdriver.Chrome()
  yield driver
  driver.quit()

def test_valid_login(driver):
  driver.get("https://www.maxmilhas.com.br/login")
  
  #Inserir usuário e senha válidos 
  username_field = driver.find_element_by_id("email")
  username_field.send_keys("usuario@email.com")

  password_field = driver.find_element_by_id("senha") 
  password_field.send_keys("senha")

  login_button = driver.find_element_by_class_name("btn")
  login_button.click()

  assert "Usuário logado" in driver.page_source

def test_invalid_login(driver):
  driver.get("https://www.maxmilhas.com.br/login")

  #Inserir usuário ou senha inválidos
  username_field = driver.find_element_by_id("email")
  username_field.send_keys("usuario_invalido@email.com")

  password_field = driver.find_element_by_id("senha")
  password_field.send_keys("senha_invalida")

  login_button = driver.find_element_by_class_name("btn")
  login_button.click()

  assert "Usuário ou senha inválidos" in driver.page_source