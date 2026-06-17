##imports
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse, FileResponse
import mysql.connector
import datetime 
from pydantic import BaseModel

## classe pra receber o corpo da requisição através do "fetch()" do javascript 
class CashbackRequest(BaseModel):
    valor: float
    vip: bool

## try para inicialização do servidor e conexão com o banco de dados MySQL
try :
    ## conexão com o banco de dados MySQL
    # carregando dotenv 
    load_dotenv()

    myconn =mysql.connector.connect(
            host= os.getenv('host'),
            user=os.getenv('user'),
            password=os.getenv('pass'),
            database=os.getenv('db'),
            port=os.getenv('port'))
    
    ## query de criação da tabela "consultas cashback" caso ela não exista
    query = """CREATE TABLE IF NOT EXISTS consultas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vip BOOLEAN NOT NULL DEFAULT FALSE,
    valor FLOAT NOT NULL,
    cashback FLOAT NOT NULL,
    data DATETIME NOT NULL,
    ip VARCHAR(45)
    );"""
    cursor = myconn.cursor()
    cursor.execute(query)
    print ("LOG:Tabela existe ou foi criada com sucesso!")
except mysql.connector.Error as err:
    print("ERROR: {}".format(err)) 

app = FastAPI()

## /servindo arquivos para o frontend
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r") as f:
        return HTMLResponse(content=f.read())
    
@app.get("/script.js")
async def get_script():
    return FileResponse("script.js", media_type="application/javascript")

@app.get("/style.css")
async def get_style():
    return FileResponse("style.css", media_type="text/css")
## começando os endpoints/
@app.get("/consultas")
async def consultas(request: Request):
    try:
        ## consulta o banco
        cursor = myconn.cursor(dictionary=True)
        query = "SELECT vip, valor, cashback FROM consultas WHERE ip = %s"
        cursor.execute(query, (request.client.host,))
        results = cursor.fetchall()
        ## transforma boolean em sim ou não para exibição no frontend
        for consulta in results:
            if consulta['vip']:
                consulta['vip'] = 'Sim'
            else:
                consulta['vip'] = 'Não'
        return results
    
    except mysql.connector.Error as err:
        print("ERROR: {}".format(err))
        return {"error": str(err)}

@app.post("/cashback", status_code=201)
async def cashback(valor: CashbackRequest,request: Request):
    ## calcula cashback
    cashback = valor.valor * 0.05 
    if valor.valor > 500:
            cashback = cashback * 2
    if valor.vip == True:
        cashback += cashback * 0.10
    
    try:
        ## obtendo data e formatando
        datetime_now = datetime.datetime.now()
        strftime = datetime_now.isoformat()
        cursor = myconn.cursor()
        query = "INSERT INTO consultas (vip, valor, cashback, data, ip) VALUES (%s, %s, %s, %s, %s)"
        values = (valor.vip, valor.valor, cashback, datetime_now, request.client.host)
        cursor.execute(query, values)
        myconn.commit()
        print("LOG: Consulta de cashback inserida com sucesso!")
        return {"message": "created"} 
    except mysql.connector.Error as err:
        return {"ERROR": str(err), "message": "Erro ao inserir consulta de cashback"}
        print("ERROR: {}".format(err)) 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 