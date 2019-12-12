  **SIMIAN API**

**/stats**

O recurso de stats retorna a estatística de DNA's humanos, simíos e proporção de símios para a população humana. A API faz a leitura dos registros em uma tabela no DynamoDB.

`GET https://u85iq28rf0.execute-api.us-east-1.amazonaws.com/prd/stats`

**/simian**

O recurso valida o DNA informado no request, identificando se há repetições em diferentes sequencias da matriz para as sequências de A, T, C ou G. Retorna o http code 200 (símio) ou 403 (humano), além disso, retorna um JSON com a propriedade `simian` com `true` ou `false`. 

`POST https://u85iq28rf0.execute-api.us-east-1.amazonaws.com/prd/simian`

Body request:


    {
        "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
    }
  
**Requisitos**

- Python >= 3.6
- Pip
- AWS CLI

**Dependências**

- boto3
- botocore
- Flask

**Executando a aplicação**

Antes de rodar a aplicação, tenha o AWS CLI configurado no ambiente onde será reproduzida.

No terminal, rode o seguinte comando para instalar todas as dependências da aplicação:

`python3.6 -m pip install -r requirements.txt` ou `pip install -r requirements.txt`

Para executar a aplicação:

`python3.6 application.py` ou `python application.py`

Por default, a aplicação subirá no `localhost:5000`.

**Tabela**

Tenha uma tabela NoSQL com a seguinte estrutura:

    {
        "key": "string",
        "type": "string"
    }