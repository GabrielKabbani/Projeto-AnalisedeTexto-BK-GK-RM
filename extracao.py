import requests

data_url = "https://d18rn0p25nwr6d.cloudfront.net/CIK-0000320193/b4266e40-1de6-4a34-9dfb-8632b8bd57e0.pdf" #link para o 10k da Apple

nome_saida = 'apple10k.pdf'

def baixa(pdf_url, nome_saida):
    response = requests.get(pdf_url) #pegando o pdf
    
    response.raise_for_status()  # vendo se está válido

    with open(nome_saida, 'wb') as output_file:
    
        output_file.write(response.content) #escrevendo arquvio de saida

baixa(data_url, nome_saida)