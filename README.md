# Back Ecom

Este projeto é uma **API REST** robusta para um sistema de e-commerce, desenvolvido com foco em **segurança, organização e escalabilidade**. Durante o desenvolvimento apliquei as melhores práticas e utilizando diversas ferramentas para garantir um backend sólido.

## Funcionalidades

- **Autenticação Segura**:  
  Utilização do **Flask-Login** para gerenciamento de sessões e **Werkzeug Security** para o hash de senhas, garantindo que as credenciais dos usuários sejam armazenadas de forma segura.

- **Banco de Dados Relacional**:  
  Modelagem do banco utilizando **Flask-SQLAlchemy**, com definição das relações entre usuários, produtos e itens do carrinho, otimizando consultas e garantindo a integridade dos dados.

- **Gerenciamento de Produtos**:  
  Implementação de um CRUD completo para produtos, com buscas otimizadas e controle de permissões.

- **Carrinho de Compras Dinâmico**:  
  Estrutura que permite adicionar, remover e listar itens no carrinho, com operações restritas a usuários autenticados.

- **Controle de Acesso**:  
  Proteção de rotas sensíveis com **Flask-Login**, permitindo que apenas usuários autenticados executem ações críticas, como finalizar compras.

- **Suporte a CORS**:  
  Integração com **Flask-CORS** para permitir requisições de diferentes origens, facilitando a futura integração com um frontend.

- **Documentação e Testes**:  
  Uso do **Postman** para gerenciar a documentação da API e testar os endpoints, garantindo uma comunicação clara e uma entrega organizada.

## Tecnologias Utilizadas

- **Flask** – Framework web para Python.
- **Flask-SQLAlchemy** – ORM para modelagem e manipulação do banco de dados.
- **Flask-Login** – Gerenciamento de autenticação de usuários.
- **Flask-CORS** – Suporte a requisições cross-origin.
- **Werkzeug Security** – Hash de senhas.
- **Postman** – Documentação e testes da API.

## Instalação

### Pré-requisitos

- Python 3.x instalado
- Git instalado

### Passos para configurar o ambiente

1. **Clone o repositório**

```bash
   git clone https://github.com/marcusgarim/back_ecom.git
   cd back_ecom
```

2. **Crie e ative um ambiente virtual**

    - No Windows:

        `python -m venv venv venv\Scripts\activate`

    - No macOS/Linux:

        `python3 -m venv venv source venv/bin/activate`

3. **Instale as dependências**

    Certifique-se de que o arquivo `requirements.txt` está presente na raiz do projeto e execute:

    `pip install -r requirements.txt`

4. **Configuração das variáveis de ambiente**

    Se o projeto utilizar variáveis de ambiente (como a chave secreta do Flask ou configurações de banco de dados), crie um arquivo `.env` na raiz do projeto e defina os valores necessários. Por exemplo:

    `FLASK_APP=app.py FLASK_ENV=development SECRET_KEY=your_secret_key DATABASE_URL=your_database_url`

5. **Execute a aplicação**

    Após a instalação e configuração, execute o servidor:

    `flask run`

    A API estará disponível em `http://127.0.0.1:5000`.

## Testando a API

Utilize o Postman para importar a coleção de endpoints (disponibilizada no projeto) e testar a comunicação com a API. Dessa forma, é possível verificar as respostas e garantir que todos os endpoints estejam funcionando conforme o esperado.

## Conclusão

Este projeto me proporcionou um aprendizado prático e aprofundado na construção de um backend robusto e escalável. Com a implementação de soluções de autenticação, gerenciamento de banco de dados e controle de acesso, além do uso de ferramentas essenciais como o Postman para documentação e testes, foi possível desenvolver uma API que atende a demandas reais de um sistema de e-commerce.