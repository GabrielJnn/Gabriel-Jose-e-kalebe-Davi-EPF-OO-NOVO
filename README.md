# 🌱 PlantsVsTime - Sistema de Gerenciamento de Plantas

**PlantsVsTime** é uma aplicação web desenvolvida em Python usando o framework Bottle para ajudar você a cuidar melhor das suas plantas! O sistema permite cadastrar plantas, registrar regas e acompanhar quando cada planta precisa ser regada novamente.

## ✨ Funcionalidades Principais

### 🌿 Gerenciamento de Plantas
- ✅ **Cadastrar plantas** com nome, espécie e intervalo de rega
- ✅ **Editar informações** das plantas
- ✅ **Excluir plantas** do sistema
- ✅ **Listar todas as plantas** organizadamente

### 💧 Sistema de Regas Inteligente
- ✅ **Registrar regas** das plantas
- ✅ **Cálculo automático** da próxima rega baseada no intervalo configurado
- ✅ **Indicadores visuais** por status:
  - 🟢 Verde: Planta ok (mais de 2 dias para regar)
  - 🟡 Amarelo: Regar em breve (1-2 dias)
  - 🔴 Vermelho: Urgente regar (hoje ou atrasada)

### 👥 Sistema de Usuários
- ✅ **Cadastro de usuários** com email e senha
- ✅ **Login seguro** com sessões
- ✅ **Cada usuário vê apenas suas próprias plantas**

### 🎨 Interface Moderna
- ✅ **Design responsivo** que funciona no celular e desktop
- ✅ **Interface intuitiva** com ícones e cores
- ✅ **Feedback visual** para todas as ações

## 🚀 Tecnologias Utilizadas

- **Backend:** Python 3.13+
- **Framework Web:** Bottle (microframework leve)
- **Banco de Dados:** Arquivos JSON (simples e educativo)
- **Frontend:** HTML5, CSS3, JavaScript básico
- **Arquitetura:** MVC (Model-View-Controller)

## 📁 Estrutura do Projeto

```
PlantsVsTime/
├── main.py              # Arquivo principal de inicialização
├── app.py               # Configuração da aplicação Bottle
├── config.py            # Configurações do sistema
├── requirements.txt     # Dependências Python
├── README.md           # Este arquivo
│
├── controllers/         # Controladores (lógica das rotas)
│   ├── base_controller.py
│   ├── plant_controller.py
│   ├── auth_controller.py
│   └── watering_controller.py
│
├── models/             # Modelos de dados (classes)
│   ├── user.py
│   ├── plant.py
│   └── watering_record.py
│
├── services/           # Lógica de negócio e persistência
│   ├── user_service.py
│   ├── plant_service.py
│   ├── watering_service.py
│   └── json_service.py
│
├── views/              # Templates HTML (páginas)
│   ├── layout.tpl      # Layout base
│   ├── home.tpl        # Página inicial
│   ├── login.tpl       # Página de login
│   ├── register.tpl    # Cadastro de usuário
│   ├── plants_list.tpl # Lista de plantas
│   ├── plant_form.tpl  # Formulário de planta
│   └── watering_form.tpl
│
├── static/             # Arquivos estáticos
│   ├── css/
│   │   └── style.css   # Estilos CSS
│   └── img/
│       └── BottleLogo.png
│
└── data/               # Banco de dados JSON
    ├── users.json      # Dados dos usuários
    ├── plants.json     # Dados das plantas
    └── waterings.json  # Histórico de regas
```

## ▶️ Como Executar o Projeto

### Pré-requisitos
- Python 3.13 ou superior
- Navegador web moderno

### Passo a Passo

1. **Clone ou baixe o projeto**
   ```bash
   git clone https://github.com/GabrielJnn/Gabriel-Jose-e-kalebe-Davi-EPF-OO-NOVO.git
   cd PlantsVsTime
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o servidor**
   ```bash
   python main.py
   ```

5. **Abra no navegador**
   ```
   http://localhost:8080
   ```

## 👤 Como Usar

### Primeiro Acesso
1. Acesse `http://localhost:8080`
2. Clique em "Criar Conta" para se cadastrar
3. Faça login com seu email e senha

### Gerenciando Plantas
1. Na página inicial, clique em "Ver Minhas Plantas"
2. Clique em "Adicionar Planta" para cadastrar uma nova
3. Preencha:
   - **Nome:** Nome da planta (ex: Orquídea)
   - **Espécie:** Tipo da planta (ex: Flor)
   - **Frequência:** A cada quantos dias regar (ex: 3)

### Registrando Regas
1. Na lista de plantas, clique em "Ver Detalhes" de uma planta
2. Clique em "Registrar Rega" ou "Registrar Primeira Rega"
3. Confirme que regou a planta hoje

### Acompanhando Status
- **Verde:** Planta saudável, regar em mais de 2 dias
- **Amarelo:** Regar em breve (1-2 dias)
- **Vermelho:** Urgente regar (hoje ou atrasada)
- **Cinza:** Nunca foi regada

## 🎓 Sobre o Projeto

Este projeto foi desenvolvido como trabalho acadêmico para demonstrar os conceitos de **Programação Orientada a Objetos (POO)** aplicados ao desenvolvimento web.

### Conceitos Demonstrados
- ✅ **Classes e Objetos** (Models)
- ✅ **Encapsulamento** (Services)
- ✅ **Herança** (BaseController)
- ✅ **Polimorfismo** (diferentes tipos de rotas)
- ✅ **MVC** (Model-View-Controller)
- ✅ **Persistência de Dados** (JSON)
- ✅ **Tratamento de Exceções**
- ✅ **Validação de Dados**

## 🤝 Contribuição

Para contribuir com o projeto:

1. Faça um Fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'feat: adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto é de uso educacional e pode ser utilizado livremente para fins de aprendizado.

## 👨‍💻 Autor

**Gabriel José e Kalebe Davi**

Projeto desenvolvido para a disciplina de Programação Orientada a Objetos.

---

**🌱 Nunca esqueça de regar suas plantas com o PlantsVsTime!** 💚
