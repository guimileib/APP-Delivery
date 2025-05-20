# APP-Delivery

API de Delivery desenvolvida em Python utilizando Flask e MongoDB, com arquitetura modular e foco em boas práticas de organização de código.

## Descrição

Este projeto implementa uma API RESTful para gerenciamento de pedidos de delivery. Utiliza Flask como framework web e MongoDB como banco de dados, com conexão gerenciada por um handler dedicado. O código é organizado em módulos para facilitar manutenção e escalabilidade.

## Requisitos

- Python 3.8+
- MongoDB em execução local (`localhost:27017`)
- As dependências listadas em `requirements.txt`

## Instalação

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd APP-Delivery
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Certifique-se de que o MongoDB está rodando localmente e possui um usuário `meuAdmin` com senha `minhaSenhaForte` no banco `rocket_db`.

## Execução

Para iniciar a API, execute:
```bash
python run.py
```
O servidor Flask estará disponível em `http://localhost:3000`.

## Estrutura do Projeto

```
APP-Delivery/
│
├── run.py                      # Ponto de entrada da aplicação
├── requirements.txt            # Dependências do projeto
└── src/
    ├── main/
    │   ├── server/             # Inicialização do Flask
    │   ├── routes/             # Definição das rotas/endpoints
    │   ├── composer/           # Compositores de casos de uso
    │   └── http_types/         # Tipos auxiliares para requisições HTTP
    ├── models/
    │   ├── connection/         # Handler de conexão com o MongoDB
    │   └── repository/         # Repositórios de acesso ao banco
    └── use_cases/              # Casos de uso da aplicação
```

## Endpoints

- **POST `/delivery/order`**  
  Cria um novo pedido.  
  Corpo esperado: JSON com os dados do pedido.

- **GET `/delivery/order/<order_id>`**  
  Busca um pedido pelo ID.

- **PATCH `/delivery/order/<order_id>`**  
  Atualiza campos de um pedido existente.

## Observações

- O projeto utiliza um padrão de repositório para abstração do acesso ao banco de dados.
- A conexão com o MongoDB é centralizada em um handler singleton.
- Os endpoints utilizam compositores para injeção de dependências e organização dos casos de uso.
- Para rodar os testes, utilize o `pytest`. 