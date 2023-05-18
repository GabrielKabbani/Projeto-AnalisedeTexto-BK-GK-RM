import requests

# OCR
import easyocr

# PDF para imagem
from pdf2image import convert_from_path

# para trabalhar com diretórios / sistema operacional
import os

# para os DataFrames
import pandas as pd

# para exibir os arquivos de imagem
import cv2
import matplotlib.pyplot as plt

data_url = "https://d18rn0p25nwr6d.cloudfront.net/CIK-0000320193/b4266e40-1de6-4a34-9dfb-8632b8bd57e0.pdf" #link para o 10k da Apple

nome_saida = 'apple10k.pdf'

def baixa(pdf_url, nome_saida):
    response = requests.get(pdf_url) #pegando o pdf
    
    response.raise_for_status()  # vendo se está válido

    with open(nome_saida, 'wb') as output_file:
    
        output_file.write(response.content) #escrevendo arquvio de saida

baixa(data_url, nome_saida)


paginas = convert_from_path('apple10k.pdf', 200)

#Salvando cada pagina do PDF como imagem para extracao usando OCR
i = 1
lista_imagens = []
for pg in paginas:
    img_path = './img/Apple10k_{}.jpg'.format(i)
    pg.save(img_path, 'JPEG')
    lista_imagens.append(img_path)
    i += 1

#criando o objeto reader, mudar para False caso nao rode
reader = easyocr.Reader(['pt', 'en'], gpu = True) 

print(lista_imagens[0])

for image_path in lista_imagens:
    try:
        text = reader.readtext(image_path, detail=0)
        str_texto = " ".join(text)
        print(str_texto)
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")

print(str(str_texto))

with open('./text/texto.txt', 'w') as f:
    f.write(str_texto)
        
print(len(text))



