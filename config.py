# config.py - Configurações da aplicação PlantsVsTime
# Este arquivo contém todas as configurações do sistema

import os

class Config:
    # Diretório base do projeto (onde está localizada a pasta raiz)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # === CONFIGURAÇÕES DO SERVIDOR ===
    # Endereço onde o servidor vai rodar (localhost = só na sua máquina)
    HOST = 'localhost'
    # Porta do servidor (8080 é comum para desenvolvimento)
    PORT = 8080
    # Ativar modo debug (mostra erros detalhados)
    DEBUG = True
    # Recarregar automaticamente quando arquivos mudam
    RELOADER = True

    # === CAMINHOS DOS ARQUIVOS ===
    # Pasta onde ficam os templates HTML
    TEMPLATE_PATH = os.path.join(BASE_DIR, 'views')
    # Pasta onde ficam arquivos estáticos (CSS, JS, imagens)
    STATIC_PATH = os.path.join(BASE_DIR, 'static')
    # Pasta onde ficam os arquivos de dados (JSON)
    DATA_PATH = os.path.join(BASE_DIR, 'data')

    # === OUTRAS CONFIGURAÇÕES ===
    # Chave secreta para sessões (mudar em produção!)
    SECRET_KEY = 'sua-chave-secreta-aqui'
