# Pixels Counter

O **Pixels Counter+** é um projeto em python, desenvolvido para auxiliar na contagem dos pixels pretos de uma imagem.

## Requisitos

Para iniciar o projeto, é necessário instalar algumas bibliotecas utilizando o comando abaixo: 

    pip install fastapi uvicorn requests numpy pillow

## Passos para Configuração

1. **Inicie o servidor no terminal**: uvicorn main:app --reload.
    - Obs: É preciso rodar o comando na pasta /pixels-counter (raiz do projeto).

2. **Utilize algum software de teste de APIs**: Insomnia, Postman ou outro.

3. **API**:
    - Utilize a URL http://127.0.0.1:8000/verifyPixels/ (Porta padrão = 8000. Trocar caso a porta for diferente);
    - Método POST;
    - Body no formato JSON, utilizando os parâmetros: id e file_name;
        - id (int)
        - file_name (string)

    - File_names disponíveis para uso:
        - nada.jpg
        - pouco.jpg 
        - medio.jpg 
        - muito.jpg 
        - tudo.jpg

Após seguir esses passos, é a API irá retornar um JSON com os dados da Requisição. 
Incluindo a quantidade de pixels pretos da imagem no caso de sucesso. Assim como uma mensagem específicando um erro, caso ocorra.
