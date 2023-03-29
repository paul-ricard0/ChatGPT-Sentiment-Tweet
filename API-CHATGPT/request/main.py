import os, dotenv
import requests

dotenv.load_dotenv()
CHAVE_API = os.getenv("CHAVE_API", None)   

def analise_sentimento(texto: str) -> str:
    
 
    modelo_engine = "text-davinci-003" 
    
    comando = f"Responda em única palabra, sendo positivo, negativo ou neutro o sentimento contidono seguinte texto:{texto}"
    
    cabecalho = {
        "Content-Type": "applivation/json",
        "Authorization": f"Bearer {CHAVE_API}"
    }
    
    dados = {
        "prompt": comando,
        "temperature": 0.7,
        "max_tokens": 35, 
        "n": 1, 
        "stop": None 
    }
    
    resposta = requests.post(
        url=f"https://api.openai.com/v1/engines/{modelo_engine}/completions",
        headers=cabecalho,
        json=dados
    )
    
    print(resposta.json())



analise_sentimento('Adorei este produto!')

 
"""
modelo_engine você consegue pegar https://platform.openai.com/playground em model
comando é o prompt que passamos para o chatgpt

cabecalho passo os parâmetros padrão de acesso para fazer a requisição
"""
