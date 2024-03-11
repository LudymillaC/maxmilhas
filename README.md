# maxmilhas

Projeto de Testes Automatizados com Selenium (Python)
Este projeto contém casos de teste automatizados para testar funcionalidades de um site, desenvolvidos utilizando Selenium com Python.

Pré-requisitos
Python 3.7 ou superior
Selenium
ChromeDriver ou GeckoDriver
Instalação
Clone o repositório:
git clone https://github.com/user/selenium-python-project.git
Crie um ambiente virtual e ative-o:
python -m venv venv
source venv/bin/activate
Instale as dependências:
pip install -r requirements.txt
Configuração
O projeto está configurado para executar os testes no Chrome por padrão. Caso queira executar no Firefox, altere a variável browser no arquivo config.py para firefox.

Execução dos Testes
Para rodar os testes:

python -m unittest discover -s tests
É possível também executar testes individuais:

python -m unittest tests.test_login
Estrutura de Pastas
tests - Pasta contendo os casos de teste
pages - Classe Page Objects
config.py - Arquivo de configurações
requirements.txt - Dependências do projeto
Autor
Ludymilla Christina

Espero que este README ajude a configurar e executar os testes deste projeto Selenium. Fique à vontade para abrir issues caso tenha alguma dúvida ou sugestão!
