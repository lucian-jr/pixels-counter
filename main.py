import os
import requests
import numpy as np

from fastapi import FastAPI
from pydantic import BaseModel
from PIL import Image

app = FastAPI()

imgBaseURL = "https://www.meucopoeco.com.br/uploads/python/"

# MODEL
class Item(BaseModel) : 
    id: int
    file_name: str
    black_pixels: int = 0

@app.get("/")
def home() :
    return {"message": "API com FastAPI funcionando!"}

# Verifica quantos picels a imagem tem
@app.post("/verifyPixels/")
def create_item(item: Item):
    url = f"{imgBaseURL}{item.file_name}"

    try:
        # Fazendo a requisição para o link
        resposta = requests.get(url, stream=True)
        resposta.raise_for_status()

        with open(item.file_name, "wb") as arquivo:
            for chunk in resposta.iter_content(chunk_size=8192):
                arquivo.write(chunk)

        # Abrindo a imagem
        image = Image.open(item.file_name).convert("L")
        image_array = np.array(image)

        # Contar pixels pretos
        black_pixels = int(np.sum(image_array == 0))  # Converter para int
        item.black_pixels = black_pixels
        
        # Excluindo a imagem local
        os.remove(item.file_name)

        # Retornar resposta
        return {"message": "Sucess", "item": item.dict()}

    except requests.exceptions.RequestException as e:
        return {"message": "Erro ao baixar a imagem", "error": str(e)}

    except IOError as e:
        return {"message": "Erro ao processar a imagem", "error": str(e)}