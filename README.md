#  Cashback

Aplicação web **simular e consultar cashback de compras**, construída com FastAPI no backend e HTML/CSS/JS puro no frontend. Os resultados de cada consulta são persistidos em um banco de dados MySQL.

> Projeto desenvolvido por **Eduardo Araújo Nóbrega** como parte do processo seletivo da **Nology**.

**Demo online:** https://cashback-henna-three.vercel.app 
O servidor, por ser hospedado gratuitamente, pode limitar o número de conexões e não funcionar sob estresse



## Tecnologias utilizadas

**Backend**
- [Python 3.12](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/)
- [Pydantic](https://docs.pydantic.dev/) (validação dos dados de entrada)

**Frontend**
- HTML5
- CSS3
- JavaScript (puro, sem frameworks)

**Banco de dados*
- MySQL

**Deploy**
- Deploy via [Vercel](https://vercel.com/)


## Pré-requisitos

- Python 3.12 ou superior
- Acesso a um banco de dados MySQL (local ou remoto)
-  `pip`

## Instalação e execução local

1. Clone o repositório:
   ```bash
   git clone https://github.com/EduardoAraujo265/Cashback.git
   cd Cashback
   ```

2. Instale as dependências:

   **Usando uv (recomendado):**
   ```bash
   uv sync
   ```

   **Usando pip:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
   ou, em modo de desenvolvimento (com reload automático):
   ```bash
   uvicorn index:app --reload
   ```
3. Execute a aplicação:
   ```bash
   python index.py
   ```
   ou, em modo de desenvolvimento (com reload automático):
   ```bash
   fastapi run index.py --reload
   ```


4. Acesse no navegador: http://localhost:8000

## Endpoints da API

Método

 `GET`  `/` Retorna a página principal (`index.html`) 
 `GET`  `/consultas`  Retorna o histórico de consultas feitas pelo IP da requisição 
 `POST`  `/cashback` Calcula o cashback, salva a consulta e retorna confirmação 


## Autor

**Eduardo Araújo Nóbrega**
[GitHub](https://github.com/EduardoAraujo265)
