# Extrator de Texto em Imagem e PDF

Este é um aplicativo simples em Python que permite a leitura de documentos PDF e imagens de baixa qualidade e transcreve o texto para uma área de texto editável. É uma aplicação de desktop que utiliza a biblioteca PyQt5 para a interface gráfica e o Tesseract OCR para a extração de texto de imagens.

## Funcionalidades

- Abre arquivos PDF e imagens (JPEG, PNG) para extração de texto.
- Utiliza OCR (Reconhecimento Óptico de Caracteres) para extrair texto de imagens.
- Exibe o texto extraído em uma área de texto editável, permitindo a cópia para outros fins.

## Pré-requisitos

- Python 3.x
- PyQt5
- Tesseract OCR
- PIL (Python Imaging Library)
- PyMuPDF (para a extração de texto de arquivos PDF)

Certifique-se de ter os pré-requisitos instalados antes de executar o aplicativo.

## Instalação

1. Clone este repositório para o seu ambiente local:

git clone https://github.com/rodineyw/transcricao_text.git


2. Instale as dependências:

pip install -r requirements.txt

3. Execute o aplicativo:

python app.py


## Como usar

1. Abra o aplicativo.
2. No menu "Arquivo", selecione "Abrir" para escolher um arquivo PDF ou uma imagem.
3. O texto extraído será exibido na área de texto.
4. Você pode copiar o texto para outros fins, se desejar.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para reportar problemas ou sugerir melhorias. Se desejar contribuir com código, por favor, envie um pull request.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
