# main.py - Arquivo principal do projeto PlantsVsTime
# Este arquivo inicia o servidor web da aplicação

from app import create_app

if __name__ == '__main__':
    # Cria a aplicação usando a factory function
    app = create_app()
    # Inicia o servidor web
    app.run()
